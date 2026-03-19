import time
import json

# -----------------------------
# Logger (Simple Observability)
# -----------------------------
class Logger:
    @staticmethod
    def log(message: dict):
        message["timestamp"] = time.time()
        # print(message)
        with open("log.jsonl", "a") as f:
            f.write(json.dumps(message) + "\n")
    
