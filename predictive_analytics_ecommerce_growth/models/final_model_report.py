import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# 1. Load data
path = './data/processed/commerce_customers_cleaned.csv'
df = pd.read_csv(path)

# 2. Define Features (X) and Target (y)
X = df[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y = df['Yearly Amount Spent']

# 3. Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# 4. Train the Model
lm = LinearRegression()
lm.fit(X_train, y_train)

# 5. Make Predictions
predictions = lm.predict(X_test)

# --- VISUALIZATION SECTION ---

# Set the style
sns.set_palette("GnBu_d")
sns.set_style('whitegrid')

# Visual 1: Feature Importance (Coefficients)
coeff_df = pd.DataFrame(lm.coef_, X.columns, columns=['Coefficient']).sort_values(by='Coefficient', ascending=False)

plt.figure(figsize=(10, 6))
# Note: Added 'hue' to avoid warnings in newer Seaborn versions
sns.barplot(x='Coefficient', y=coeff_df.index, data=coeff_df, palette='viridis', hue=coeff_df.index, legend=False)
plt.title('Business Impact: Dollars gained per 1-unit increase')
plt.xlabel('Increase in Yearly Spend ($)')
plt.ylabel('User Metric')
plt.show()

# Visual 2: Predicted vs Actual (Testing the Model)
plt.figure(figsize=(8, 6))
plt.scatter(y_test, predictions)
plt.xlabel('Y Test (Actual Values)')
plt.ylabel('Predicted Y')
plt.title('Model Accuracy: Predicted vs Actual')
plt.show()

# Visual 3: Residuals (Error Distribution)
plt.figure(figsize=(8, 5))
sns.histplot((y_test - predictions), bins=50, kde=True)
plt.title('Residuals Distribution (Error Margin)')
plt.xlabel('Error Amount ($)')
plt.show()

# Print Final Summary
print("\n--- Final Model Performance ---")
print(f"R-squared Score: {metrics.r2_score(y_test, predictions):.4f}")
print(f"MAE: ${metrics.mean_absolute_error(y_test, predictions):.2f}")
print("\nCoefficients:")
print(coeff_df)