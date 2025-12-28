import json
import os

class Memory:
    def __init__(self, file_path='memory.json'):

        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)

    def add(self, role, message):
        history = self.get_history(raw=True)
        history.append({"role" : role, "message" : message})
        with open(self.file_path, 'w') as f:
            json.dump(history, f, indent=4)

    def get_history(self, raw=False):
        with open(self.file_path, 'r') as f:
            history = json.load(f)
        if raw:
            return history
        return "\n".join([f"{h['role']}: {h['message']}" for h in history]) 

    def clear(self):
        with open(self.file_path, "w") as f:
            json.dump([], f)