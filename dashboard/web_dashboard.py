import streamlit as st
import pandas as pd
import json
import time


st.set_page_config(layout="wide")

st.title("📊 Options Risk Dashboard")

# Refresh moved to end

LOG_FILE = "../log.jsonl"

# Load logs
data = []
try:
    with open(LOG_FILE) as f:
        for line in f:
            log = json.loads(line)
            if log["event"] == "POSITION_UPDATED":
                data.append(log)
except:
    st.warning("Waiting for data...")

if data:
    df = pd.DataFrame(data)

    latest = df.iloc[-1]

    # ---- KPI ROW ----
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("PnL", latest["pnl"])
    col2.metric("Delta", latest["portfolio_delta"])
    col3.metric("Gamma", latest["portfolio_gamma"])
    col4.metric("Vega", latest["portfolio_vega"])

    # ---- CHARTS ----
    st.subheader("PnL Trend")
    st.line_chart(df["pnl"])

    st.subheader("Greeks Exposure")
    st.line_chart(df[["portfolio_delta", "portfolio_gamma", "portfolio_vega"]])

    # ---- POSITIONS ----
    st.subheader("Positions")
    st.json(latest["positions"])

# Auto refresh every 2 sec
time.sleep(2)
st.rerun()

# import streamlit as st
# from main_dashboard import RiskDashboard
# import time

# # -----------------------------
# # Streamlit UI
# # -----------------------------
# st.set_page_config(page_title="Risk Dashboard", layout="wide")

# st.title("📊 Options Risk Dashboard")

# placeholder = st.empty()

# while True:
#     dashboard = RiskDashboard()
#     dashboard.load_logs()

#     with placeholder.container():
#         col1, col2, col3, col4 = st.columns(4)

#         col1.metric("PnL", dashboard.pnl)
#         col2.metric("Delta", dashboard.delta)
#         col3.metric("Gamma", dashboard.gamma)
#         col4.metric("Vega", dashboard.vega)

#         st.subheader("Positions")
#         st.json(dashboard.positions)

#     time.sleep(2)
