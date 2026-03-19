# Options Risk Framework

A simplified framework for options trading orchestration and risk management. This system simulates a trading loop where a strategy generates signals, which are then validated by a risk engine before being executed and updated in the portfolio.

## Architecture Overview

The system is built with a modular architecture to separate concerns:

- **Trading Orchestrator**: The central hub (`trading_orchestrator.py`) that coordinates the flow between strategy, risk, execution, and portfolio management.
- **Risk Engine**: Validates every order against predefined safety limits (`risk_engine.py`). Now includes Greek limits (Delta, Gamma, Vega).
- **Strategy**: A module for generating trading signals (`strategy.py`). It generates orders with associated Greeks.
- **Execution Engine**: Simulates the execution of approved orders (`execution_engine.py`).
- **Portfolio Manager**: Maintains the state of positions, calculates realized PnL, and tracks portfolio-level Greeks (`portfolio_manager.py`).
- **Risk Dashboards**: 
    - **CLI Dashboard**: A standalone utility (`dashboard/main_dashboard.py`) for real-time monitoring in the terminal.
    - **Web Dashboard**: A modern Streamlit-based interface (`dashboard/web_dashboard.py`) for visual risk tracking and PnL trends.
- **Models**: Defines the core data structures for the system (`models.py`).

## Features

- **Order Validation**: Automatic checks for order size, position limits per symbol, and daily loss thresholds.
- **Greeks Management**: Real-time tracking and risk-limiting for Delta, Gamma, and Vega at the portfolio level.
- **Position Tracking**: Updates to position quantity, average cost, and Greeks.
- **PnL Calculation**: Automated tracking of realized profit and loss.
- **JSONL Logging**: Structured logging of every step in the trading lifecycle to `log.jsonl` for easy parsing and analysis.

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

The system will run in an infinite loop, generating and processing orders. Logs are written to `log.jsonl`.

To run the **Risk Dashboard**:

```bash
python dashboard/main_dashboard.py
```

The dashboard will read `log.jsonl` and provide a live view of your portfolio's risk state in your terminal.

To run the **Streamlit Web Dashboard**:

```bash
streamlit run dashboard/web_dashboard.py
```

This provides a rich visual experience with real-time PnL charts and Greeks exposure tracking.

## Project Structure

- `main.py`: Entry point for the simulation loop.
- `trading_orchestrator.py`: Orchestrates the trading workflow.
- `risk_engine.py`: Handles order validation and risk limits (including Greeks).
- `portfolio_manager.py`: Manages positions, PnL, and Greeks.
- `execution_engine.py`: Mock execution engine.
- `strategy.py`: Strategy module generating signals with Greek parameters.
- `models.py`: Data models for Orders, Positions, and Portfolio.
- `logger.py`: Structured JSONL logging utility.
- `dashboard/main_dashboard.py`: Real-time CLI risk monitoring dashboard.
- `dashboard/web_dashboard.py`: Modern Streamlit-based web dashboard with visualization.
- `log.jsonl`: Structured log file containing the history of all trading events.
- `fix_logs.py`: Utility to convert or fix malformed log files.

## License

This project is licensed under the MIT License.
