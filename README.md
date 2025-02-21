# Optimizing Hospital Readmission Reduction Using Patient Clustering

An unsupervised learning approach to identify high-risk patient subgroups, reduce hospital readmissions, and provide actionable insights for healthcare professionals.

---

## Project Overview
Hospital readmissions are a major concern for healthcare providers, leading to financial burdens and reduced patient satisfaction. Traditional predictive models often focus on whether a readmission will occur, without explaining **why** it happens. This project uses **HDBSCAN** clustering and **explainable AI (SHAP)** to discover and interpret **hidden patient subgroups** at high risk of readmission. By exploring these subgroups, hospitals can implement targeted interventions that address the core causes of readmissions.

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
- **Source:** [UCI Machine Learning Repository]([https://archive.ics.uci.edu/ml/datasets/Diabetes+130-US+hospital+discharge+data+Se]  
- **Description:** Contains over 100,000 hospital admissions for patients with diabetes from 130 hospitals in the U.S. from 1999–2008.  
- **Preprocessing Steps:**  
  1. Remove or impute missing values where possible.  
  2. Engineer new features (e.g., medication adherence proxies, follow-up frequency).  
  3. Handle potential class imbalance.  

> **Note**: Make sure you have permission and follow data-use guidelines when using or sharing this dataset.

---

## Methodology
1. **Data Preprocessing**  
   - Feature engineering (e.g., _“lab result volatility”_ to capture the stability of lab values)  
   - Handling missing data and outliers  

2. **Clustering with HDBSCAN**  
   - Identify variable-density clusters  
   - Determine hyperparameters (e.g., `min_cluster_size`) based on silhouette scores and domain knowledge  

3. **Explainability with SHAP**  
   - Gain insight into each cluster’s risk factors  
   - Highlight major drivers of readmissions (e.g., medication non-adherence)  

4. **Dashboard Development**  
   - Implement an interactive dashboard using **Plotly** and **Dash**  
   - Visualize clusters, SHAP values, and subgroup-level insights  

---

## Results & Dashboard
- After clustering, patients will be segmented into meaningful groups.  
- **SHAP analysis** will detail which features are driving higher readmission probabilities.  
- In the **dashboard**, clinicians and stakeholders can:  
  - Select clusters of interest  
  - View top risk features  
  - Compare potential interventions  

---

## License
This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this software, as long as the original license is included.

---

## Contact
- **Author:** Deep Manish Mehta  
- **GitHub:** [@deepmehta27](https://github.com/deepmehta27)  
