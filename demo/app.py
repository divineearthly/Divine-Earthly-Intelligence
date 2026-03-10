
import streamlit as st
import sys
import os

# Setup paths for imports
sys.path.append(os.getcwd())

from modules.orchestrator import DomainOrchestrator
from agents.multi_agent import MultiAgentSystem

st.set_page_config(page_title='Divine Earthly Intelligence Dashboard', layout='wide')

st.title('🌍 Divine Earthly Intelligence Dashboard')
st.markdown('### Hybrid Intelligence Engine for Agriculture, Climate, and Disaster Prediction')

# Initialize Orchestrator and MAS
orch = DomainOrchestrator()
mas = MultiAgentSystem()

# Sidebar for Domain Selection
st.sidebar.header('Settings')
domain = st.sidebar.selectbox(
    'Select Analysis Domain',
    ['Agriculture', 'Climate Risk', 'Disaster Prediction']
)

st.header(f'{domain} Analysis')

# Domain-specific inputs
with st.form(key='analysis_form'):
    col1, col2 = st.columns(2)
    
    if domain == 'Agriculture':
        with col1:
            temp = st.number_input('Temperature (°C)', value=25.0)
            hum = st.number_input('Humidity (%)', value=50.0)
        with col2:
            soil = st.number_input('Soil Moisture (%)', value=30.0)
        
        submit = st.form_submit_button('Run Agriculture Analysis')
        if submit:
            result = orch.route_request('agriculture', soil_moisture=soil, temperature=temp, humidity=hum)
            
    elif domain == 'Climate Risk':
        with col1:
            carbon = st.number_input('Carbon Levels (PPM)', value=410.0)
            sea = st.number_input('Sea Level Rise (mm)', value=3.2)
        with col2:
            avg_t = st.number_input('Avg Global Temp Increase (°C)', value=1.1)
            
        submit = st.form_submit_button('Run Climate Analysis')
        if submit:
            result = orch.route_request('climate', carbon_levels=carbon, sea_level_rise=sea, avg_temp=avg_t)
            
    else: # Disaster Prediction
        with col1:
            sensor_val = st.number_input('Sensor Magnitude', value=0.5)
            s_type = st.selectbox('Sensor Type', ['flood', 'seismic', 'wildfire'])
        with col2:
            d_temp = st.number_input('Local Temperature (°C)', value=30.0)
            d_hum = st.number_input('Local Humidity (%)', value=40.0)
            
        submit = st.form_submit_button('Run Disaster Prediction')
        if submit:
            result = orch.route_request('disaster', sensor_type=s_type, value=sensor_val, temperature=d_temp, humidity=d_hum)

# Display Results
if 'result' in locals():
    st.subheader('Analysis Result')
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.metric(label='Risk Level', value=result['prediction'])
    with res_col2:
        st.info(f'Methodology Used: {result["method"].capitalize()}')

# Multi-Agent Workflow Visualization
st.divider()
st.header('🤖 Multi-Agent Reasoning Workflow')
user_query = st.text_input('Ask the Agents a specific question:', 'How can we mitigate crop loss in 2024?')

if st.button('Execute Agent Workflow'):
    with st.spinner('Agents are collaborating...'):
        # In a real app, we would capture stdout or modify MAS to return steps
        # For this demo, we simulate the logic visible in the logs
        final_out = mas.run_workflow(user_query)
        
        st.success('Workflow Complete!')
        st.json({
            'Query': user_query,
            'Final Agent Optimization': final_out
        })
