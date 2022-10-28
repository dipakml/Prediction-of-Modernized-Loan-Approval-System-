## End-to-End Machine Learning Project- Loan Eligibility Prediction using Machine Learning

<img target="_blank" src="https://github.com/dipakml/Prediction-of-Modernized-Loan-Approval-System-/blob/master/PL-Eligibility-Calc.png" width=600>

### Table of Content
  * [Overview](#overview)
  * [Dataset Information](#dataset)
  * [Motivation](#motivation)
  * [Demo](#demo)
  * [Steps in the project execution](#Learning-Objective)
  * [Technical Aspect](#technical-aspect)
  * [Technologies Used](#technologies-used)
  * [Installation](#installation)
  * [Note](#note)



### Overview 
A Bank’s profit and loss depend on the amount of the loans that is whether the client or customer is paying back the loan. Recovery of loans is the most tedious task for the banking sector. 

Dream Housing Finance company deals in all kinds of home loans. They have a presence across all urban, semi-urban and rural areas. The customer first applies for a home loan and after that, the company validates the customer eligibility for the loan.

The company wants to automate the loan eligibility process (real-time) based on customer detail provided while filling out online application forms. These details are Gender, Marital Status, Education, number of Dependents, Income, Loan Amount, Credit History, and others.

To automate this process, they have provided a dataset to identify the customer segments that are eligible for loan amounts so that they can specifically target these customers.

 The historical data of candidates was used to build a machine learning model using different classification algorithms. The main objective of this project is to predict whether a new applicant granted the loan or not using machine learning models trained on the historical data set.


In this project, let's apply machine learning techniques and develop a web based application to predict the loan eligibility of new applicant.


### Dataset Information
Variable	          Description

Loan_ID	            Unique Loan ID

Gender	            Male/ Female

Married	            Applicant married (Y/N)

Dependents	        Number of dependents

Education	         Applicant Education (Graduate/ Under Graduate)

Self_Employed	      Self employed (Y/N)

ApplicantIncome	    Applicant income

CoapplicantIncome	  Coapplicant income

LoanAmount	Loan    amount in thousands

Loan_Amount_Term	  Term of loan in months

Credit_History	    credit history meets guidelines

Property_Area	      Urban/ Semi Urban/ Rural

Loan_Status	        Loan approved (Y/N)


Final dataset: 615 observations

Dataset used in this project can be found here : [Dataset] https://www.kaggle.com/datasets/ninzaami/loan-predication


### Motivation
The motivation was to use machine learning experiments to try to automate the loan eligibility process with low risk & better recovery.

Idea is to implement the end to end machine learning project while using free deployment platform like Heroku.



### Demo
[Visit this link for Web application](https://loanwebapp7.herokuapp.com/)

Web application Snapshot:

<img target="_blank" src="https://github.com/dipakml/Prediction-of-Modernized-Loan-Approval-System-/blob/master/webapp_snapshot.png" width=800>



### Steps in the project execution

- Data gathering 
- Descriptive Analysis 
- Data Visualizations 
- Data Preprocessing 
- Data Modelling 
- Model Evaluation 
- Model Deployment 

### Technical Aspect 

- Training a machine learning model using scikit-learn. 
- Building and hosting a streamlit web app on Heroku. 
- A user has to input key features.
- Once it gets all the fields information , the prediction is displayed. 


### Technologies Used  
![](https://forthebadge.com/images/badges/made-with-python.svg) 

<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/streamlit.png" width=160>
<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/heroku.png" width=160>
<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/numpy.png" width=160>
<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/pandas.jpeg" width=160>

### Installation 
- Clone this repository and unzip it.
- After downloading, cd into the working directory.
- Begin a new virtual environment with Python 3 and activate it.
- Install the required packages using pip install -r requirements.txt
- Execute the command: streamlit run app.py


### Note:
- Webapp can handle concurrency upto some extent but can be scaled.

