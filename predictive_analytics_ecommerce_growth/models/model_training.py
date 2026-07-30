import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# 1. Load data
# df = pd.read_csv('ecommerce_customers_cleaned.csv')
path = './data/processed/ecommerce_customers_cleaned.csv'
df = pd.read_csv(path)

# 2. Define Features (X) and Target (y)
# We want to predict 'Yearly Amount Spent' based on the numerical behavior metrics
X = df[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y = df['Yearly Amount Spent']

# 3. Split the data
# 70% of data used for training, 30% for testing the accuracy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# 4. Train the Model
lm = LinearRegression()
lm.fit(X_train, y_train)

# 5. Make Predictions
predictions = lm.predict(X_test)

# 6. Evaluate Accuracy
print('MAE (Mean Absolute Error):', metrics.mean_absolute_error(y_test, predictions))
print('RMSE (Root Mean Squared Error):', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
print('R-squared Score:', metrics.r2_score(y_test, predictions))

# 7. Model Interpretation: Coefficients
coeff_df = pd.DataFrame(lm.coef_, X.columns, columns=['Coefficient'])
print("\n--- Model Coefficients ---")
print(coeff_df)