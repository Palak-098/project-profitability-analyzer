import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Layout setup
st.set_page_config(page_title="Project Profitability Dashboard", layout="wide")
st.title("📊 Project Profitability Analyzer")

# Load data
file_path = "data/Project_Profitability_Tracker_100.csv"
try:
    df = pd.read_csv(file_path)
except:
    st.error("❌ File not found. Check path.")
    st.stop()

# Clean & engineer data
df['Start_Date'] = pd.to_datetime(df['Start_Date'], errors='coerce')
df['End_Date'] = pd.to_datetime(df['End_Date'], errors='coerce')
df = df.dropna(subset=['Revenue', 'Cost', 'Start_Date', 'End_Date'])
df['Profit'] = df['Revenue'] - df['Cost']
df['ROI'] = (df['Profit'] / df['Cost']) * 100
df['Project_Duration'] = (df['End_Date'] - df['Start_Date']).dt.days
df['Month'] = df['Start_Date'].dt.strftime('%b-%Y')
df['Status'] = df['Profit'].apply(lambda x: 'Profit' if x >= 0 else 'Loss')

# Sidebar filters
st.sidebar.header("🔍 Filter Options")
clients = ["All"] + sorted(df["Client"].unique().tolist())
selected_client = st.sidebar.selectbox("Select Client", clients)

status_options = ["All", "Profit", "Loss"]
selected_status = st.sidebar.radio("Project Status", status_options)

months = ["All"] + sorted(df["Month"].unique().tolist())
selected_month = st.sidebar.selectbox("Select Month", months)

# Apply filters
filtered_df = df.copy()
if selected_client != "All":
    filtered_df = filtered_df[filtered_df["Client"] == selected_client]

if selected_status != "All":
    filtered_df = filtered_df[filtered_df["Status"] == selected_status]

if selected_month != "All":
    filtered_df = filtered_df[filtered_df["Month"] == selected_month]

# Data preview
st.subheader("📁 Filtered Data Preview")
st.dataframe(filtered_df.head())

# Summary
st.subheader("📋 Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Total Projects", len(filtered_df))
col2.metric("Profitable", len(filtered_df[filtered_df["Status"] == "Profit"]))
col3.metric("Loss-Making", len(filtered_df[filtered_df["Status"] == "Loss"]))

col4, col5 = st.columns(2)
col4.metric("Avg ROI", f"{filtered_df['ROI'].mean():.2f}%")
col5.metric("Longest Duration", f"{filtered_df['Project_Duration'].max()} days")

st.write("#### 💼 Top 5 Clients by Profit")
top_clients = filtered_df.groupby("Client")['Profit'].sum().sort_values(ascending=False).head()
st.dataframe(top_clients.reset_index().rename(columns={"Profit": "Total Profit"}))

# Monthly Profit Chart
st.subheader("📈 Monthly Profit Trend")
monthly = filtered_df.groupby("Month")["Profit"].sum().reset_index().sort_values(by="Month")
fig1, ax1 = plt.subplots(figsize=(10, 4))
sns.barplot(x="Month", y="Profit", data=monthly, ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# ROI Histogram
st.subheader("📊 ROI Distribution")
fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.histplot(filtered_df["ROI"], bins=20, kde=True, ax=ax2, color="green")
st.pyplot(fig2)

# Top 10 Clients
st.subheader("🏆 Top 10 Clients by Profit")
top_clients_chart = filtered_df.groupby("Client")["Profit"].sum().sort_values(ascending=False).head(10)
fig3, ax3 = plt.subplots(figsize=(8, 4))
top_clients_chart.plot(kind="bar", ax=ax3, color="orange")
st.pyplot(fig3)

# Profit vs Loss Pie
st.subheader("🥧 Profit vs Loss Distribution")
status_counts = filtered_df['Status'].value_counts()
fig4, ax4 = plt.subplots()
ax4.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90,
        colors=["#66bb6a", "#ef5350"])
ax4.axis('equal')
st.pyplot(fig4)

st.success("✅ Dashboard Loaded with Client, Status & Month Filters!")
