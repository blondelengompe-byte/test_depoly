import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import time 

df = pd.read_csv('bank.csv')
st.set_page_config(page_title="Dashboard", page_icon='✅', layout="wide")
#Dashboard
st.title('Real time data analystics dashboard')


job_filter = st.selectbox('Select a job', pd.unique(df['job']))
df_job = df[df['job'] == job_filter]

#creation d'indicateurs

avg_age = np.mean(df['age'])
count_married = int(df[df['marital'] == 'married']['marital'].count())
balance = np.mean(df['balance'])

kpi1,kpi2,kpi3 = st.columns(3)
kpi1.metric(label='Age', value = round(avg_age), delta = round(avg_age ))
kpi2.metric(label='Married count', value = count_married ,delta = count_married)
kpi3.metric(label='Balance $',value=f"{round(balance, 2)}",delta=-round(balance / count_married) * 100)






#Graphiques

col1,col2 = st.columns(2)
with col1:
    st.markdown("### First Chart")
    fig1 = plt.figure()
    sns.barplot(data=df , y ='age' , x= 'marital', palette = 'muted')
    st.pyplot(fig1)
with col2:
    st.markdown("### Second Chart")
    fig2 = plt.figure()
    sns.barplot(data=df , y ='age' , x= 'job', palette = 'muted')
    st.pyplot(fig2)

st.markdown("### Detailed Data View")
st.dataframe(df)
