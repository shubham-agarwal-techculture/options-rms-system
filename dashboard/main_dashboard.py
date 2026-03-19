"""
Decoupled Risk Dashboard
- Reads logs or state from file (or stream later)
- Displays live risk metrics
- Can be extended to web dashboard (FastAPI/Streamlit)
"""

import time
import json
from collections import defaultdict

LOG_FILE = "C:\\Users\\Pc\\Desktop\\Shubham\\My work\\options_risk_framework\\log.jsonl"  # assume logs written here

class RiskDashboard:
    def __init__(self):
        self.positions = defaultdict(int)
        self.pnl = 0
        self.delta = 0
        self.gamma = 0
        self.vega = 0

    def process_log(self, log):
        event = log.get("event")

        if event == "POSITION_UPDATED":
            self.positions = log.get("positions", {})
            self.pnl = log.get("pnl", 0)
            self.delta = log.get("portfolio_delta", 0)
            self.gamma = log.get("portfolio_gamma", 0)
            self.vega = log.get("portfolio_vega", 0)

    def display(self):
        print("\n===== RISK DASHBOARD =====")
        print(f"PnL: {self.pnl}")
        print(f"Positions: {self.positions}")
        print(f"Delta: {self.delta}")
        print(f"Gamma: {self.gamma}")
        print(f"Vega: {self.vega}")
        print("==========================\n")

    def load_logs(self):
        try:
            with open(LOG_FILE, "r") as f:
                for line in f:
                    log = json.loads(line.strip())
                    self.process_log(log)
        except FileNotFoundError:
            pass

    def run(self):
        print("Starting Risk Dashboard...")
        seen = 0

        while True:
            try:
                with open(LOG_FILE, "r") as f:
                    lines = f.readlines()

                new_lines = lines[seen:]
                seen = len(lines)

                if new_lines:
                    for line in new_lines:
                        log = json.loads(line.strip())
                        self.process_log(log)
                    self.display()

                time.sleep(2)



            except FileNotFoundError:
                print("Waiting for log file...")
                time.sleep(2)


if __name__ == "__main__":
    dashboard = RiskDashboard()
    dashboard.run()
