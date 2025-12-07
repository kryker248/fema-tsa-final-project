import streamlit as st
import pandas as pd
import plotly.express as px

st.title("FEMA TSA Analysis Dashboard")

@st.cache_data
def load_data():
    # CSV must be in the same repo
    return pd.read_csv("fema_clean_sample.csv")

df = load_data()

st.subheader("Data Preview")
st.write(df.head())

st.subheader("Repair Amount Distribution")
fig_hist = px.histogram(
    df,
    x="repairAmount",
    nbins=40,
    title="Distribution of Repair Amounts"
)
st.plotly_chart(fig_hist)

st.subheader("Repair Amount by TSA Eligibility")
fig_box = px.box(
    df,
    x="tsaEligible",
    y="repairAmount",
    labels={
        "tsaEligible": "TSA Eligible (1 = Yes, 0 = No)",
        "repairAmount": "Repair Amount"
    },
    title="Repair Amount by TSA Eligibility"
)
st.plotly_chart(fig_box)

st.write("Authors: Kyle Ryker & Julia McDemott")
