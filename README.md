# Credit-Card-Default-Machine-Learning

## Table of Contents
- Introduction
- Problem Statement
- Data Source
- Libraries Used
- Data Analysis
- Modeling
- Conclusion

## Introduction
Create a model to predict whether a user will or will not pay for the next month based on historical user payment data in previous months


## Problem Statement
The objective of this project is to predict users' ability to make payments in order to reduce the number of users who are unable to pay by 10% within a 3-month timeframe, thereby minimizing losses for PT. ABC.

## Data Source
https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=ml_datasets&t=credit_card_default&page=table&project=sonorous-study-394708&ws=!1m5!1m4!4m3!1sbigquery-public-data!2sml_datasets!3scredit_card_default

## Libraries Used
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Scikit-learn
- Streamlit

## Data Analysis
The notebook is expected to employ various machine learning techniques, including:
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Feature Engineering

## Modeling
- Model Definition:
SVM, KNN, Logistic Regression
- Cross Validation:: for looking best model between 5 model that have been define before
- Hyperparameter Tuning:
SVM model with weights,n,n_neighbors
F1 score: 47%
- Model Evaluation:
Compare baselineHyper(default) KNN model 47 % and Hyperparameter Tuning SVM model 45%

## Data Inference
Make sampling data to test model that has been created

## Hugging Face
Make application for deploy model that has been created
[Hugging Face](https://huggingface.co/spaces/kennethv1706/Dataset_Credit_Score)


## Conclusion
- I chose f1 score as the score parameter because I think minimizing false positives and false negatives is important.

- From the STD results which are close to 0 and below the mean, it means that the KNN model has a default STD value of 0.03 so the model is the best fit. So it can be said that the default knn model has good consistency, but the validation of the prediction results is not good because it is only around 48%. From a business perspective, this model cannot be used because the prediction results are still less than 50% good, so it can lead to wrong prediction results which can cause the company to suffer losses. In the future, it is possible to increase feature selection, increase parameter selection to improve model performance and even try new models so that you can choose more of the best models.

- To increase the number of users who can pay, it's a good idea to bill on payday around 25-31 during payday because on that date they have a lot of money so they can pay

- The majority of users come from graduate and university backgrounds. Maybe in the future a threshold can be selected or given for users who can use this facility because users with high school level education, others, and unknowns may not have income or their income is small so it is more likely that they will fail to pay. When we set a threshold for users with a large or fixed income, we can reduce the percentage of defaults

- The KNN model cannot be used to solve problem statements because the F1 score accuracy rate is only 46% so it cannot be used to reduce the level of non-payment on default payments.