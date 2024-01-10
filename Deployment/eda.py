import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Welcome to Explaration Data Analysis')
#Memanggil data csv 
    df= pd.read_csv('P1G2_Kenneth Vincentius.csv')

#menampilakn 5 data teratas
    st.table(df.head(5))


#menampilakn barplot menampilkan persentase orang yang bisa membayar atau tidak
    st.title('Def Payment Percentage Presentation')
    count_data = df['default_payment_next_month'].value_counts()
    total_data = len(df)
    percentage_data = (count_data / total_data) * 100

    fig_1 = plt.figure()
    sns.barplot(x=percentage_data.index, y=percentage_data.values)
    plt.title('Def Payment Percentage Presentation')
    plt.xlabel('def_payment')
    plt.ylabel('Persentase (%)')
    for i in range(len(percentage_data)):
        plt.text(i, percentage_data[i], f'{percentage_data[i]:.2f}%', ha='center', va='bottom')
    st.pyplot(fig_1)

#menampilkan penjelasan plot def payment presentasi
    with st.expander('Explanation'):
        st.caption('Results: We can see that 78.58% can pay and 21.42% cannot pay')

#Menampilkan barplot menampilkan persentase defaulting payment berdasarkan jenis kelamin
    st.title("Percentage of Gender")
    fig_2 = plt.figure(figsize=(6, 6))
    def_payment_gender = sns.countplot(data=df, x='sex', hue='default_payment_next_month')
    for container in def_payment_gender.containers:
            def_payment_gender.bar_label(container)
    st.pyplot(fig_2)

#menapilkan penjelesan distribusi gender
    with st.expander('Explanation'):
        st.caption('It can be seen that the majority of users are women. It can be said that the users are housewives and career women compared to men who are fewer in number.')

 # Membuat plot histogram dari distribusi usia
    st.title('Distribution of Age')
    fig_3=plt.figure(figsize=(8, 6))
    sns.histplot(data=df, x='age', bins=30, kde=True)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    st.pyplot(fig_3)
    # fig3, axes = plt.subplots(1, 2, figsize=(12, 5))


#menampilkan detail dari plot distribution age
    with st.expander('Explanation'):
        st.caption('Results: It can be seen that the age distribution is from 20 to 50')
        st.caption('Insight : To increase the number of users who can pay, its a good idea to bill on payday around 25-31 during payday because on that date they have a lot of money so they can pay')

#Menampilkan Education lever Distribusi
    df['education_level'] = df['education_level'].apply(lambda x: 4 if x in [0, 5, 6] else x)

    fig_4=plt.figure(figsize=(8, 6))
    st.subheader('Education Level Distribution')
    sns.countplot(x='education_level', data=df)
    plt.xlabel('Education Level')
    plt.ylabel('Amount')
    st.pyplot(fig_4)

#menampilkan detail dari plot distribusi education
    with st.expander("Explanation"):
        st.caption('Notes: 1 Graduate, 2 University, 3 High School, 4 Others . Results: It can be seen from this that the majority of users are graduates and universities')
        st.caption('Insight: Maybe in the future a threshold can be selected or given for users who can use this facility because users with high school level education, others may not have income or their income is small so it will be more likely for them to fail to pay. When we set a threshold for users with a large or fixed income, we can reduce the percentage of defaults.')
