from models import OrderRequest, Position, Portfolio
# -----------------------------
# Risk Engine
# -----------------------------
class RiskEngine:
    def __init__(self, portfolio: Portfolio):
        self.portfolio = portfolio
        self.max_position_per_symbol = 100
        self.max_order_size = 50
        self.max_daily_loss = -5000

    def check_order(self, order: OrderRequest) -> (bool, str):
        pos = self.portfolio.positions.get(order.symbol, Position(order.symbol))

        # Check 1: order size
        if order.qty > self.max_order_size:
            return False, "Order size too large"

        # Check 2: position limit
        projected_qty = pos.qty + order.qty if order.side == "BUY" else pos.qty - order.qty
        if abs(projected_qty) > self.max_position_per_symbol:
            return False, "Position limit exceeded"

        # Check 3: daily loss
        if self.portfolio.realized_pnl < self.max_daily_loss:
            return False, "Daily loss limit breached"

        return True, "Approved"
