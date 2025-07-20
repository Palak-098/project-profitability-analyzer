def basic_summary(df):
    return {
        "Total Projects": len(df),
        "Profitable Projects": len(df[df['Status'] == 'Profit']),
        "Loss-Making Projects": len(df[df['Status'] == 'Loss']),
        "Average ROI": f"{df['ROI'].mean():.2f}%",
        "Longest Project Duration": f"{df['Project_Duration'].max()} days",
        "Top Clients": df.groupby("Client")['Profit'].sum().sort_values(ascending=False).head()
    }
