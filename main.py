import time
from trading_orchestrator import TradingSystem
# -----------------------------
# Run
# -----------------------------
system = TradingSystem()

for _ in range(5):
    system.run_once()
    time.sleep(1)