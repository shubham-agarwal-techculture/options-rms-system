import time

# -----------------------------
# Logger (Simple Observability)
# -----------------------------
class Logger:
    @staticmethod
    def log(message: dict):
        message["timestamp"] = time.time()
        print(message)
        with open("log.txt", "a") as f:
            f.write(str(message) + "\n")    
