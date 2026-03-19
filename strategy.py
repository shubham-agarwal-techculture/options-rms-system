from models import OrderRequest
from random import randint

# -----------------------------
# Strategy (Example)
# -----------------------------
class DummyStrategy:
    def generate_signal(self) -> OrderRequest:
        rand_num = randint(0,100)

        side = "BUY" if rand_num > 50 else "SELL"

       
        order = randint(1,10)
        return OrderRequest(
            symbol="NIFTY-OPT",
            qty=order,
            price=100.0,
            side=side,
            strategy="dummy"
        )
