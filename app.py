import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Advanced Data Visualization System",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("🚀 Advanced Data Distribution Visualization System")

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Dashboard Controls")

# Upload or generate data
uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])
generate_data = st.sidebar.button("Generate Random Dataset")

# ---------------- LOAD DATA ----------------
if uploaded_file:
    df = pd.read_csv(uploaded_file)

elif generate_data:
    df = pd.DataFrame({
        "Sales": np.random.randint(100, 1000, 300),
        "Profit": np.random.randn(300) * 100,
        "Quantity": np.random.randint(1, 50, 300),
        "Discount": np.random.rand(300),
        "Category": np.random.choice(["Electronics", "Clothing", "Food"], 300)
    })

else:
    st.warning("⚠️ Please upload a dataset or generate sample data.")
    st.stop()

# ---------------- DATA CLEANING ----------------
st.sidebar.subheader("🧹 Data Cleaning")

if st.sidebar.checkbox("Remove Null Values"):
    df = df.dropna()

if st.sidebar.checkbox("Remove Duplicates"):
    df = df.drop_duplicates()

# ---------------- DATA PREVIEW ----------------
st.subheader("📄 Dataset Preview")
st.dataframe(df, use_container_width=True)

# ---------------- COLUMN TYPES ----------------
numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
categorical_cols = df.select_dtypes(include='object').columns.tolist()

# ---------------- FILTERS ----------------
st.sidebar.subheader("🔍 Filters")

selected_num_cols = st.sidebar.multiselect(
    "Select Numeric Columns",
    numeric_cols,
    default=numeric_cols[:2]
)

if categorical_cols:
    selected_cat_col = st.sidebar.selectbox("Select Category Column", categorical_cols)
    selected_values = st.sidebar.multiselect(
        "Filter Category Values",
        df[selected_cat_col].unique()
    )
    
    if selected_values:
        df = df[df[selected_cat_col].isin(selected_values)]

# ---------------- KPI METRICS ----------------
st.subheader("📊 Key Performance Indicators")

if selected_num_cols:
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Mean", round(df[selected_num_cols[0]].mean(), 2))
    col2.metric("Max", round(df[selected_num_cols[0]].max(), 2))
    col3.metric("Min", round(df[selected_num_cols[0]].min(), 2))

# ---------------- VISUALIZATION ----------------
st.subheader("📈 Visualizations")

colA, colB = st.columns(2)

# Histogram
with colA:
    st.markdown("### Histogram")
    fig = px.histogram(
        df,
        x=selected_num_cols[0],
        color=selected_cat_col if categorical_cols else None
    )
    st.plotly_chart(fig, use_container_width=True)

# Box Plot
with colB:
    st.markdown("### Box Plot")
    fig = px.box(
        df,
        y=selected_num_cols[0],
        color=selected_cat_col if categorical_cols else None
    )
    st.plotly_chart(fig, use_container_width=True)

# Scatter Plot
st.markdown("### 🔥 Scatter Plot")
if len(selected_num_cols) >= 2:
    fig = px.scatter(
        df,
        x=selected_num_cols[0],
        y=selected_num_cols[1],
        color=selected_cat_col if categorical_cols else None
    )
    st.plotly_chart(fig, use_container_width=True)

# Violin Plot
st.markdown("### 🎻 Violin Plot")
fig = px.violin(df, y=selected_num_cols[0], box=True)
st.plotly_chart(fig, use_container_width=True)

# KDE Plot
st.markdown("### 📊 KDE Plot")
fig, ax = plt.subplots()
sns.kdeplot(df[selected_num_cols[0]], fill=True, ax=ax)
st.pyplot(fig)

# ---------------- CORRELATION ----------------
st.markdown("### 🔥 Correlation Heatmap")
fig, ax = plt.subplots()
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# ---------------- PAIR PLOT ----------------
st.markdown("### 📊 Pair Plot (EDA)")
if st.checkbox("Show Pair Plot"):
    fig = sns.pairplot(df[numeric_cols])
    st.pyplot(fig)

# ---------------- SUMMARY ----------------
st.subheader("📊 Summary Statistics")
st.write(df.describe())

# ---------------- DOWNLOAD ----------------
st.subheader("⬇️ Download Filtered Data")
st.download_button(
    "Download CSV",
    df.to_csv(index=False),
    file_name="filtered_data.csv"
)