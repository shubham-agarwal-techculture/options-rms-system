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

@dataclass
class Position:
    symbol: str
    qty: int = 0
    avg_price: float = 0.0

@dataclass
class Portfolio:
    cash: float
    positions: Dict[str, Position] = field(default_factory=dict)
    realized_pnl: float = 0.0
