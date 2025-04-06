import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Page Configuration
st.set_page_config(
    page_title="🧬 Patient Cluster Explorer", 
    layout="wide", 
    page_icon="📊"
)

# Title and Description
st.title("🧬 Patient Cluster Explorer")
st.markdown("Explore patient clusters and readmission drivers with interactive charts and explainable AI insights.")

# Instructions Expander
with st.expander("📖 How to Use This Dashboard", expanded=True):
    st.markdown(
        """
        - **Filters (Sidebar)**: Refine the patient cohort by age, race, gender, cluster group, and readmission status.
        - **Feature Selection**: Choose numeric features (e.g., time in hospital, lab procedures, medications, comorbidities) to visualize correlations and scatter matrices.
        - **Cluster Distribution**: Bar chart showing patient counts per cluster.
        - **Readmission Distribution**: Bar chart of readmission status counts.
        - **Correlation Heatmap**: Interactive heatmap of selected features to spot strong associations.
        - **Scatter Matrix**: Pairwise scatter plots colored by readmission status to explore feature interactions.
        - **Interpret Results**: Use these insights to understand which factors drive readmissions and tailor interventions accordingly.
        """
    )

# Load Dataset
@st.cache_data
def load_data():
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, "clustered_data.csv")
    if not os.path.exists(data_path):
        st.error(f"Data file not found at {data_path}")
        return pd.DataFrame()
    df = pd.read_csv(data_path)
    cluster_labels = {
        0: "High Risk",
        1: "Low Engagement",
        2: "Moderate Utilization",
        -1: "Noise"
    }
    df["cluster_name"] = df["cluster_label"].map(cluster_labels)
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("🧪 Filter Patients")
age_groups = df["age_group"].unique().tolist() if "age_group" in df.columns else []
races = df["race_label"].unique().tolist() if "race_label" in df.columns else []
genders = df["gender_label"].unique().tolist() if "gender_label" in df.columns else []
clusters = df["cluster_name"].dropna().unique().tolist() if "cluster_name" in df.columns else []
readmission_labels = df["readmitted_label"].unique().tolist() if "readmitted_label" in df.columns else []

selected_ages = st.sidebar.multiselect("🎂 Age Group", options=age_groups, default=age_groups)
selected_races = st.sidebar.multiselect("🌍 Race", options=races, default=races)
selected_genders = st.sidebar.multiselect("⚧ Gender", options=genders, default=genders)
selected_clusters = st.sidebar.multiselect("🔗 Cluster", options=clusters, default=clusters)
selected_readmit = st.sidebar.multiselect("🔄 Readmission Status", options=readmission_labels, default=readmission_labels)

# Feature Selection for Analysis
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
default_features = ['time_in_hospital', 'num_lab_procedures', 'num_medications', 'comorbidity_count', 'severity_score']
selected_features = st.sidebar.multiselect(
    "🔎 Select Features for Analysis", 
    options=numeric_cols, 
    default=[f for f in default_features if f in numeric_cols]
)

# Filter Data
filtered_df = df[
    (df["age_group"].isin(selected_ages)) &
    (df["race_label"].isin(selected_races)) &
    (df["gender_label"].isin(selected_genders)) &
    (df["cluster_name"].isin(selected_clusters)) &
    (df["readmitted_label"].isin(selected_readmit))
]

# Layout: Charts & Metrics
col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("🔢 Cluster Distribution")
    if not filtered_df.empty:
        cluster_counts = filtered_df["cluster_name"].value_counts().reset_index()
        cluster_counts.columns = ["Cluster", "Count"]
        fig = px.bar(
            cluster_counts, x="Cluster", y="Count", color="Cluster",
            title="Number of Patients per Cluster", template="plotly_white"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data matches the selected filters.")

with col2:
    st.subheader("📋 Key Stats")
    st.metric("Total Patients", len(filtered_df))
    st.metric(
        "Avg. Time in Hospital", 
        round(filtered_df["time_in_hospital"].mean(), 2) if not filtered_df.empty else 0
    )

# Readmission Distribution
st.subheader("🔄 Readmission Status Distribution")
if not filtered_df.empty and "readmitted_label" in filtered_df.columns:
    readmit_counts = filtered_df["readmitted_label"].value_counts().reset_index()
    readmit_counts.columns = ["Readmission Status", "Count"]
    fig4 = px.bar(
        readmit_counts, x="Readmission Status", y="Count", color="Readmission Status",
        title="Readmission Distribution", template="plotly_white"
    )
    st.plotly_chart(fig4, use_container_width=True)
else:
    st.warning("No data matches the selected filters.")

# Correlation Heatmap
if selected_features and len(selected_features) > 1:
    st.subheader("🧪 Feature Correlation Heatmap")
    corr = filtered_df[selected_features].corr()
    fig5 = px.imshow(
        corr, text_auto=True, aspect="auto", color_continuous_scale="RdBu_r",
        title="Correlation Matrix"
    )
    st.plotly_chart(fig5, use_container_width=True)

# Scatter Matrix
if selected_features and len(selected_features) > 1:
    st.subheader("📊 Scatter Matrix of Selected Features")
    fig6 = px.scatter_matrix(
        filtered_df, dimensions=selected_features, color="readmitted_label",
        title="Scatter Matrix", template="plotly_white"
    )
    fig6.update_layout(height=800)
    st.plotly_chart(fig6, use_container_width=True)
