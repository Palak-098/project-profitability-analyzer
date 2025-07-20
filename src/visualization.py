import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_monthly_profit(df):
    os.makedirs("charts", exist_ok=True)
    monthly = df.groupby("Month")["Profit"].sum().reset_index().sort_values(by='Month')
    plt.figure(figsize=(10,5))
    sns.barplot(x="Month", y="Profit", data=monthly, palette="Blues_d")
    plt.title("Monthly Profit Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("charts/monthly_profit_trend.png")
    plt.close()

def plot_roi_histogram(df):
    os.makedirs("charts", exist_ok=True)
    plt.figure(figsize=(8,5))
    sns.histplot(df['ROI'], bins=20, kde=True, color='green')
    plt.title("ROI Distribution")
    plt.xlabel("ROI (%)")
    plt.tight_layout()
    plt.savefig("charts/roi_histogram.png")
    plt.close()

def plot_top_clients(df):
    os.makedirs("charts", exist_ok=True)
    top_clients = df.groupby("Client")["Profit"].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10,6))
    top_clients.plot(kind='bar', color='orange')
    plt.title("Top 10 Clients by Total Profit")
    plt.ylabel("Profit")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("charts/top_clients.png")
    plt.close()
