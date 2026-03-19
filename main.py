import time
from trading_orchestrator import TradingSystem
# -----------------------------
# Run
# -----------------------------
system = TradingSystem()

# for _ in range(10):
while True:
    system.run_once()
    time.sleep(1)