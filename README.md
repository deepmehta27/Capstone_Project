# Optimizing Hospital Readmission Reduction Using Patient Clustering

**Author:** Deep Manish Mehta  
**Date:** April 29, 2025  
**Course:** Capstone Project – MS in Data Science, Pace University

---

## Project Overview

Hospital readmissions pose significant challenges by driving up healthcare costs and reducing patient satisfaction. Traditional predictive models often lack explainability regarding the underlying causes of readmissions. This project introduces an innovative unsupervised learning framework that not only identifies hidden, high-risk patient subgroups but also explains the key factors driving these outcomes. The ultimate goal is to inform targeted interventions that can reduce readmission rates.

---

## Project Goal

- **Develop an unsupervised learning framework** to cluster patients based on healthcare utilization and clinical severity.
- **Transform clustering results** into actionable insights using explainable AI techniques.
- **Support strategic decision-making** for reducing hospital readmissions through targeted interventions.

---

## Objectives
1. **Perform Exploratory Data Analysis (EDA)**  
   - Clean and preprocess the Diabetes 130-US Hospitals dataset.  
   - Engineer features capturing medication adherence, lab result volatility, and follow-up compliance.

2. **Cluster Patients Using HDBSCAN**  
   - Identify dense regions of similar patients without needing a predefined number of clusters.  
   - Validate cluster quality using silhouette scores and domain expertise.

3. **Explain Risk Drivers with SHAP**  
   - Quantify the contribution of each feature (e.g., missed appointments) to higher readmission rates.  
   - Provide interpretable insights for clinicians and decision-makers.

4. **Build an Interactive Dashboard**  
   - Enable data exploration and cluster analysis.  
   - Allow clinicians to visually investigate patient subgroups and potential interventions.

---

## Dataset
- **Name:** Diabetes 130-US Hospitals  
- **Source:** [UCI Machine Learning Repository]([https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008]  
- **Description:** Contains over 100,000 hospital admissions for patients with diabetes from 130 hospitals in the U.S. from 1999–2008.  
- **Preprocessing Steps:**  
  1. Remove or impute missing values where possible.  
  2. Engineer new features (e.g., medication adherence proxies, follow-up frequency).  
  3. Handle potential class imbalance.

---
## Methodology

1. **Data Cleaning & Preprocessing**
   - Replace missing values and remove duplicates.
   - Drop irrelevant or redundant columns.
   - Encode categorical variables and engineer additional features such as total visits, outpatient ratio, and severity score.

2. **Exploratory Data Analysis (EDA)**
   - Visualize data distributions and relationships (e.g., readmission status, age groups, race, gender).
   - Create correlation matrices to understand feature interactions.

3. **Clustering with HDBSCAN**
   - Scale features and perform PCA for dimensionality reduction.
   - Apply HDBSCAN to identify patient subgroups, handling noise points appropriately.

4. **Interpretation with SHAP**
   - Convert unsupervised clusters into binary targets.
   - Train Random Forest classifiers in a one-vs-rest framework.
   - Use SHAP analysis to determine key features driving each patient subgroup.

5. **Model Evaluation**
   - Validate clusters with cross-validation scores, train/test accuracies, and silhouette scores.
   - Generate detailed profiles for each cluster (Low Engagement, Moderate Utilization, High Risk).

---

## Quick Start

To begin, ensure all required libraries are installed:

```python
!pip install pandas numpy matplotlib seaborn scikit-learn hdbscan shap
```

Then, load and preprocess the data as described. For full details, refer to the subsequent cells in this notebook.

---
