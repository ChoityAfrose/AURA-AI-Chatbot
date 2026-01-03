import streamlit as st
import threading
from config.settings import Settings
from Aura.gemini_engine import GeminiEngine
from Aura.prompt_controller import PromptController
from Aura.memory import Memory
from Aura.assistant import AuraAssistant
from Aura.export_chat import ChatExporter
from datetime import datetime
import time

# Smart Greeting Based on Time of Day
def get_smart_greeting():
    hour = datetime.now().hour

    if 5 <= hour < 12:
        return "🌅 Good morning! I'm Aura, your AI assistant. How can I help you today?"
    elif 12 <= hour < 17:
        return "☀️ Good afternoon! I'm Aura. What can I assist you with?"
    elif 17 <= hour < 22:
        return "🌆 Good evening! I'm Aura, ready to help you."
    else:
        return "🌙 Hello! I'm Aura. How can I support you right now?"

# Typing Indicator  
def typing_indicator(placeholder, steps=4):
    dots = ["", ".", "..", "..."]
    emojis = ["🧠", "✨"]

    for i in range(steps):
        placeholder.markdown(
            f"{emojis[i % len(emojis)]} **Aura is typing{dots[i % len(dots)]}**"
        )
        time.sleep(0.8)


# Streamlit App Configuration
st.set_page_config(page_title="Aura AI", page_icon="🧠")

st.title("🧠 Aura – Your AI Assistant")

# Sidebar
role = st.sidebar.selectbox("Select Assistant Role", ["Tutor", "Coder", "Mentor", "Resume Helper"])

response_length = st.sidebar.selectbox(
    "Response Length",
    ["Short", "Medium", "Detailed"]
)

# Memory Management
memory = Memory()

# Export Chat
exporter = ChatExporter()

if st.sidebar.button("🗑 Clear Memory"):
    memory.clear()
    st.session_state.chat_history = []
    st.toast("🧹 Memory Cleared", icon="✅")

if st.sidebar.button("💾 Export Chat"):
    chat_text = exporter.export_txt()
    st.download_button(
        label="Download Chat",
        data=exporter.export_txt(),
        file_name="chat_history.txt",
        mime="text/plain"
    )

# Initialize
settings = Settings()
engine = GeminiEngine(settings.load_api_key())
controller = PromptController(role, response_length)
aura = AuraAssistant(engine, controller, memory)


# Chat

if "greeted" not in st.session_state:
    st.session_state.greeted = False

if "processing" not in st.session_state:
    st.session_state.processing = False

if "last_user_input" not in st.session_state:
    st.session_state.last_user_input = ""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "last_role" not in st.session_state:
    st.session_state.last_role = role

if role != st.session_state.last_role:
    st.session_state.chat_history = []
    memory.clear()
    st.session_state.chat_history.append(
        {"role": "assistant",
         "message": f"🔄 Switched to **{role} Mode**.\n\nHow can I help you as a {role.lower()}?"}
    )
    st.session_state.last_role = role

if len(st.session_state.chat_history) == 0:
    st.session_state.chat_history.append(
        {"role": "assistant", "message": get_smart_greeting()}
    )

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["message"])

user_input = st.chat_input("Type your message")

if user_input and not st.session_state.processing:
    st.session_state.processing = True
    st.session_state.last_user_input = user_input
    st.session_state.chat_history.append(
        {"role": "user", "message": user_input}
    )

if st.session_state.processing:
    st.chat_message("User").write(st.session_state.last_user_input)
    with st.chat_message("assistant"):
        # Typing indicator
        typing_placeholder = st.empty()

        # show typing animation (short)
        typing_indicator(typing_placeholder)

        typing_placeholder.empty()
        
        response_box = st.empty()
        full_response = ""

        for chunk in aura.respond_stream(st.session_state.last_user_input):
            full_response += chunk
            response_box.markdown(full_response)

    st.session_state.chat_history.append(
        {"role": "assistant", "message": full_response}
    )

    st.session_state.processing = False
    st.session_state.last_user_input = ""


