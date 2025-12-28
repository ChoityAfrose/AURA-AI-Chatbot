import json

class ChatExporter:
    def export_txt(self, memory_file="memory.json"):
        with open(memory_file, "r") as f:
            data = json.load(f)

        content = ""
        for chat in data:
            content += f"{chat['role']}: {chat['message']}\n\n"

        return content
