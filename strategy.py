from models import OrderRequest

# -----------------------------
# Strategy (Example)
# -----------------------------
class DummyStrategy:
    def generate_signal(self) -> OrderRequest:
        return OrderRequest(
            symbol="NIFTY-OPT",
            qty=10,
            price=100.0,
            side="BUY",
            strategy="dummy"
        )
