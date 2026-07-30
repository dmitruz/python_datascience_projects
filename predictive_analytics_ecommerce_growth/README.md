# Predictive Analytics for Ecommerce Growth

## Project Overview
This project analyzes customer behavior data for an ecommerce company to determine whether development efforts should focus on their **Mobile App** or **Website**. Using Python, the project follows a complete Data Science pipeline: Data Cleaning, Exploratory Data Analysis (EDA), KPI calculation, and Machine Learning modeling.

---

## 1. Exploratory Data Analysis (EDA)
The goal of the EDA phase was to identify visual patterns and correlations between user engagement and revenue.

### Key Visualizations:
* **Jointplots:** We compared `Time on App` and `Time on Website` against `Yearly Amount Spent`.
    * *Observation:* The App shows a clear linear trend with spending, while the Website shows a flat, scattered distribution.
* **Pairplot:** A grid of all numerical features revealed that `Length of Membership` has the most significant visual relationship with total expenditure.
* **Correlation Heatmap:** Mathematically confirmed that `Length of Membership` (0.81) and `Time on App` (0.50) are the primary drivers of revenue.

---
<img width="1000" height="600" alt="corelation" src="https://github.com/user-attachments/assets/13a3640d-0635-4614-8d95-43498f55e5c1" />

<img width="500" height="500" alt="impackt_loyalty" src="https://github.com/user-attachments/assets/0e8654e5-04b2-442a-a1b2-1e76b47f167b" />

<img width="600" height="600" alt="time_on_app" src="https://github.com/user-attachments/assets/db9c1fea-8790-4f79-b055-8affa5830a35" />






## 2. Business KPI Analysis
Before modeling, we established baseline metrics to understand the "average" customer profile:

| Metric | Value | Business Context |
| :--- | :--- | :--- |
| **Average Revenue Per User (ARPU)** | **$499.31** | Total average yearly spend |
| **Avg Time on App** | **12.05 min** | Engagement on Mobile |
| **Avg Time on Website** | **37.06 min** | Engagement on Desktop |
| **Avg Membership Length** | **3.53 years** | Average customer age in system |

**Key Insight:** Even though customers spend nearly **3x more time** on the website, the mobile app is far more efficient at converting time into revenue.

---

## 3. Machine Learning Analysis
We implemented a **Linear Regression** model to predict yearly spending. The model achieved high precision, allowing us to quantify the exact value of each minute a user spends on the platform.

### Model Performance:
* **R-squared Score:** **0.989** (The model explains 98.9% of spending variance).
* **Mean Absolute Error (MAE):** **$7.22** (Predictions are accurate within a $7 margin).

### Feature Coefficients (The "Impact" Table):
The coefficients represent the dollar increase in yearly spend for every 1-unit increase in the metric:

* **Length of Membership:** **+$61.28**
* **Time on App:** **+$38.59**
* **Avg. Session Length:** **+$25.98**
* **Time on Website:** **+$0.19**

---
<img width="1000" height="600" alt="business_impact_ML" src="https://github.com/user-attachments/assets/14dbf706-244d-4ed3-b2fd-2a6438863c2d" />

<img width="800" height="600" alt="model_accuracy_ML" src="https://github.com/user-attachments/assets/7890b43c-72f3-4321-8b46-b03dc14d2e10" />

<img width="800" height="500" alt="residual_destribution_ML" src="https://github.com/user-attachments/assets/b7f9b25c-37b9-4ec4-90a7-4a11bed6ad4b" />




## Final Conclusions & Recommendations

### Technical Conclusion
The model is highly successful. The residual analysis shows a normal distribution, confirming that the Linear Regression assumptions are met and the results are statistically significant. 

### Business Recommendations
1.  **Prioritize the Mobile App:** The "Time on App" is roughly **200 times more valuable** than "Time on Website" in terms of revenue correlation ($38.59 vs $0.19).
2.  **Focus on Retention (Loyalty):** Every extra year a customer stays a member adds ~$61 to the bottom line. Marketing should prioritize loyalty programs over broad web traffic ads.
3.  **Website Strategy:** The website is currently a "passive" touchpoint. It should either be accepted as a browsing-only tool or redesigned to match the conversion efficiency of the app.

---

## How to Run This Project
1. Clone the repository.
2. Install dependencies:  
   `pip install -r requirements.txt`
3. Run the analysis:  
   `python src/final_model_report.py`
