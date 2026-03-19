import uuid

from models import OrderRequest, Position, Portfolio
from risk_engine import RiskEngine
from execution_engine import ExecutionEngine
from portfolio_manager import PortfolioManager
from strategy import DummyStrategy
from logger import Logger

# -----------------------------
# Trading System Orchestrator
# -----------------------------
class TradingSystem:
    def __init__(self):
        self.portfolio = Portfolio(cash=100000)
        self.logger = Logger()
        self.risk = RiskEngine(self.portfolio)
        self.execution = ExecutionEngine()
        self.pm = PortfolioManager(self.portfolio)
        self.strategy = DummyStrategy()

    def run_once(self):
        order = self.strategy.generate_signal()
        order_id = str(uuid.uuid4())

        self.logger.log({
            "event": "ORDER_REQUESTED",
            "order_id": order_id,
            "symbol": order.symbol,
            "qty": order.qty
        })

        approved, reason = self.risk.check_order(order)

        if not approved:
            self.logger.log({
                "event": "ORDER_REJECTED",
                "order_id": order_id,
                "reason": reason
            })
            return

        self.logger.log({
            "event": "ORDER_APPROVED",
            "order_id": order_id
        })

        result = self.execution.execute(order)

        self.logger.log({
            "event": "ORDER_EXECUTED",
            "order_id": order_id,
            "status": result["status"]
        })

        if result["status"] == "FILLED":
            self.pm.update_position(order, result["fill_price"])

            delta, gamma, vega = self.portfolio.total_greeks()

            self.logger.log({
                "event": "POSITION_UPDATED",
                "symbol": order.symbol,
                "positions": {k: v.qty for k, v in self.portfolio.positions.items()},
                "pnl": self.portfolio.realized_pnl,
                "portfolio_delta": delta,
                "portfolio_gamma": gamma,
                "portfolio_vega": vega
            })