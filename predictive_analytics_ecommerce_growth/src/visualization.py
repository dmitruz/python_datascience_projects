import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the cleaned data
df = pd.read_csv('./data/processedecommerce_customerce_cleaned.csv')
# 2. Compare Website vs App
# Let's see if more time on the Website leads to more spending
sns.jointplot(x='Time on Website', y='Yearly Amount Spent', data=df)
plt.suptitle('Website Time vs Yearly Spend', y=1.02)
plt.show()

# Now let's see the App
sns.jointplot(x='Time on App', y='Yearly Amount Spent', data=df)
plt.suptitle('App Time vs Yearly Spend', y=1.02)
plt.show()

# 3. Explore all relationships at once
# This is the most powerful tool in EDA
sns.pairplot(df)
plt.show()

# 4. Correlation Heatmap
# This gives us the exact mathematical "strength" of relationships
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Customer Metrics')
plt.show()

# 5. Focus on the strongest relationship
sns.lmplot(x='Length of Membership', y='Yearly Amount Spent', data=df)
plt.title('Impact of Loyalty on Revenue')
plt.show()