
class PromptController:
    def __init__(self, role="Tutor"):
        self.role = role

    def build_prompt(self, user_input, memory):
        system_prompt = f""" You are AURA, a smart AI assistant.
        Your role is: {self.role}

        Rules:
        - Be polite
        - Explain clearly
        - Help like a human assistant

        Conversation History:
        {memory}

        User Question:
        {user_input}
        """
        return system_prompt
