# 🚀 Advanced Data Distribution Visualization System

A powerful, interactive Streamlit dashboard built in Python for seamless data cleaning, analysis, and visualization. Easily upload datasets or generate random ones, perform Exploratory Data Analysis (EDA), visualize distributions, and download filtered datasets.

## ✨ Features

- **Upload & Generate**: Load your own CSV files or generate a random mock dataset to instantly explore the dashboard.
- **Data Cleaning**: Tools to instantly drop missing (Null) values or duplicates from your data.
- **Dynamic Filters**: Select specific numeric and categorical columns to isolate exactly the data you want to see.
- **Interactive KPI Panel**: Dynamic Key Performance Indicators showing statistical measures: Mean, Max, Min.
- **Rich Visualizations**:
  - **Histograms & Box Plots**
  - **Scatter Plots & Violin Plots** 
  - **KDE (Kernel Density Estimation) Plots**
  - **Interactive Pair Plots**
  - **Correlation Heatmaps**
- **Download Ready**: Export your actively filtered and cleaned data securely as a CSV after exploration.

## 🛠️ Built With

- **[Streamlit](https://streamlit.io/)** - For the front-end web app framework
- **[Pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/)** - For data manipulation and mathematical analysis
- **[Plotly](https://plotly.com/)** - For highly interactive graphical charts
- **[Seaborn](https://seaborn.pydata.org/) & [Matplotlib](https://matplotlib.org/)** - For statistical data visualization

## 🚀 Getting Started

Follow these simple instructions to run the dashboard locally!

### Prerequisites

Ensure you have **Python 3** installed on your system.

### 1. Clone the Repository

```bash
git clone https://github.com/sudhanshu-199/Advanced-Data-Distribution-Visualization-System.git
cd Advanced-Data-Distribution-Visualization-System
```

### 2. Install Dependencies

You can configure a virtual environment (optional but recommended) and then install all requirements from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Execute the following command to start the Streamlit server:

```bash
streamlit run app.py
```

The application will launch and be available in your browser locally, typically at `http://localhost:8501`.

## 📸 Usage Workflow
1. Use the left **Dashboard Controls** to upload a CSV file or click **Generate Random Dataset**.
2. Apply Data Cleaning options if your uploaded data contains faults (e.g., removing nulls/duplicates).
3. Apply filters using the respective column selections for numeric/categorical features.
4. Interactively visualize your distributions utilizing the diverse graphical plots provided.
5. Hit **Download CSV** at the bottom to export the newly refined dataset!
