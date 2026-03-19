from models import OrderRequest

# -----------------------------
# Execution Engine (Mock)
# -----------------------------
class ExecutionEngine:
    def execute(self, order: OrderRequest):
        # Simulate execution
        return {
            "status": "FILLED",
            "fill_price": order.price
        }
