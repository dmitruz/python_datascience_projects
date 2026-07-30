import os
import sys
import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import ttest_ind, chisquare


script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else os.getcwd()

df_path = os.path.join(script_dir, "game_ab_testing_dataset.csv")


if not os.path.exists(df_path):
    print("[ERROR] Could not find the CSV files in the script folder!")
    sys.exit()

df_path = r"D:\Github\datascience\dataAnalyst\python_projects\ab_test_user_retention\game_ab_testing_dataset.csv"

df_path = pd.read_csv(df_path)

# --------------------------------------------------------------------------

# 1 рівномірний розподіл користувачів на 2 групи

# 0   date                 500 non-null    object 
#  1   variant              500 non-null    object 
#  2   downloads            500 non-null    int64  
#  3   retention_day7       500 non-null    float64
#  4   retention_day30      500 non-null    float64
#  5   completed_level3     500 non-null    int64  
#  6   completed_level10    500 non-null    int64  
#  7   avg_session_minutes  500 non-null    float64
#  8   purchase_rate        500 non-null    float64
#  9   revenue_usd          500 non-null    float64


average_d7_retention = np.mean(df_path['retention_day7']) #0.35

average_d30_retention = np.mean(df_path['retention_day30']) # 0.23

print(average_d7_retention)
print(average_d30_retention)

# метрики по групам

variant_retention7 = df_path.groupby('variant')['retention_day7'].mean() # 0.35, 0.35
variant_retention30 = df_path.groupby('variant')['retention_day30'].mean() # 0.23, 0.23
variant_revenue = df_path.groupby('variant')['revenue_usd'].mean() # 26, 26

print(variant_retention7)  # 0.35, 0.35
print(variant_retention30) # 0.23, 0.23
print(variant_revenue) # 26, 26

# Hypotes Новий онбординг покращить Day 7 Retention на 5% відносно контрольної групи.


check_values = df_path['variant'].value_counts(normalize=True)

print(check_values)  # 534   and 466

# calculate uplift

retention = df_path.groupby('variant')['retention_day7'].mean()

a = retention['A']  # 0.51
b = retention['B']  # 0.48

uplift = (b - a) / a * 100

print(f"Uplift = {uplift:.2f}%") # 2.96%

# check statistical significance.  Use Z-test for proportions

# count amount of succesful users

success_a = (df_path[df_path['variant'] == 'A']['retention_day7'] > 0.35).sum()
print(success_a)  # 122
success_b = (df_path[df_path['variant'] == 'B']['retention_day7'] > 0.35).sum()
print(success_b) # 119

n_a = len(df_path[df_path['variant'] == 'A'])
print(n_a)  # 258

n_b = len(df_path[df_path['variant'] == 'B'])
print(n_b) # 242

# test
count = np.array([success_a, success_b])
nobs = np.array([n_a, n_b])
stat, pvalue = proportions_ztest(count, nobs)

print(pvalue) #0.52
if pvalue < 0.05:
    print("Statistically significant")
else:
    print("Not statistically significant") # not statisticaly significant
