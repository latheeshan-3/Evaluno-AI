from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
import json

load_dotenv()

router = APIRouter()

# Initialize model + parser
model = ChatGroq(model="llama-3.3-70b-versatile")
parser = StrOutputParser()

# Request schema (if needed for other endpoints)
class InterviewTypeRequest(BaseModel):
    cv_text: str
    job_title: str
    job_requirements: str
    job_description: str
    type: str  # technical, behavioral, scenario, project

# ✅ Updated ChatPromptTemplate for LangChain 0.2+
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(
        content=(
            "You are a senior technical recruiter and interviewer with deep industry experience.\n"
            "Given the candidate's CV, job title, job requirements, and job description:\n"
            "- Generate 8–12 interview questions that are ONLY of type: {type}\n"
            "- Each item must include:\n"
            "    • 'question': A clearly phrased question\n"
            "    • 'answer': A plausible answer\n"
            "    • 'type': must be '{type}'\n"
            "    • 'difficulty': one of ['easy', 'medium', 'hard']\n\n"
            "Return ONLY valid JSON array like:\n"
            "[{\"question\": str, \"answer\": str, \"type\": str, \"difficulty\": str}]"
        )
    ),
    HumanMessage(
        content=(
            "CV Text:\n{cv_text}\n\n"
            "Job Title: {job_title}\n"
            "Requirements: {job_requirements}\n"
            "Description: {job_description}\n\n"
            "Generate only '{type}' questions."
        )
    ),
])

chain = prompt | model | parser


# ----------------------------- ROUTE --------------------------------

@router.post("/interview/generate-type")
async def generate_by_type_upload(
    cv_file: UploadFile = File(...),
    job_title: str = Form(...),
    job_requirements: str = Form(...),
    job_description: str = Form(...),
    type: str = Form(...)
):
    if type not in ["technical", "behavioral", "scenario", "project"]:
        raise HTTPException(status_code=400, detail="Invalid type specified")

    # Read uploaded CV
    try:
        contents = await cv_file.read()
        cv_text = contents.decode("utf-8", errors="ignore")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not read CV: {str(e)}")

    # Run model
    try:
        output = chain.invoke({
            "cv_text": cv_text,
            "job_title": job_title,
            "job_requirements": job_requirements,
            "job_description": job_description,
            "type": type,
        })

        print("LLM Output:", output)

        items = json.loads(output)
        return {"items": items}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing model response: {str(e)}")
