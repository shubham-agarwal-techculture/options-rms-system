# Options Risk Framework

A simplified framework for options trading orchestration and risk management. This system simulates a trading loop where a strategy generates signals, which are then validated by a risk engine before being executed and updated in the portfolio.

## Architecture Overview

The system is built with a modular architecture to separate concerns:

- **Trading Orchestrator**: The central hub (`trading_orchestrator.py`) that coordinates the flow between strategy, risk, execution, and portfolio management.
- **Risk Engine**: Validates every order against predefined safety limits (`risk_engine.py`).
- **Strategy**: A module for generating randomized trading signals (`strategy.py`). It generates random BUY/SELL orders with varying quantities.
- **Execution Engine**: Simulates the execution of approved orders (`execution_engine.py`).
- **Portfolio Manager**: Maintains the state of positions and calculates realized PnL (`portfolio_manager.py`).
- **Models**: Defines the core data structures for the system (`models.py`).

## Features

- **Order Validation**: Automatic checks for order size, position limits per symbol, and daily loss thresholds.
- **Position Tracking**: Real-time updates to position quantity and average cost.
- **PnL Calculation**: Automated tracking of realized profit and loss.
- **Event Logging**: Detailed logging of every step in the trading lifecycle. Logs are printed to the console and persisted to `log.txt` (`logger.py`).

## Getting Started

### Prerequisites

- Python 3.8+

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd options_risk_framework
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

### Running the System

To run the live trading simulation:

```bash
python main.py
```

The system will run in an infinite loop, generating and processing orders every second. To stop the simulation, press `Ctrl+C`.

## Project Structure

- `main.py`: Entry point for the simulation loop (runs infinitely).
- `trading_orchestrator.py`: `TradingSystem` class for orchestrating the trading workflow.
- `risk_engine.py`: `RiskEngine` class for order validation.
- `portfolio_manager.py`: `PortfolioManager` class for state management.
- `execution_engine.py`: Mock `ExecutionEngine` for order fulfillment.
- `strategy.py`: `DummyStrategy` for randomized signal generation.
- `models.py`: Dataclasses for `OrderRequest`, `Position`, and `Portfolio`.
- `logger.py`: Utility for logging system events to console and `log.txt`.
- `log.txt`: Persistent log file containing the history of all trading events.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details (if available).
