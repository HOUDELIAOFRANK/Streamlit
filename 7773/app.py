import numpy as np
from metaflow import Flow,Step,get_metadata, metadata,DataArtifact,Task,cards
from metaflow import Run
from metaflow import Metaflow
import streamlit as st
import plotly.express as px

# FLOW_NAME = 'RandomForestflow'
FLOW_NAME = 'SampleClassificationFlow'

def get_path(sub_path):
    s = str(latest_run)
    s = s[5:-2]
    s += sub_path
    return s
def get_latest_successful_run(flow_name: str):
    "Gets the latest successfull run."
    for r in Flow(flow_name).runs():
        if r.successful: 
            return r

latest_run = get_latest_successful_run(FLOW_NAME)
# st.title('Random Forest Model of Loan Status')
st.title('SampleClassificationFlow')

st.dataframe(Step(get_path( '/load_data')).task.data.df)

Male = Step(get_path( '/gender')).task.data.Male
Female = Step(get_path('/gender')).task.data.Female
Married = Step(get_path('/married')).task.data.Married
Unmarried = Step(get_path('/married')).task.data.Unmarried
Urban = Step(get_path('/urban')).task.data.Urban
Semiurban = Step(get_path('/urban')).task.data.Semiurban
Rural = Step(get_path('/urban')).task.data.Rural
gender_card = Step(get_path( '/gender')).task.card
married_card = Step(get_path('/married')).task.card
urban_card = Step(get_path('/urban')).task.card
group_selection = st.sidebar.selectbox(
    label='Select the Feature',
    options=['Gender', 'Marriage', 'Urban'])
if group_selection == 'Gender':
    st.sidebar.subheader('Group selection')
    x_values = st.sidebar.selectbox('Female or Male', options=['Male', 'Female'])
    if x_values == 'Male':
        st.write('The Miss Rate of Male group is {}.'.format(Male))
    if x_values == 'Female':
        st.write('The Miss Rate of Female group is {}.'.format(Female))
if group_selection == 'Marriage':
    st.sidebar.subheader('Group selection')
    x_values = st.sidebar.selectbox('Female or Male', options=['Married', 'Unmarried'])
    if x_values == 'Married':
        st.write('The Miss Rate of Married group is {}.'.format(Married))
    if x_values == 'Unmarried':
        st.write('The Miss Rate of Unmarried group is {}.'.format(Unmarried))
if group_selection == 'Urban':
    st.sidebar.subheader('Group selection')
    x_values = st.sidebar.selectbox('Female or Male', options=['Urban', 'Semiurban', 'Rural'])
    if x_values == 'Urban':
        st.write('The Miss Rate of Urban group is {}.'.format(Urban))
    if x_values == 'Semiurban':
        st.write('The Miss Rate of Semiurban group is {}.'.format(Semiurban))
    if x_values == 'Rural':
        st.write('The Miss Rate of Rural group is {}.'.format(Rural))