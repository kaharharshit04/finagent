# 🤖 FinAgent: Multi-Modal RAG Financial Assistant

**FinAgent** is an intelligent AI assistant designed to analyze complex financial documents (PDFs, Excel, CSV) using a **Retrieval-Augmented Generation (RAG)** architecture. The project demonstrates how to build a production-grade AI tool using a FastAPI backend and a modern frontend, powered by Groq.

FinAgent provides context-aware answers to complex financial queries, showcasing how Large Language Models (LLMs) can be combined with vector search for real-world document intelligence.

---

## ✨ Features

- 📄 **Multi-File Processing:** Upload and analyze multiple PDFs, CSVs, and Excel files simultaneously.
- 🔍 **Semantic Search:** Uses RAG to find the exact context within your financial data.
- 🧠 **Agentic Reasoning:** Implements "Plan-and-Execute" logic to solve complex financial queries.
- ⚡ **High Performance:** Fast backend built with FastAPI and Groq LLM.
- 🎨 **Clean UI:** Responsive and intuitive dashboard for seamless document interaction.

---

## 🏗 Architecture

**User** ↓  
**React Frontend** ↓  
**API Requests** (FastAPI Backend) ↓  
**Vector Store** (Sentence-Transformers) ↓  
**LLM Orchestration** (Groq / Gemini API)

---

## 🛠 Tech Stack

### Frontend
- HTML
- Tailwind CSS / Material UI

### Backend
- Python
- FastAPI
- Pandas / PDFPlumber (Data Parsing)

### AI / LLM
- Groq (LLaMA-3)
- HuggingFace (Embeddings)

### Infrastructure
- AWS (Deployment)
- Git / GitHub

---

## 📂 Project Structure

⚙️ Installation
1. Clone the Repository

Bash
git clone [https://github.com/harshitkahar/FinAgent.git](https://github.com/harshitkahar/FinAgent.git)
cd FinAgent
2. Backend Setup

Bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
3. Environment Variables

Create a .env file in the root directory:

Code snippet
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_gemini_api_key
4. Running the App

Bash
uvicorn app.main:app --reload
The application will be available at: http://localhost:8000

🚀 Usage
Start the FastAPI server.

Open the web interface.

Upload your financial documents (PDF/Excel/CSV).

Ask complex questions like "What was my total spend on utilities last month?" or "Summarize the investment risks."

🌍 Live Demo
Web Application: https://finagent-hk.aws.amazon.com (Update with your actual link)

📌 Future Improvements
📊 Visual Analytics: Generate charts and graphs from financial data.

🔐 User Auth: Secure login and private document storage.

🏦 Bank API Integration: Connect directly to financial institutions.

💾 Persistent Vector DB: Use Pinecone or Milvus for long-term memory.

👨‍💻 Author
Harshit Kahar Software Developer & GenAI Enthusiast LinkedIn

⭐ Support
If you found this project useful, please consider giving it a ⭐ on GitHub!