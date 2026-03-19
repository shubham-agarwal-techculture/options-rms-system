from dataclasses import dataclass, field
from typing import Dict, List

# -----------------------------
# Models
# -----------------------------
@dataclass
class OrderRequest:
    symbol: str
    qty: int
    price: float
    side: str  # BUY / SELL
    strategy: str
    delta: float = 0.0
    gamma: float = 0.0
    vega: float = 0.0

@dataclass
class Position:
    symbol: str
    qty: int = 0
    avg_price: float = 0.0
    delta: float = 0.0
    gamma: float = 0.0
    vega: float = 0.0

@dataclass
class Portfolio:
    cash: float
    positions: Dict[str, Position] = field(default_factory=dict)
    realized_pnl: float = 0.0

    def total_greeks(self):
        total_delta = sum(p.delta for p in self.positions.values())
        total_gamma = sum(p.gamma for p in self.positions.values())
        total_vega = sum(p.vega for p in self.positions.values())
        return total_delta, total_gamma, total_vega