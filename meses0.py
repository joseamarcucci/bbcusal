import streamlit as st
import pandas as pd
import numpy as np


import matplotlib.pyplot as plt

from data.create_data import create_table
from math import ceil
def app():
    #st.markdown('<img style="float: left;" src="https://virtual.usal.edu.ar/branding/themes/Usal_7Julio_2017/images/60usalpad.png" />', unsafe_allow_html=True)
    st.markdown('<style>div[data-baseweb="select"] > div {text-transform: capitalize;}body{background-color:#008357;}</style>', unsafe_allow_html=True)
    st.markdown(
    """<style>
        .css-19ih76x{text-align: left !important}
    </style>
    """, unsafe_allow_html=True) 
   
    st.markdown("<h3 style='text-align: left; color: #008357;'>Usuarios mensuales Collaborate</h3>", unsafe_allow_html=True)
   
    #SHEET_ID = '12D4hfpuIkT7vM69buu-v-r-UYb8xx4wM1zi-34Fs9ck'
    dfeb = pd.read_csv('https://docs.google.com/spreadsheets/d/1yvDAVczwETC2JwcNeaYx2h2PD5fGCSWdJoY4QoMqR48/export?format=csv&gid=883950483')
    dfmar = pd.read_csv('https://docs.google.com/spreadsheets/d/1kNaXpaA0OiKZyWBfeBwm9SW6O9YfpSh6DcDQaFZGkSg/export?format=csv')
    buff, col, buff2 = st.beta_columns([1,3,1])
    dfabr= pd.read_csv('https://docs.google.com/spreadsheets/d/1yvDAVczwETC2JwcNeaYx2h2PD5fGCSWdJoY4QoMqR48/export?format=csv&gid=1411220795')
    dfmay = pd.read_csv('https://docs.google.com/spreadsheets/d/1_iz1sWXVezBgjWe_BhDxdc00U7Pg8BFwVwVqCgjivsU/export?format=csv')

    #st.write(maxValue2,maxValue3,maxValue4,maxValue5)
    dfeb['AttendeeFirstJoinTime'] = pd.to_datetime(dfeb['AttendeeFirstJoinTime']).dt.strftime('%y-%m-%d')
    usuarios2=dfeb.sort_values(by=['AttendeeFirstJoinTime'])
    #usuarios=usuarios.groupby("AttendeeFirstJoinTime", as_index=False)['NameOfAttendee'].count()
    usuarios2=usuarios2.groupby("AttendeeFirstJoinTime", as_index=False)['NameOfAttendee'].nunique()
    #st.table(usuarios[['NameOfAttendee','AttendeeFirstJoinTime']])
    df2=(usuarios2['NameOfAttendee']).max()
    st.write('Total Usuarios Febrero: ',df2)
    dfmar['AttendeeFirstJoinTime'] = pd.to_datetime(dfmar['AttendeeFirstJoinTime']).dt.strftime('%y-%m-%d')
    usuarios3=dfmar.sort_values(by=['AttendeeFirstJoinTime'])
    #usuarios=usuarios.groupby("AttendeeFirstJoinTime", as_index=False)['NameOfAttendee'].count()
    usuarios3=usuarios3.groupby("AttendeeFirstJoinTime", as_index=False)['NameOfAttendee'].nunique()
    #st.table(usuarios[['NameOfAttendee','AttendeeFirstJoinTime']])
    df3=(usuarios3['NameOfAttendee']).max()
    st.write('Total Usuarios Marzo: ',df3)
    dfabr['AttendeeFirstJoinTime'] = pd.to_datetime(dfabr['AttendeeFirstJoinTime']).dt.strftime('%y-%m-%d')
    usuarios4=dfabr.sort_values(by=['AttendeeFirstJoinTime'])
    #usuarios=usuarios.groupby("AttendeeFirstJoinTime", as_index=False)['NameOfAttendee'].count()
    usuarios4=usuarios4.groupby("AttendeeFirstJoinTime", as_index=False)['NameOfAttendee'].nunique()
    #st.table(usuarios[['NameOfAttendee','AttendeeFirstJoinTime']])
    df4=(usuarios4['NameOfAttendee']).max()
    st.write('Total Usuarios Abril: ',df4)
    dfmay['AttendeeFirstJoinTime'] = pd.to_datetime(dfmay['AttendeeFirstJoinTime']).dt.strftime('%y-%m-%d')
    usuarios5=dfmay.sort_values(by=['AttendeeFirstJoinTime'])
    #usuarios=usuarios.groupby("AttendeeFirstJoinTime", as_index=False)['NameOfAttendee'].count()
    usuarios5=usuarios5.groupby("AttendeeFirstJoinTime", as_index=False)['NameOfAttendee'].nunique()
    #st.table(usuarios[['NameOfAttendee','AttendeeFirstJoinTime']])
    df5=(usuarios5['NameOfAttendee']).max()
    st.write('Total Usuarios Mayo 9/5: ',df5)
    df = pd.DataFrame({

    'Mes': ['Febrero','Marzo', 'Abril', 'Mayo'],
    'Usuarios': [df2, df3, df4, df5]
    })
    #st.line_chart(df.rename(columns={'Mes':'index'}).set_index('index'))
    import altair as alt




    grafico=alt.Chart(df).mark_line().encode(x=alt.X('Mes', sort=None),y='Usuarios',).properties(width=800, height=600)
    st.altair_chart(grafico)
