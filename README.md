# 🧠 Aura – Personal AI Assistant

Aura is a smart, role-based AI assistant built with Python, Streamlit, and Google Gemini API.
It provides a modern ChatGPT-style interface with streaming responses, memory, smart greetings, role switching, and UX enhancements.

## 🎯 Project Objective

The objective of Aura is to demonstrate how to build a production-style AI assistant using clean architecture and OOP principles that can:

- Answer general and technical questions
- Adapt behavior based on selected assistant roles
- Stream responses in real time
- Maintain and manage conversation memory
- Provide a polished user experience

## 🛠 Tech Stack

- Python 3.11+
- Streamlit
- Google Gemini API
- python-dotenv
- JSON (for memory storage)

## 🧠 OOP Concepts Used

- Classes & Objects
- Encapsulation
- Inheritance
- Modular Coding
- Separation of Concerns
- Single Responsibility Principle

## 🤖 Assistant Roles

### 🟢 Tutor
- Explains concepts step by step
- Uses simple language
- Ideal for beginners and learners

### 🔵 Mentor
- Provides high-level guidance
- Focuses on real-world usage and best practices
- Helps with career and learning direction

### 🟣 Coder
- Gives technical explanations
- Uses code examples
- Focuses on implementation details

### 🟠 Resume Helper
- Helps improve resumes
- Suggests professional wording
- Provides structured feedback

## ✨ Core Features

- ChatGPT-style chat interface
- Smart greeting based on time of day
- Role-based prompt behavior
- Response length control (Short / Medium / Detailed)
- Streaming responses (word-by-word)
- Animated typing indicator (UX polish)
- Persistent conversation memory (JSON)
- Clear memory functionality
- Export chat history as `.txt`
- Secure API key handling using `.env`

## 📁 Project Structure

```text
AURA_AI_CHATBOT/
│
├── app.py                      # Streamlit UI & app logic
│
├── Aura/
│   ├── assistant.py            # Core assistant logic
│   ├── gemini_engine.py        # Gemini API wrapper
│   ├── prompt_controller.py    # Role & response control
│   ├── memory.py               # JSON-based memory
│   └── export_chat.py          # Chat export feature
│
├── config/
│   └── settings.py             # Environment & config loader
│
├── .env                        # API key (ignored by git)
├── requirements.txt
└── README.md

```

## 🔐 Security

- API key is stored in .env

- .env file is excluded from GitHub using .gitignore

- No Gemini logic is placed inside app.py

## 🚀 How to Run the Project

### Clone the Repository

```bash
git clone https://github.com/your-username/AURA-AI-CHATBOT.git

cd AURA-AI-CHATBOT
```
### Create Virtual Environment

```bash
conda create -n aura python=3.11

conda activate aura
```
### Install Dependencies

```bash
pip install -r requirements.txt
```
### Add Environment Variable

```env
GEMINI_API_KEY=your_api_key_here
```

### Run the Application
```bash
streamlit run app.py
```

## 🧠 Application Flow
```pgsql
User Input
   ↓
Memory → PromptController → GeminiEngine
   ↓
Streaming Response
   ↓
Streamlit Chat UI

```
## 🎥 Project Demo Video

[▶️ Watch Project Demo Video](https://www.linkedin.com/posts/choityromena_ai-generativeai-python-activity-7414233850194669568-lf-I?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEtCk1gBGeWIL99lLclKYglEj8FnMYtkIM0)

## Author

Romena Afrose Choity  
Assistant Programmer at Bangabhaban  
Full-Stack Data Science & Generative AI Learner | Python | NLP | AI Automation

## 📄 License
This project is intended for Educational Purposes.