import pandas as pd

# 1. Load the cleaned data
# Assuming you are running this from the project root or 'src' folder
df = pd.read_csv('ecommerce_customers_cleaned.csv')

# --- CALCULATIONS ---

# 1. Average Revenue Per User (ARPU)
arpu = df['Yearly Amount Spent'].mean()

# 2. Engagement Distribution (Averages)
avg_time_app = df['Time on App'].mean()
avg_time_website = df['Time on Website'].mean()

# 3. Customer Lifetime Value (CLV) Proxy Analysis
# We define "Loyal" customers as those whose membership is longer than the average
avg_membership = df['Length of Membership'].mean()

loyal_customers = df[df['Length of Membership'] >= avg_membership]
new_customers = df[df['Length of Membership'] < avg_membership]

avg_spend_loyal = loyal_customers['Yearly Amount Spent'].mean()
avg_spend_new = new_customers['Yearly Amount Spent'].mean()

# --- CREATE TABLE VIEW ---

kpi_summary = pd.DataFrame({
    "Metric": [
        "Average Revenue Per User (ARPU)",
        "Avg Time on App",
        "Avg Time on Website",
        "Avg Membership Length",
        "Avg Spend (Loyal Customers)",
        "Avg Spend (New Customers)"
    ],
    "Value": [
        f"${arpu:.2f}",
        f"{avg_time_app:.2f} min",
        f"{avg_time_website:.2f} min",
        f"{avg_membership:.2f} years",
        f"${avg_spend_loyal:.2f}",
        f"${avg_spend_new:.2f}"
    ],
    "Business Context": [
        "Total average yearly spend",
        "Engagement on Mobile",
        "Engagement on Desktop",
        "Average customer age in system",
        "Spending of long-term members",
        "Spending of recent members"
    ]
})

# Display the table
print("\n--- ECOMMERCE KPI DASHBOARD ---")
print(kpi_summary.to_string(index=False))


kpi_summary.to_csv('./data/kpi_metrics.csv', index=False)