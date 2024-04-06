import streamlit as st
import pickle
import pandas as pd
import sklearn
import numpy as np

import streamlit as st
import pickle
import pandas as pd
import sklearn
import numpy as np

st.set_page_config(
    page_title="XAI Project",
    page_icon="👋",
)
st.title("Heart Disease Prediction Integrating With XAI 21BAI1734_21BAI1488_21BAI1730")
st.sidebar.success("Select a page above.")

st.write('Cardiovascular diseases (CVDs) are the number 1 cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worldwide. Four out of 5CVD deaths are due to heart attacks and strokes, and one-third of these deaths occur prematurely in people under 70 years of age. Heart failure is a common event caused by CVDs and this dataset contains 11 features that can be used to predict a possible heart disease.')

st.write('People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help.')
