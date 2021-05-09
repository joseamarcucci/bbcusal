import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from data.create_data import create_table
from math import ceil
def app():
    
    #st.markdown('<img style="float: left;" src="https://virtual.usal.edu.ar/branding/themes/Usal_7Julio_2017/images/60usalpad.png" />', unsafe_allow_html=True)
    st.markdown("<style>body {color: #fff;background-color: #111;}</style>",unsafe_allow_html=True,)
    st.markdown("<span style=“background-color:#121922”>",unsafe_allow_html=True)
    st.markdown(
    """<style>
        .css-19ih76x{text-align: left !important}
    </style>
    """, unsafe_allow_html=True) 
    st.markdown("<h3 style='text-align:  left; color: #008357;'>Campus Moodle</h3>", unsafe_allow_html=True)
    df = pd.read_csv('/mydrive/MyDrive/multiapps/abril.csv')
    #SHEET_ID = '12D4hfpuIkT7vM69buu-v-r-UYb8xx4wM1zi-34Fs9ck'
    #df = pd.read_csv('https://docs.google.com/spreadsheets/d/' + SHEET_ID + '/export?format=csv')
    #df = pd.read_csv('https://docs.google.com/spreadsheets/d/1kNaXpaA0OiKZyWBfeBwm9SW6O9YfpSh6DcDQaFZGkSg/export?format=csv')

    #CHOICES = {456987: "PAD", 7896321: "FCEyE", 4578123: "MED"}


    #def format_func(option):
       #return CHOICES[option]


    #option = st.selectbox("Seleccionar Unidad", options=list(CHOICES.keys()), format_func=format_func)
    #st.write(f"Seleccionaste {format_func(option)}" )
    #column = format_func(option)
    above_352 = df["SessionOwner"] == 'USAL_rest_production'
    df5=pd.value_counts(df[above_352]['SessionName'])

    #bool_series = df[above_352]["ContextIdentifier"].str.startswith(column, na = False)
    dupli=df[above_352].drop_duplicates(subset = ['SessionName'])
    sesiones = df[above_352]['SessionName'].unique()
    df6=pd.value_counts(sesiones)
    time = pd.DatetimeIndex(df[above_352]['AttendeeTotalTimeInSession'])
    times1=time.hour * 60 + time.minute+ time.second/60
    times=times1.values.sum()
    times3=df6.index
    aulas=len(times3)
    df['RoomOpened'] = pd.to_datetime(df['RoomOpened']).dt.strftime('%d-%m-%y')
    maxValue = df['RoomOpened'].max()
    minValue = df['RoomOpened'].min()
    st.write('Período:',minValue,' al ',maxValue)
    st.write('Sesiones/Aulas: ',aulas)
    st.write('Minutos usados: ',round(times,1))

    st.sidebar.title('Consumos semanales')
    
    st.sidebar.write('Se ven las distintas materias')
    st.sidebar.write('No se pueden mostrar por UA')
    #if st.checkbox('Mostrar Aulas'):
    #st.table(df[above_352][['RoomOpened','SessionName','NameOfAttendee','AttendeeTotalTimeInSession']])
    dupli.index = [""] * len(dupli)

    dupli['Minutos Usados']=round(pd.to_timedelta(dupli['AttendeeTotalTimeInSession']).dt.total_seconds()/60)
    totalesua=dupli.groupby("SessionName")['Minutos Usados'].sum() 
    #st.markdown("### Sample Data")
    #df = create_table()
    #st.write(df)
    st.table(totalesua)
    #st.write('Navigate to `Data Stats` page to visualize the data')


