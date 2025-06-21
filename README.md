#  Telecom Customer Churn Dashboard

![Streamlit](https://img.shields.io/badge/Streamlit-App-orange)
![Python](https://img.shields.io/badge/Python-3.9-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub Repo stars](https://img.shields.io/github/stars/MauryaGhogare/Telecom-Customer-Churn-Analysis?style=social)


An interactive Streamlit dashboard for analyzing customer churn behavior in a telecom company. This project provides data filtering, visual insights, and strategic recommendations to reduce customer churn.

---

##  Live Demo

 [Streamlit App](https://telecom-customer-churn-analysis-ixqnny5ubzhc7wslpkcbqp.streamlit.app/)
 
 Note: If the app shows “Not connected to a server”, simply refresh the page once. This is a common temporary issue with hosted Streamlit apps.

---

## 📂 Project Structure

📁 telecom-churn-dashboard/  
├── app.py  
├── Customer Churn.csv  
├── telecom_customer_churn_analysis.ipynb  
├── requirements.txt  
└── README.md  

---

## Features

-  Interactive sidebar filters (Gender, Contract Type, Internet Service, Senior Citizen, Payment Method, etc.)
-  Multiple visualizations:
  - Churn by Gender
  - Churn by Senior Citizen
  - Tenure Distribution
  - Contract Type
  - Services Used
  - Payment Method
  - Heatmap of Tenure vs Monthly Charges
-  Export Options:
  - Download filtered dataset as CSV
  - Download all plots as a single PDF
-  Insights & Recommendations to reduce churn

---

## Dataset Information

- Source: [Kaggle - Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn)
- Records: 7043 customers
- Features: Demographics, Account Info, Services, Billing, Churn Status

---

## Key Insights

- New customers (tenure < 6 months) with high monthly charges (> ₹90) have the highest churn rate.
- Senior Citizens churn more — better onboarding and simplified plans may help.
- Month-to-month contract users churn significantly more than long-term users.
- Customers with Tech Support, Security, or Backup services tend to stay longer.
- Users paying via Electronic Check have a higher churn rate — investigate friction.

---

## Recommendations

- Offer welcome discounts or calls for first 6 months.
- Promote upgrades to long-term contracts.
- Bundle support/security services in default plans.
- Design senior-friendly UI & support options.
- Investigate why Electronic Check users leave.

---

## How to Run the Project Locally

### 1. Clone the Repository
git clone https://github.com/your-username/telecom-churn-dashboard.git
cd telecom-churn-dashboard

### 2. Install Requirements
pip install -r requirements.txt

### 3. Run the Streamlit App
streamlit run app.py

---

## requirements.txt
streamlit
pandas
matplotlib
seaborn

---

## Author
**Maurya Ghogare**  
Email: [mauryaghogare10@gmail.com](mailto:mauryaghogare10@gmail.com)  
GitHub: [@MauryaGhogare](https://github.com/MauryaGhogare)  
LinkedIn: [mauryaghogare](https://www.linkedin.com/in/mauryaghogare)

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE).  
You are free to use, modify, and distribute this software with proper attribution.

---

## Show Your Support
If you liked this project, leave a ⭐ star on GitHub!
