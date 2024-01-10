import streamlit as st
import eda
import model

page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    st.write('Name      : Kenneth Vincentius')
    st.write('Create a model to predict whether a user will or will not pay for the next month based on historical user payment data in previous months')
    st.write('')
    st.caption('Please select another menu in the Select Box on the left of your screen to get started!')
    st.write('')
    st.write('')
    with st.expander("Background "):
        st.caption('I am a data scientist at PT. ABC, and I have been assigned a project to manage a dataset related to user payment credit scores. My task is to select the appropriate model to use on this dataset and provide predictions regarding whether users will be able to pay for the next month or not, based on their historical data.')

    with st.expander("Problem Statement"):
            st.caption('The objective of this project is to predict users ability to make payments in order to reduce the number of users who are unable to pay by 10% within a 3-month timeframe, thereby minimizing losses for PT. ABC')

elif page == 'Exploration Data Analysis':
    eda.run()
else:
    model.run()

