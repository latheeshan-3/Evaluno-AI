# Evaluno AI – Smart Recruitment Platform

<div align="center">

![Evaluno AI](https://img.shields.io/badge/Evaluno-AI%20Recruitment-blue?style=for-the-badge)
![Next.js](https://img.shields.io/badge/Next.js-15.3-black?style=for-the-badge&logo=next.js)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-Latest-47A248?style=for-the-badge&logo=mongodb)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

A modern AI-powered recruitment system designed to streamline candidate evaluation, automated shortlisting, and intelligent interview generation.

[Features](#features) • [Installation](#installation) • [Tech Stack](#tech-stack) • [API Docs](#api-testing) • [License](#license)

</div>

---

## ✨ Features

- 🤖 **AI-powered resume evaluation** - Intelligent parsing and analysis of candidate resumes
- 💬 **Automated interview question generation** - Context-aware questions based on job requirements
- 👥 **Role-based recruitment workflows** - Customizable hiring pipelines
- 🔐 **JWT-secured authentication** - Enterprise-grade security
- 🎨 **Modern and responsive UI** - Built with Next.js 15 and Tailwind CSS
- ⚡ **Fast real-time communication** - Optimized Next.js ↔ FastAPI integration
- 📄 **Resume parsing** - Support for PDF and DOCX formats

---

## 📁 Project Structure

```
/evaluno-ai
│
├── front-end/               # Next.js UI
│   ├── app/
│   ├── components/
│   ├── public/
│   ├── package.json
│   └── ...
│
└── back-end/                # FastAPI backend
    ├── main.py
    ├── routes/
    ├── models/
    ├── services/
    │   └── ai_service.py
    ├── .env
    ├── requirements.txt
    └── ...
```

---

## 🛠️ Tech Stack

### Frontend (Next.js)
- **Next.js 15** - React framework
- **React 19** - UI library
- **Tailwind CSS v4** - Styling
- **Framer Motion** - Animations
- **Three.js + Vanta.js** - 3D graphics
- **JWT-Decode** - Token handling

### Backend (FastAPI)
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
- **MongoDB** (Motor + PyMongo) - Database
- **LangChain** - AI orchestration
- **Groq API** - LLM integration (LLaMA3/Mixtral)
- **PyMuPDF** - PDF parsing
- **python-docx** - DOCX parsing
- **JWT authentication** - Secure auth
- **Pydantic v2** - Data validation

---

## 🚀 Installation

### Prerequisites
- Node.js 18+ and npm
- Python 3.9+
- MongoDB (local or Atlas)

### Backend Setup (FastAPI)

1. **Navigate to Backend**
```bash
cd back-end
```

2. **Create and Activate Virtual Environment**
```bash
# Mac/Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Environment Variables**

Create a `.env` file inside `back-end/`:

```env
GROQ_API_KEY=your_groq_api_key_here
MONGO_URI=mongodb://localhost:27017/evaluno
SECRET_KEY=your_secret_key_here
```

> ⚠️ **Note**: Replace the API keys with your own credentials. Never commit `.env` files to version control.

5. **Start Backend Server**
```bash
uvicorn main:app --reload --port 8000
```

Backend will be available at: **http://localhost:8000**

---

### Frontend Setup (Next.js)

1. **Navigate to Frontend**
```bash
cd front-end
```

2. **Install Dependencies**
```bash
npm install
```

3. **Start Development Server**
```bash
npm run dev
```

Frontend will be available at: **http://localhost:3000**

---

## 🔌 Frontend ↔ Backend Integration

The frontend communicates with FastAPI using:

```
http://localhost:8000/api/...
```

> **Important**: Ensure the backend is running before starting the frontend.

---

## 📦 Dependencies

### Frontend (package.json)
```json
{
  "dependencies": {
    "framer-motion": "^12.23.6",
    "jwt-decode": "^4.0.0",
    "next": "15.3.3",
    "react": "^19.0.0",
    "react-countup": "^6.5.3",
    "react-dom": "^19.0.0",
    "three": "^0.178.0",
    "vanta": "^0.5.24"
  }
}
```

### Backend (requirements.txt)
```txt
fastapi==0.109.1
uvicorn==0.27.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
pymongo==4.7.2
motor==3.3.1
python-dotenv==1.0.0
pydantic==2.11.5
pydantic-settings==2.9.1
PyJWT==2.8.0
email-validator==2.1.1
langchain-groq
langchain
PyMuPDF
python-docx
python-multipart
```

---

## 🧪 API Testing

You can test API endpoints using:

- **FastAPI Swagger UI** → http://localhost:8000/docs
- **Postman**
- **Thunder Client** (VS Code extension)
- **cURL**

Example API endpoint:
```bash
curl -X GET http://localhost:8000/api/candidates
```

---

## 🤖 AI & Groq Integration

Evaluno AI uses:
- **LangChain** - AI orchestration framework
- **Groq LLaMA3 / Mixtral models** - High-performance LLMs

### AI Capabilities:
- Resume evaluation and scoring
- Job-specific interview question generation
- Candidate ranking and shortlisting
- Skills gap analysis

AI logic is located in:
```
back-end/services/ai_service.py
```

---

## 🔐 Authentication

The backend includes:
- ✅ JWT token authentication
- ✅ Password hashing using `passlib[bcrypt]`
- ✅ Token verification using `python-jose`
- ✅ Secure environment-based secret keys

---

## 💾 Database (MongoDB)

Evaluno AI requires MongoDB running locally:

```
mongodb://localhost:27017/evaluno
```

### Alternative Options:
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) (Cloud)
- [AWS DocumentDB](https://aws.amazon.com/documentdb/)
- Docker MongoDB instance

---

## 📜 Scripts

### Frontend Commands

| Command | Description |
|---------|-------------|
| `npm run dev` | Run Next.js development server |
| `npm run build` | Build production bundle |
| `npm start` | Run production server |
| `npm run lint` | Run ESLint |

### Backend Commands

| Command | Description |
|---------|-------------|
| `uvicorn main:app --reload` | Start FastAPI server with hot reload |
| `pip install -r requirements.txt` | Install all Python dependencies |

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - you may modify, distribute, or extend this project as needed.

---

## 📞 Support

If you encounter any issues or have questions:

- Open an issue on GitHub
- Contact the development team
- Check the [API documentation](http://localhost:8000/docs)

---

<div align="center">

Made with ❤️ by the Evaluno AI Team

⭐ Star this repo if you find it helpful!

</div>
