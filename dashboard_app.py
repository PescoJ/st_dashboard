# This code imports Pandas and Streamlit libraries to create a simple dashboard application.
from turtle import color
import pandas as pd
import streamlit as st
# Set the title and version of the dashboard
st.set_page_config(layout="wide")
st.title("Project Management Dashboard")
st.markdown("Version 0.0.5")
# Display a logo at the top of the dashboard
st.logo("logo.png", size="large")
# Function to load data from an Excel file with caching
@st.cache_data
def load_data(file):
    data = pd.read_excel(file)
    return data
# Create tabs for uploading data, viewing data, and displaying progress graphics
tab_1, tab_2, tab_3 = st.tabs(["Upload Data", "View Data", "Progress Graphics"])
with tab_1:
    st.header("Upload your Excel file")
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])
with tab_2:
    st.header("View Uploaded Data")
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        st.success("File uploaded successfully!", icon = "✅")
        st.dataframe(df, use_container_width=True, column_config={
            "Start Date": st.column_config.DateColumn("Start Date"),
            "End Date": st.column_config.DateColumn("End Date"),
            "Progress": st.column_config.ProgressColumn("Progress", color="auto")})
    else:
        st.info("No data uploaded yet.", icon = "ℹ️")
with tab_3:
    st.header("Progress Graphics")
    if uploaded_file is not None:
        st.bar_chart(data=df.set_index("Task Name")["Progress"])
    else:
        st.info("No data uploaded yet.", icon = "ℹ️")
    
