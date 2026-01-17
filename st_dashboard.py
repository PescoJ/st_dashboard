# This code imports Pandas and Streamlit libraries to create a simple dashboard application.
import pandas as pd
import streamlit as st
import altair as alt
# Set the title and version of the dashboard
st.set_page_config(layout="wide")
st.title("Project Management Dashboard")
st.markdown("Version 0.0.11")
# Display a logo at the top of the dashboard
st.logo("logo.png", size="large")
# Function to load data from an Excel file with caching
@st.cache_data
def load_data(file):
    data = pd.read_excel(file)
    return data
# Format data for Line Chart on Step Tab 6
def load_progress_data(file):
    df = pd.read_excel(file, sheet_name="Progress Over Time")
    df.columns = df.columns.str.strip()
    if "Task Name" not in df.columns:
        st.error("The 'Progress Over Time' sheet must contain a 'Task Name' column.")
        return pd.DataFrame(columns=["Task Name", "Week", "Progress"])
    long_df = pd.melt(df,
                      id_vars=["Task Name"], 
                      var_name="Week", 
                      value_name="Progress"
                      )
    return long_df
# Create tabs for uploading data, viewing data, and displaying progress graphics
tab_1, tab_2, tab_3, tab_4, tab_5, tab_6 = st.tabs(["Upload Data", "End of Week 1", "End of Week 2", "End of Week 3", "End of Week 4", "Progress Graphics"])
# Tab 1 - Upload Data
with tab_1:
    st.header("Upload your Excel file")
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])
# Tab 2 - End of Week 1
with tab_2:
    st.header("End of Week 1")
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file, sheet_name="End of Week 1")
        st.success("File uploaded successfully!", icon = "✅")
        st.dataframe(df, use_container_width=True, column_config={
            "Start Date": st.column_config.DateColumn("Start Date"),
            "End Date": st.column_config.DateColumn("End Date"),
            "Progress": st.column_config.ProgressColumn("Progress", color="auto")})
    else:
        st.info("No data uploaded yet.", icon = "ℹ️")
# Tab 3 - End of Week 2
with tab_3:
    st.header("End of Week 2")
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file, sheet_name="End of Week 2")
        st.success("File uploaded successfully!", icon = "✅")
        st.dataframe(df, use_container_width=True, column_config={
            "Start Date": st.column_config.DateColumn("Start Date"),
            "End Date": st.column_config.DateColumn("End Date"),
            "Progress": st.column_config.ProgressColumn("Progress", color="auto")})
    else:
        st.info("No data uploaded yet.", icon = "ℹ️")
# Tab 4 - End of Week 3
with tab_4:
    st.header("End of Week 3")
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file, sheet_name="End of Week 3")
        st.success("File uploaded successfully!", icon = "✅")
        st.dataframe(df, use_container_width=True, column_config={
            "Start Date": st.column_config.DateColumn("Start Date"),
            "End Date": st.column_config.DateColumn("End Date"),
            "Progress": st.column_config.ProgressColumn("Progress", color="auto")})
    else:
        st.info("No data uploaded yet.", icon = "ℹ️")
# Tab 5 - End of Week 4
with tab_5:
    st.header("End of Week 4")
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file, sheet_name="End of Week 4")
        st.success("File uploaded successfully!", icon = "✅")
        st.dataframe(df, use_container_width=True, column_config={
            "Start Date": st.column_config.DateColumn("Start Date"),
            "End Date": st.column_config.DateColumn("End Date"),
            "Progress": st.column_config.ProgressColumn("Progress", color="auto")})
    else:
        st.info("No data uploaded yet.", icon = "ℹ️")
# Defining variables for Tab 6 - Progress Graphic

# Tab 6 - Progress Graphic
with tab_6:
    st.header("Progress Graphic")
    if uploaded_file is not None:
        progress_df = load_progress_data(uploaded_file)
        all_tasks = progress_df["Task Name"].unique()
        chosen_tasks = st.multiselect(
            "Select Tasks to Display", 
            options=all_tasks, 
            default=all_tasks[:15], 
            max_selections=15
            )
        filtered_df = progress_df[progress_df["Task Name"].isin(chosen_tasks)]
        chart = (
            alt.Chart(filtered_df)
            .mark_line(point=True)
            .encode(
                x = alt.X("Week:N", title = "Project Week"),
                y = alt.Y("Progress:Q", title = "Progress (%)", scale=alt.Scale(domain=[0, 1])),
                color = alt.Color("Task Name:N", title = "Task Name"),
                tooltip = ["Task Name:N", "Week:N", "Progress:Q"]     
            )
        )
        st.altair_chart(chart, use_container_width=True)
    else:
        st.info("No data uploaded yet.", icon = "ℹ️")
    
