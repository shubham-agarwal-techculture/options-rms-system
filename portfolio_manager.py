from models import OrderRequest, Position, Portfolio

# -----------------------------
# Portfolio Manager
# -----------------------------
class PortfolioManager:
    def __init__(self, portfolio: Portfolio):
        self.portfolio = portfolio

    def update_position(self, order: OrderRequest, fill_price: float):
        pos = self.portfolio.positions.get(order.symbol, Position(order.symbol))

        if order.side == "BUY":
            total_cost = pos.avg_price * pos.qty + fill_price * order.qty
            pos.qty += order.qty
            pos.avg_price = total_cost / pos.qty if pos.qty != 0 else 0
        else:
            pnl = (fill_price - pos.avg_price) * order.qty
            self.portfolio.realized_pnl += pnl
            pos.qty -= order.qty

        self.portfolio.positions[order.symbol] = pos
