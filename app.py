import streamlit as st
from config.settings import Settings
from Aura.gemini_engine import GeminiEngine
from Aura.prompt_controller import PromptController
from Aura.memory import Memory
from Aura.assistant import AuraAssistant
from Aura.voice_input import VoiceInput
from Aura.export_chat import ChatExporter
# Streamlit App Configuration
st.set_page_config(page_title="Aura AI", page_icon="🧠")

st.title("🧠 Aura – Your AI Assistant")

# Sidebar
role = st.sidebar.selectbox("Select Assistant Role", ["Tutor", "Coder", "Mentor"])

# Memory Management
memory = Memory()

# Export Chat
exporter = ChatExporter()

if st.sidebar.button("🗑 Clear Memory"):
    memory.clear()
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
controller = PromptController(role)
aura = AuraAssistant(engine, controller, memory)
voice = VoiceInput()

# Chat

if "processing" not in st.session_state:
    st.session_state.processing = False

if "last_user_input" not in st.session_state:
    st.session_state.last_user_input = ""


user_input = st.chat_input("Type your message")

if user_input and not st.session_state.processing:
    st.session_state.processing = True
    st.session_state.last_user_input = user_input

if st.session_state.processing:
    st.chat_message("User").write(st.session_state.last_user_input)
    with st.chat_message("assistant"):
        response_box = st.empty()
        full_response = ""

        for chunk in aura.respond_stream(st.session_state.last_user_input):
            full_response += chunk
            response_box.markdown(full_response)

    st.session_state.processing = False
    st.session_state.last_user_input = ""


