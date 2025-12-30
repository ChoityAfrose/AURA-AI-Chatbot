# 🧠 Aura – Personal AI Assistant

Aura is a smart, role-based AI assistant built using Python, Streamlit, and Google Gemini API. It provides streaming responses, chat memory, and multiple assistant roles.

## 🎯 Project Objective

The goal of this project is to design and develop a personal AI assistant capable of:

- Answering general questions
- Helping with learning and productivity
- Acting based on different assistant roles
- Maintaining conversation history
- Providing real-time streaming responses

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

## ✨ Core Features

- ChatGPT-style chat interface
- Role-based prompt behavior
- Markdown-safe streaming responses
- Persistent conversation memory (JSON)
- Clear memory option
- Export chat history as `.txt`
- Secure API key handling using `.env`

## 📁 Project Structure

```text
AURA_AI_CHATBOT/
│
├── app.py
│
├── Aura/
│   ├── assistant.py
│   ├── gemini_engine.py
│   ├── prompt_controller.py
│   ├── memory.py
│   └── export_chat.py
│
├── config/
│   └── settings.py
│
├── .env
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

[▶️ Watch Project Demo Video](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

## Author

Assistant Programmer at Bangabhaban  
Full-Stack Data Science & Generative AI Learner | Python | NLP | AI Automation

## 📄 License
This project is intended for educational purposes.