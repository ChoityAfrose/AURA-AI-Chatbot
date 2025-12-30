import time
from time import sleep


class AuraAssistant:
    def __init__(self, engine, prompt_controller, memory):
        self.engine = engine
        self.prompt_controller = prompt_controller
        self.memory = memory

    def respond(self, user_input):
        self.memory.add("User", user_input)
        
        prompt = self.prompt_controller.build_prompt(user_input, self.memory.get_history())

        response = self.engine.generate(prompt)

        self.memory.add("Aura Assistant", response)
        return response
    

    def respond_stream(self, user_input):
        self.memory.add("User", user_input)

        prompt = self.prompt_controller.build_prompt(
            user_input, self.memory.get_history()
        )

        full_response = self.engine.generate(prompt)
        self.memory.add("Aura Assistant", full_response)

        # ✅ Stream by LINE (markdown-safe)
        for line in full_response.split("\n"):
            yield line + "\n"
            time.sleep(0.08)