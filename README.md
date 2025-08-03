# Finance-Mobile-Money-Fraud-Detection

# 📊 Mobile Money Fraud Detection in Rwanda

A capstone data science project to detect suspicious mobile money transactions in Rwanda using machine learning and anomaly detection techniques.

---
🙋‍♂️ **Student and ID: Mugisha Leopold - 26636**



📊 Dataset: Synthetic Mobile Money Transaction Dataset

---

## 📁 Project Structure and steps

## ✅ Project Steps

✅ Step 1: Project Folder Setup

fraud-detection/

├── data/                                 # Raw dataset

├── outputs/                              # Cleaned data, graphs, model results

├── src/                                  # All Python scripts

---

✅ Step 2: Data Cleaning (src/clean_data.py)

- Removed missing values

- Fixed timestamps

- Dropped rows with incomplete balances

- ✅ Output: outputs/cleaned_data.csv

---
✅ Step 3: Exploratory Data Analysis (src/eda.py)

Generated key insights:

- 📊 Transaction Amount Distribution

- 📊 Fraud vs Legit Count

- 📈 Step vs Amount over time

- 📦 Boxplot by fraud

- 🔥 Correlation Heatmap

- ✅ Saved to: outputs/

---
✅ Step 4: Anomaly Detection (src/anomaly_detection.py)

 Algorithm:

- Isolation Forest

- Detected outliers in key numeric columns

- Added a new column anomaly (1 = suspicious)

✅ Saved to:

- anomaly_data.csv

- anomaly_plot.png (scatter)

- anomaly_distribution.png (bar)

---
✅ Step 5: Model Evaluation (src/evaluate_model.py)

- Compared isFraud (actual) vs anomaly (predicted)

- Classification metrics:

- Precision

- Recall

- F1-score

- Confusion matrix

---
✅ Step 6: Power BI Dashboard

- Created interactive visuals:

- Fraud vs Legit count (bar)

- Suspicious transactions over time (line)

- Fraud percentage (card or donut)

- Imported scatterplots from Python

✅ File: powerbi_dashboard.pbix

---

✅ Step 7: Reporting

📝 report.docx: 

  - Includes project summary
  - visualizations, evaluation
  - conclusion

🎞 presentation.pptx: Ready-to-present slide deck

---
**⚙️ How It Works**

**1. Data Preparation**

- The CSV dataset contains transaction logs with fields like amount, sender/recipient balances, and fraud labels.

**2. Cleaning & Formatting**

- We clean missing values, fix datatypes (e.g., timestamps), and remove noisy rows.

**3. Exploratory Analysis (EDA)**

- We use seaborn and matplotlib to understand how transaction patterns behave, both for legit and fraudulent activity.

**4. Anomaly Detection with Isolation Forest**

- We train a model to detect outliers based on transaction features — without using fraud labels. These outliers are tagged as suspicious.

**5. Model Evaluation**

- The detected anomalies are compared against true frauds using F1-score and other metrics to measure how accurate the model is.

**7. Power BI Dashboards**

- Cleaned and enriched data is visualized in Power BI to generate real-time insights into fraud patterns and trends.

---

## 🧠 Problem Statement

**Can machine learning detect suspicious mobile money transactions in Rwanda?**

This project uses synthetic transaction data to explore fraud detection using Isolation Forest, EDA, and Power BI.

---

## 📊 Dataset

- **Source**:
  - [Mendeley Data](https://data.mendeley.com/datasets/zhj366m53p/2?utm_source)
    
- 📊 Dataset: Synthetic Mobile Money Transaction Dataset
- **Format**: CSV
- **Size**: 1.7 million rows, 10 columns

---

## 🧪 Tools & Techniques

- **Python** – pandas, seaborn, matplotlib, sklearn
- **Anomaly Detection** – Isolation Forest
- **Power BI** – for interactive dashboards
- **Data Format** – Structured CSV
- **VS Code**
- **Mendeley Data**
- **Git & GitHub**
---

## 📊 Visuals

- Distribution of Transaction Amounts
- Fraud vs Non-Fraud Transactions
- Correlation Heatmap
- Anomalies Scatter Plot
- Power BI Dashboard: Pie chart, column chart, filters

---
## 📁 ScreenShoot

<img width="1000" height="400" alt="step_vs_amount" src="https://github.com/user-attachments/assets/ada8e186-e7ea-4f65-8c07-31b9f2689b71" />
<img width="800" height="400" alt="amount_distribution" src="https://github.com/user-attachments/assets/92c8dca0-a9f5-413d-ba02-de3b33f7c0c7" />
<img width="600" height="400" alt="anomaly_distribution" src="https://github.com/user-attachments/assets/095ab633-0039-42f3-aa21-d4218acc2b12" />
<img width="1000" height="500" alt="anomaly_plot" src="https://github.com/user-attachments/assets/f711656f-314c-4050-89ed-a66e3e0b55a0" />
<img width="800" height="500" alt="boxplot_amount_fraud" src="https://github.com/user-attachments/assets/8e72d2eb-35eb-43fe-b56b-8377d5860116" />
<img width="500" height="400" alt="confusion_matrix" src="https://github.com/user-attachments/assets/cc8c8a85-c88e-45e6-b18e-3891cc01b767" />
<img width="1000" height="600" alt="correlation_heatmap" src="https://github.com/user-attachments/assets/66d1eb92-75a2-4555-8b27-701959ef403a" />
<img width="600" height="400" alt="fraud_count" src="https://github.com/user-attachments/assets/c67ed5ec-fd98-4e97-9443-01a14ae9c3b9" />


---
### 📁 Download Project Files from Google Drive

- To access large files that are not hosted directly on GitHub (e.g. cleaned data, synthetic_mobile_money_transaction_dataset, anomaly_data,suspicious_transactions, PowerPoint, Word report):

- https://drive.google.com/drive/folders/1Zz_H8KSwZ7szYjaz3uFgA74tGdE8iTyL?usp=sharing

Python
