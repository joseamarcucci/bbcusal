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
    st.markdown("<h3 style='text-align:  left; color: #008357;'>Campus BBLearn</h3>", unsafe_allow_html=True)
   
    #SHEET_ID = '12D4hfpuIkT7vM69buu-v-r-UYb8xx4wM1zi-34Fs9ck'
    #df = pd.read_csv('https://docs.google.com/spreadsheets/d/' + SHEET_ID + '/export?format=csv')
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/1yvDAVczwETC2JwcNeaYx2h2PD5fGCSWdJoY4QoMqR48/export?format=csv&gid=883950483')

    #df = pd.read_csv('/mydrive/MyDrive/multiapps/bbc204.csv')
    df=df.sort_values(by=['SessionOwner'])
    
    CHOICES = {456987: "PAD", 7896321: "FCEyE", 43: "MED", 453: "ELM", 45783: "ING", 8123: "LENGUAS", 48123: "FHGT", 457123: "JURI", 457823: "FCS", 4578128: "FLEO", 4578123: "HGT", 578128:"FCJ"}
    

    def format_func(option):
       return CHOICES[option] 
    
    buff, col, buff2 = st.beta_columns([1,3,1])

    option = buff.selectbox("Seleccionar Unidad", options=list(CHOICES.keys()), format_func=format_func)
    #st.write(f"Seleccionaste {format_func(option)}" )
    column = format_func(option)
    above_352 = df["SessionOwner"] == 'USAL_lti_production'
    sesionesu = df[above_352]['SessionName'].unique()
    df5=pd.value_counts(sesionesu)

    bool_series = df[above_352]["ContextIdentifier"].str.startswith(column, na = False)
    dupli=df[above_352][bool_series].drop_duplicates(subset = ['SessionName'])
    sesiones = df[above_352][bool_series]['SessionName'].unique()
    df6=pd.value_counts(sesiones)
    time = pd.DatetimeIndex(df[above_352][bool_series]['AttendeeTotalTimeInSession'])
    times1=time.hour * 60 + time.minute+ time.second/60
    times=times1.values.sum()
    timeu = pd.DatetimeIndex(df[above_352]['AttendeeTotalTimeInSession'])
    times1u=timeu.hour * 60 + timeu.minute+ timeu.second/60
    timesu=times1u.values.sum()
    times3=df6.index
    aulas=len(times3)
    times3t=df5.index
    aulast=len(times3t)
    df['RoomOpened'] = pd.to_datetime(df['RoomOpened']).dt.strftime('%d-%m-%y')
    minValue = df['RoomOpened'].min()
    maxValue = df['RoomOpened'].max()
    st.write('Período:',minValue,' al ',maxValue)
    st.write('Sesiones: ',aulas)
    st.sidebar.title('Consumos período')
    st.sidebar.write('Sesiones: ',aulast)
    st.sidebar.write('Minutos: ',round(timesu,1))
    st.write('Minutos usados: ',round(times,1))
    if st.checkbox('Mostrar Sesiones UA'):
       #page_size = 1000
       #page_number = st.number_input(
       #label="Página número (c/500):",
       #min_value=1,
       #max_value=ceil(len(df)/page_size),
       #step=1,
       #)
       #current_start = (page_number-1)*page_size
       #current_end = page_number*page_size
       #st.write(df[current_start:current_end]) 
       #st.write(df[above_352][['RoomOpened','SessionName','NameOfAttendee','AttendeeTotalTimeInSession']][current_start:current_end])
       #dupli.index = [""] * len(dupli)
       #st.table(dupli[['RoomClosed','SessionName']])
       #st.table(df[above_352][bool_series][['RoomOpened','NameOfAttendee','AttendeeTotalTimeInSession','ContextName']])
       df['Minutos Usados']=round(pd.to_timedelta(df[above_352]['AttendeeTotalTimeInSession']).dt.total_seconds()/60)
       totalesua=df[above_352][bool_series].groupby("SessionName")['Minutos Usados'].sum() 
       
    #dupli=dupli.sort_values(by=['RoomClosed'])

       st.table(totalesua)
    #st.markdown("### Sample Data")
    #df = create_table()
    #st.write(df)

    #st.write('Navigate to `Data Stats` page to visualize the data')
    if st.checkbox('Comparativo Salas x UA'):
       df['Minutos Usados']=round(pd.to_timedelta(df[above_352]['AttendeeTotalTimeInSession']).dt.total_seconds()/60)
       totalesuas=df[above_352].groupby("ua")['Minutos Usados'].sum() 
       st.bar_chart(totalesuas)
    if st.checkbox('Tabla Salas x UA'):
       df['Minutos Usados']=round(pd.to_timedelta(df[above_352]['AttendeeTotalTimeInSession']).dt.total_seconds()/60)
       totalesuas=df[above_352].groupby("ua")['Minutos Usados'].sum() 
       st.table(totalesuas)

