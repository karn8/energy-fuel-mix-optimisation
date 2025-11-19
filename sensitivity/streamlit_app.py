import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="IC Sensitivity Dashboard", layout="wide")

@st.cache_data
def load_data(path):
    xls = pd.ExcelFile(path)
    fuels = pd.read_excel(xls, sheet_name="Fuels")
    params = pd.read_excel(xls, sheet_name="Parameters")
    prices = pd.read_excel(xls, sheet_name="ElectricityPrices")
    return fuels, params, prices

fuels, params, prices = load_data("ic_case_solver_final.xlsx")

st.sidebar.header("Sensitivity Controls")

roc = st.sidebar.slider("ROC value (£/MWh)", 30.0, 80.0, 45.0, 1.0)
co2_price = st.sidebar.slider("CO₂ Price (€ per tonne)", 0.0, 60.0, 15.0, 1.0)
efficiency = st.sidebar.slider("Plant Efficiency (%)", 25.0, 45.0, 35.0, 0.5)
fuel_adj = st.sidebar.slider("Fuel Price Adjustment (%)", -20.0, 50.0, 0.0, 1.0)

eff = efficiency / 100
eur_to_gbp = 0.87
co2_cost_gbp_per_mwh = co2_price * eur_to_gbp * 0.8  
fuels["Adj_Price"] = fuels["Price_per_tonne_GBP"] * (1 + fuel_adj / 100)
fuels["MWh_per_tonne"] = fuels["GJ_per_tonne"] * eff / 3.6
fuels["Fuel_cost_per_MWh"] = fuels["Adj_Price"] / fuels["MWh_per_tonne"]
fuels["ROC_per_MWh"] = np.where(fuels["Fuel"].str.contains("Wood", case=False), roc, 0)
fuels["CO2_cost_per_MWh"] = np.where(fuels["Fuel"].str.contains("Wood", case=False), 0, co2_cost_gbp_per_mwh)
fuels["Total_cost_per_MWh"] = fuels["Fuel_cost_per_MWh"] + fuels["CO2_cost_per_MWh"]

bands = prices.melt(id_vars="Month", var_name="Band", value_name="Price_£/MWh")
results = []
for _, row in bands.iterrows():
    month, band, price = row
    for _, f in fuels.iterrows():
        revenue = price
        profit = revenue - 0.65 - f["Total_cost_per_MWh"] + f["ROC_per_MWh"]
        results.append({
            "Month": month,
            "Band": band.replace("Weekday ", "").replace("Weekend ", ""),
            "Fuel": f["Fuel"],
            "Profit_£/MWh": profit
        })

df = pd.DataFrame(results)

st.title("International Coal Sensitivity Dashboard")

col1, col2 = st.columns([2, 3])

with col1:
    st.subheader("Profit per MWh by Fuel")
    fig1 = px.bar(df, x="Fuel", y="Profit_£/MWh", color="Fuel", barmode="group")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Monthly Profit Comparison (Mean by Fuel)")
    df_month = df.groupby(["Month", "Fuel"], as_index=False)["Profit_£/MWh"].mean()
    fig2 = px.line(df_month, x="Month", y="Profit_£/MWh", color="Fuel", markers=True)
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("📊 Data Summary")
st.dataframe(df.groupby("Fuel")["Profit_£/MWh"].mean().reset_index().sort_values("Profit_£/MWh", ascending=False))

st.caption("Move the sliders on the left to explore sensitivity impacts on profitability and fuel mix.")
