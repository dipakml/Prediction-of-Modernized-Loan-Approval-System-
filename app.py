# -*- coding: utf-8 -*-
"""
Created on #####

@author: DA
"""

# -*- coding: utf-8 -*-
"""

@Created by: DA
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)  

pickle_sc = open("sc.pkl","rb")
sc=pickle.load(pickle_sc)  

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2017/08/02/14/26/winter-landscape-2571788__480.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

def predict(Gender, Married, Education, Self_Employed, ApplicantIncome,
       CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
       Dependents_0, Dependents_1, Dependents_2,
       Property_Area_Semiurban, Property_Area_Urban):
   
    prediction=classifier.predict([[Gender, Married, Education, Self_Employed, ApplicantIncome,
       CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
       Dependents_0, Dependents_1, Dependents_2,
       Property_Area_Semiurban, Property_Area_Urban]])
    print(prediction)
    return prediction



def main():
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h3 style="color:white;text-align:center;">Loan Eligibility Prediction using Machine Learning </h3>
    </div>
    """
   
    st.markdown(html_temp,unsafe_allow_html=True)


    st.markdown('**This is a web application built using Machine Learning for prediction of customers loan eligibilty.  Enter the basic information mentioned below, this web application will predict the loan eligibility.**')
    Gender = st.sidebar.selectbox("Gender",("Male","Female"))
    if Gender == 'Male':
        Gender = 1
    else:
        Gender = 0

    Married = st.sidebar.selectbox("Married",("Yes","No"))
    if Married == 'Yes':
        Married = 1
    else:
        Married = 0

    Dependents = st.sidebar.selectbox("Dependents",("0","1","2", "3"))
    if Dependents == '0':
        Dependents_0 = 1
        Dependents_1 = 0
        Dependents_2 = 0
    elif Dependents == '1':
        Dependents_0 = 0
        Dependents_1 = 1
        Dependents_2 = 0
    elif Dependents == '2':
        Dependents_0 = 0
        Dependents_1 = 0
        Dependents_2 = 1
    else:
        Dependents_0 = 0
        Dependents_1 = 0
        Dependents_2 = 0

    Education = st.sidebar.selectbox("Education",("Graduate","Not Graduate"))
    if Education == 'Graduate':
        Education = 1
    else:
        Education = 0       

    Self_Employed = st.sidebar.selectbox("Self Employed",("Yes","No"))
    if Self_Employed == 'Yes':
        Self_Employed = 1
    else:
        Self_Employed = 0 



    ApplicantIncome = st.number_input("Enter Applicant Income between 150 to 80,000")

    CoapplicantIncome = st.number_input("Enter Co-Applicant Income between 0 to 40,000")

    LoanAmount = st.number_input("Enter Loan Amount between 0 to 700")

    Loan_Amount_Term = st.number_input("Enter Loan Amount Term between 12 to 480")

    Credit_History = st.number_input("Enter Credit History either 0 or 1")

    Property_Area = st.sidebar.selectbox("Property Area",("Urban","Rural","Semi Urban"))
    if Property_Area == 'Urban':
        Property_Area_Urban = 1
        Property_Area_Semiurban = 0
    elif Property_Area == 'Semi Urban':
        Property_Area_Urban = 0
        Property_Area_Semiurban = 1
    else:
        Property_Area_Urban = 0
        Property_Area_Semiurban = 1         


    
    result=""
    if st.button("Predict"):
        result=classifier.predict(sc.transform([[Gender, Married, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Dependents_0, Dependents_1, Dependents_2, Property_Area_Semiurban, Property_Area_Urban]]))
        if result ==1:
            return st.header('You are Eligibile for availing the Loan')
        else:
            return st.header('Sorry, you are not eligible to avail the Loan')
if __name__=='__main__':
    main()
    
    
    