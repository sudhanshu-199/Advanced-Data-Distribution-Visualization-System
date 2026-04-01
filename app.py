import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

sns.set(style="whitegrid")

st.set_page_config(page_title="Data Distribution Dashboard", layout="wide")

# Title
st.title("📊 Data Distribution Visualization Dashboard")

st.markdown("Explore, analyze, and visualize your data dynamically.")

# -------------------------------
# SIDEBAR
# -------------------------------

st.sidebar.header("⚙️ Controls")

data_option = st.sidebar.radio(
    "Select Data Source",
    ["Generate Random Data", "Upload CSV"]
)

# -------------------------------
# DATA LOADING
# -------------------------------

if data_option == "Generate Random Data":
    mean = st.sidebar.slider("Mean", 0, 100, 50)
    std = st.sidebar.slider("Standard Deviation", 1, 30, 10)
    size = st.sidebar.slider("Data Size", 50, 500, 200)

    data = np.random.normal(mean, std, size)
    df = pd.DataFrame(data, columns=["Values"])

else:
    uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        st.warning("Please upload a CSV file.")
        st.stop()

# -------------------------------
# DATA PREVIEW
# -------------------------------

st.subheader("📁 Dataset Preview")
st.dataframe(df.head())

# -------------------------------
# STATISTICS
# -------------------------------

st.subheader("📊 Statistical Summary")
st.write(df.describe())

# -------------------------------
# COLUMN SELECTION
# -------------------------------

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

if not numeric_cols:
    st.error("No numeric columns found!")
    st.stop()

column = st.selectbox("Select Column", numeric_cols)

# -------------------------------
# VISUALIZATION SECTION
# -------------------------------

st.subheader("📈 Visualizations")

col1, col2 = st.columns(2)

# Histogram
with col1:
    st.write("### Histogram")
    fig, ax = plt.subplots()
    ax.hist(df[column], bins=20)
    st.pyplot(fig)

# Histogram + KDE
with col2:
    st.write("### Histogram + KDE")
    fig, ax = plt.subplots()
    sns.histplot(df[column], kde=True, ax=ax)
    st.pyplot(fig)

# Box Plot
col3, col4 = st.columns(2)

with col3:
    st.write("### Box Plot")
    fig, ax = plt.subplots()
    sns.boxplot(x=df[column], ax=ax)
    st.pyplot(fig)

# KDE Plot
with col4:
    st.write("### KDE Plot")
    fig, ax = plt.subplots()
    sns.kdeplot(df[column], fill=True, ax=ax)
    st.pyplot(fig)

# Violin Plot
st.write("### Violin Plot")
fig, ax = plt.subplots()
sns.violinplot(x=df[column], ax=ax)
st.pyplot(fig)

# -------------------------------
# INTERACTIVE PLOT (PLOTLY)
# -------------------------------

st.subheader("⚡ Interactive Visualization")

fig = px.histogram(df, x=column, title="Interactive Histogram")
st.plotly_chart(fig)

# -------------------------------
# INSIGHTS
# -------------------------------

st.subheader("🧠 Insights")

mean_val = df[column].mean()
median_val = df[column].median()
std_val = df[column].std()

st.metric("Mean", f"{mean_val:.2f}")
st.metric("Median", f"{median_val:.2f}")
st.metric("Std Dev", f"{std_val:.2f}")

if mean_val > median_val:
    st.info("📌 Data is Right-Skewed")
elif mean_val < median_val:
    st.info("📌 Data is Left-Skewed")
else:
    st.info("📌 Data is Symmetric")

st.write("👉 Use box plot to detect outliers.")