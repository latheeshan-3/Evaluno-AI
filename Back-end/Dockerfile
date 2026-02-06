# Use the official Python image
FROM python:3.12-slim-bookworm

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Set the working directory
WORKDIR /app

# Copy the rest of the application code
COPY . /app

# Install dependencies using pip
RUN pip install --no-cache-dir fastapi==0.109.1 uvicorn==0.27.0 \
    python-jose[cryptography]==3.3.0 passlib[bcrypt]==1.7.4 \
    pymongo==4.7.2 motor==3.3.1 python-dotenv==1.0.0 \
    pydantic==2.11.5 pydantic-settings==2.9.1 PyJWT==2.8.0 \
    email-validator==2.1.1 langchain-groq langchain \
    PyMuPDF python-docx python-multipart

# Expose the port the app runs on
EXPOSE 8000

# Run the application using uv
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
