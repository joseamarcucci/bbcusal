import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
from data.create_data import create_table
from math import ceil
def app():
    
    st.markdown("<style>body {color: #fff;background-color: #111;}</style>",unsafe_allow_html=True,)
    st.markdown("<span style=“background-color:#121922”>",unsafe_allow_html=True)
    st.markdown(
    """<style>
        .css-19ih76x{text-align: left !important}
    </style>
    """, unsafe_allow_html=True) 
    st.markdown("<h3 style='text-align:  left; color: #008357;'>Usuarios Campus BBLearn</h3>", unsafe_allow_html=True)
   
    #SHEET_ID = '12D4hfpuIkT7vM69buu-v-r-UYb8xx4wM1zi-34Fs9ck'
    #df = pd.read_csv('https://docs.google.com/spreadsheets/d/' + SHEET_ID + '/export?format=csv')
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/1cZcUgS5AhhueUc3PXUcR6jWJgVmhzwQcp0E7RIYNuDU/export?format=csv&gid=1173523213')

    #df = pd.read_csv('/mydrive/MyDrive/multiapps/bbc204.csv')
    options = ['#VALUE!'] 
    # selecting rows based on condition 
    df = df.loc[~df['ua'].isin(options)] 
    sesionesu = df['STUDENT'].unique()
    df5=pd.value_counts(sesionesu)
    
    times3tt=df5.index
    aulastt=len(times3tt) 
    roles = df['STUDENT'].unique()
    
    
    #df['LAST_COURSE_ACCESS'] = pd.to_datetime(df['LAST_COURSE_ACCESS']).dt.strftime('%d-%m-%y')
    minValue = df['LAST_COURSE_ACCESS'].min()
    maxValue = df['LAST_COURSE_ACCESS'].max()
    st.write('Período:',minValue,' al ',maxValue)

    st.write('Usuarios totales: ',aulastt)
    dupli=df.drop_duplicates(subset = ['STUDENT'])   
    totalesxua=dupli.groupby("ua")['STUDENT'].count()
    totalesxuarolg=dupli.groupby( 'ROL')['STUDENT'].count()
    totalesxuarol=dupli.groupby( ['ua', 'ROL'])['STUDENT'].count()


    if (st.checkbox("Mostrar Tabla usuarios x UA y Rol", key='chk_Unique_item')):
        st.table(totalesxuarol)
        st.table(totalesxua)
    else:
        st.bar_chart(totalesxua)
        st.bar_chart(totalesxuarolg) 
    
       #dupli=cursos.drop_duplicates(subset = ['COURSE'])
       #st.table(dupli[['COURSE','COURSE_NUMBER','STUDENT']])



 
         

   
   


    