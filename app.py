import streamlit as st
import pandas as pd

st.set_page_config(page_title="YTM ↔ سود بانکی")
st.title("📊 YTM ↔ تبدیل سود بانکی")

mode = st.radio(
    "نوع تبدیل:",
    ["YTM → سود بانکی", "سود بانکی → YTM"]
)

rate = st.number_input(
    "نرخ (درصد)",
    min_value=0.0,
    max_value=100.0,
    value=39.0
) / 100

if mode == "YTM → سود بانکی":
    result = 12 * ((1 + rate)**(1/12) - 1)
    st.success(f"سود بانکی معادل: {result*100:.2f}%")
else:
    result = (1 + rate/12)**12 - 1
    st.success(f"YTM معادل: {result*100:.2f}%")

# ===== NAV DATA =====
@st.cache_data
def load_navs():
    df = pd.read_csv("fund_navs.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

df_navs = load_navs()
