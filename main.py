from src.data_cleaning import load_and_clean_data
from src.analysis import basic_summary
from src.visualization import plot_monthly_profit, plot_roi_histogram, plot_top_clients

# Step 1: Load and clean data
df = load_and_clean_data("data/Project_Profitability_Tracker_100.csv")

# Step 2: Show summary
basic_summary(df)

# Step 3: Create visualizations
plot_monthly_profit(df)
plot_roi_histogram(df)
plot_top_clients(df)

print("\n✅ Analysis complete. Charts saved in the 'charts' folder.")
