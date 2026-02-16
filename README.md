# Evaluno-AI

Evaluno-AI is an intelligent platform designed for automated interview processing and evaluation. It leverages a modern tech stack including FastAPI for the backend, Next.js for the frontend, and Langchain for AI-driven capabilities.

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- [Node.js](https://nodejs.org/) (v18.0.0 or higher)
- [Python](https://www.python.org/) (v3.10 or higher)
- [MongoDB](https://www.mongodb.com/) (Local or Atlas)
- An API Key for [Groq](https://console.groq.com/)

### 🛠️ Installation & Setup

#### 1. Clone the repository

```bash
git clone https://github.com/your-username/Evaluno-AI.git
cd Evaluno-AI
```

#### 2. Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd Back-end
   ```
2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables:
   Create a `.env` file in the `Back-end` directory and add the following:
   ```env
   GROQ_API_KEY=your_groq_api_key
   MONGO_URI=mongodb://localhost:27017/evaluno
   SECRET_KEY=your_secret_key
   ```
5. Run the development server:
   ```bash
   uvicorn main:app --reload
   ```

#### 3. Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd ../Front-end
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```
4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## 🏗️ Project Structure

```text
Evaluno-AI/
├── Back-end/         # FastAPI, MongoDB, Langchain
│   ├── routes/       # API endpoints
│   ├── services/     # Business logic
│   └── models/       # Database schemas
└── Front-end/        # Next.js, Three.js, Tailwind CSS
    └── app/          # Next.js Pages & Components
```

## 🧰 Tech Stack

- **Frontend**: Next.js, React, Three.js, Framer Motion, Tailwind CSS
- **Backend**: FastAPI, Langchain, Pydantic
- **Database**: MongoDB (Motor)
- **AI/LLM**: Groq (via Langchain)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
