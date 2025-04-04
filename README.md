# Optimizing Hospital Readmission Reduction Using Patient Clustering

**Author:** Deep Manish Mehta  
**Date:** April 29, 2025  
**Course:** Capstone Project – MS in Data Science, Pace University  

---

## 🧠 Project Overview

Hospital readmissions pose significant challenges by increasing healthcare costs and reducing patient satisfaction. Traditional predictive models often fail to explain why patients are readmitted. This project introduces an **unsupervised learning framework** that not only identifies **hidden, high-risk patient subgroups**, but also explains the **key risk drivers** behind those clusters using **explainable AI (SHAP)**.

---

## 🎯 Project Goal

- **Cluster patients** based on health service utilization and clinical features.
- **Explain** cluster-level patterns that correlate with readmission risks.
- **Enable intervention planning** through a clinician-friendly interactive dashboard.

---

## ✅ Objectives

1. **Perform Exploratory Data Analysis (EDA)**  
   Understand distributions, demographics, and readmission patterns.

2. **Feature Engineering & Clustering**  
   Use HDBSCAN to group similar patients based on engineered features.

3. **Cluster Interpretation with SHAP**  
   Apply explainable AI to derive risk factors within each cluster.

4. **Interactive Dashboard**  
   Enable stakeholders to explore clusters, metrics, and patient profiles.

---

## 📊 Dataset

- **Name:** Diabetes 130-US Hospitals
- **Source:** [UCI Repository](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008)
- **Description:** It contains 100,000+ hospital records for diabetic patients from 130 U.S. hospitals (1999–2008).
- **Preprocessing Steps:**
  - Dropped high-missing-value columns (e.g., weight).
  - Encoded categorical variables (`age`, `race`, etc.).
  - Engineered features: number of medications, inpatient visits, outpatient ratio, etc.

---

## 🚀 How to Run the Project

### 📦 1. Install Dependencies

Install all required packages in a virtual environment:

```bash
pip install -r requirements.txt
```

> If you face NumPy 2.x issues, run:
> ```bash
> pip install numpy==1.26.4
> ```

---

### 🧪 2. Run the Notebook (for analysis & modeling)

Open and run the notebook:

```bash
jupyter notebook DeepMehta_Capstone_Project.ipynb
```

This notebook includes:
- Data cleaning
- Feature engineering
- Clustering with HDBSCAN
- SHAP interpretation
- Data export to `clustered_data.csv`

---

### 📊 3. Launch the Dashboard

After generating `clustered_data.csv`, run the dashboard:

```bash
streamlit run dashboard_app.py
```

This will launch a **local web app** where:
- You can explore each patient cluster.
- Understand key risk features (from SHAP).
- Filter patients by risk level, medication count, and more.

---

## 📈 Methods Used

| Step                     | Technique / Tool             |
|--------------------------|------------------------------|
| EDA                      | Seaborn, Matplotlib, Pandas  |
| Clustering               | HDBSCAN                      |
| Feature Scaling          | StandardScaler               |
| Explainability           | SHAP (TreeExplainer)         |
| Dashboard                | Streamlit                    |

---

## 📚 Literature Support

Refer to `Literature_Review.pdf` for key academic papers and supporting research related to:
- Readmission reduction strategies
- Unsupervised patient profiling
- Clinical explainability with machine learning

---

## ✅ Final Notes

- Clustering is **unsupervised**, so SHAP was applied using a **Random Forest (One-vs-Rest)** on cluster labels.
- The SHAP visualizations and scores are used both in analysis and dashboard (`shap_values.pkl`).

---

## 👤 Author

**Deep Manish Mehta**  
Data Science Capstone | Pace University | April 2025

---
