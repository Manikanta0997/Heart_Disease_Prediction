import streamlit as st
import pickle
import pandas as pd
import sklearn
import numpy as np

pipe = pickle.load(open('HeartDisease_Prediction_using_KNN10.pkl','rb'))
ExerciseAngina1 = ['N','Y']
ST_Slope1 = ['Up', 'Flat', 'Down']
Sex1 = ['M', 'F']
ChestPainType1 = ['ATA', 'NAP', 'ASY', 'TA']
RestingECG1 = ['Normal', 'ST', 'LVH']
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title('HeartDisease Predictor')


col1, col2 = st.columns(2)

with col1:
	Age = st.number_input('Age')
with col2:
  	Sex = st.selectbox('Select Gender',sorted(Sex1))
col3, col4 = st.columns(2)
with col3:
	ChestPainType = st.selectbox('ChestPainType',sorted(ChestPainType1))
with col4:
	RestingBP = st.number_input('RestingBP(80-180)')
	
col5, col6 = st.columns(2)
with col5:
	FastingBS = st.number_input('FastingBS(0 or 1)')
with col6:
	RestingECG = st.selectbox('RestingECG',sorted(RestingECG1))
col7, col8, col9= st.columns(3)
with col7: 
	ExerciseAngina = st.selectbox('ExerciseAngina',sorted(ExerciseAngina1))
with col8:
	Oldpeak = st.number_input('Oldpeak(-5 - 10')
#col9 = st.columns(1)
with col9:
	ST_Slope = st.selectbox('ST_Slope',sorted(ST_Slope1))
    

if st.button('Predict Score'):
    input_df = pd.DataFrame(
     {'Age':[Age],'Sex':[Sex],'ChestPainType':[ChestPainType],'RestingBP':[RestingBP],'FastingBS':[FastingBS],'RestingECG':[RestingECG],'ExerciseAngina':[ExerciseAngina],'Oldpeak':[Oldpeak],'ST_Slope':[ST_Slope]})
    result = pipe.predict(input_df)
    #st.header("Predicted  - " + str(int(result[0])))
    if int(result[0]) == 0:
    	result = "Safe"
    else:
    	result = "Danger"
    st.header("Predicted  - " + result)

st.header("Note: It is only for educational purose")
st.write("MANIKANTA")
