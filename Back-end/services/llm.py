from langchain_groq import ChatGroq
from dotenv import load_dotenv
from schemas.interview import InterviewQnARequest, InterviewQnAResponse
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser


import os
import json

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize output parser
parser = StrOutputParser()



# Initialize the ChatGroq model
model = ChatGroq(model="llama-3.3-70b-versatile")

# Create the chat prompt
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(
        content=(
            "You are a senior technical recruiter and interviewer with deep industry experience.\n"
            "Given the candidate's CV, job title, job requirements, and job description:\n"
            "- Generate 8–12 interview questions relevant to the job.\n"
            "- Include a mix of scenario-based, behavioral, and project-specific questions.\n"
            "- Each item must include:\n"
            "    • 'question': A clearly phrased question\n"
            "    • 'answer': A plausible answer\n"
            "    • 'type': one of ['technical', 'behavioral', 'project','scenario']\n"
            "    • 'difficulty': one of ['easy', 'medium', 'hard']\n\n"
            "Return ONLY a valid JSON array like:\n"
            "[{{\"question\": str, \"answer\": str, \"type\": str, \"difficulty\": str}}]"
        )
    ),
    HumanMessage(
        content=(
            "CV Text:\n{cv_text}\n\n"
            "Job Title: {job_title}\n"
            "Requirements: {job_requirements}\n"
            "Description: {job_description}\n\n"
            "Generate the Q&A set now."
        )
    )
])

# Combine prompt, model, and parser into a chain
chain = prompt | model | parser
