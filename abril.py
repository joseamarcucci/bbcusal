import streamlit as st
import pandas as pd
import numpy as np
from data.create_data import create_table
from math import ceil
def app():
    #st.markdown('<img style="float: left;" src="https://virtual.usal.edu.ar/branding/themes/Usal_7Julio_2017/images/60usalpad.png" />', unsafe_allow_html=True)
    st.markdown('<style>div[data-baseweb="select"] > div {text-transform: capitalize;}body{background-color:#008357;}</style>', unsafe_allow_html=True)
    st.markdown(
    """<style>
        .css-19ih76x{text-align: left !important}

        .css-d56p6e{text-align: left !important}
    </style>
    """, unsafe_allow_html=True) 
    
    st.markdown("<h3 style='text-align:  left; color: #008357;'>Salas Collaborate</h3>", unsafe_allow_html=True)
   
    #SHEET_ID = '12D4hfpuIkT7vM69buu-v-r-UYb8xx4wM1zi-34Fs9ck'
    #df = pd.read_csv('https://docs.google.com/spreadsheets/d/1kNaXpaA0OiKZyWBfeBwm9SW6O9YfpSh6DcDQaFZGkSg/export?format=csv&gid=1983291520')
    buff, col, buff2 = st.beta_columns([1,3,1])
    df = pd.read_csv('abril.csv')
    df=df.sort_values(by=['SessionOwner'])
    #options = ['USAL_lti_production', 'USAL_rest_production','josemarcucci']
    df8 = pd.DataFrame({
    'Mes': ['Febrero','Marzo', 'Abril'],
    'Minutos': [2078664, 12619085, 15271367]
    })
    #df8=df8.sort_values(by=['Minutos'])
    df8.index = [""] * len(df8)

    
    buff.table(df8) 
    options = ['ALEJANDRA.LAMBERTI','josemarcucci'] 
    # selecting rows based on condition 
    df = df.loc[~df['SessionOwner'].isin(options)] 
    countries = df['SessionOwner'].unique()
    duplit=df.drop_duplicates(subset = ['SessionName'])
    df5=pd.value_counts(duplit['SessionName'])
    df['Minutos']=round(pd.to_timedelta(df['AttendeeTotalTimeInSession']).dt.total_seconds()/60)
    totales=df.groupby("SessionOwner")['Minutos'].sum()
    #st.table(totales)
    #st.table(duplit[['SessionOwner','SessionName']])

    
    '## Tipo de plataforma'
    #if st.checkbox('Ver comparativo UAs'):
       #st.bar_chart(totales)
    '## Tipo de plataforma'
    country = buff.selectbox('Usuario BBC o plataforma', countries)
  
    df[df['SessionOwner'] == country]
    
    

    #option = st.selectbox("Seleccionar Unidad", options=list(CHOICES.keys()), format_func=format_func)
    #st.write(f"Seleccionaste {format_func(option)}" )
    #column = format_func(option)
    above_352 = df["SessionOwner"] == country
    #moderador = df["AttendeeRole"] == "Moderator" 
    
    bool_series = df[above_352]["SessionOwner"].str.startswith(country, na = False)
    dupli=df[above_352][bool_series].drop_duplicates(subset = ['SessionName'])
    #dupli=df[above_352][bool_series].drop_duplicates(['SessionName']).groupby('SessionName').agg({'AttendeeTotalTimeInSession':'sum'})
    sesiones = df[above_352][bool_series]['SessionName'].unique()
    df6=pd.value_counts(sesiones)
    time = pd.DatetimeIndex(df[above_352][bool_series]['AttendeeTotalTimeInSession'])
    times1=time.hour * 60 + time.minute+ time.second/60
    times=times1.values.sum()
    timeu = pd.DatetimeIndex(df['AttendeeTotalTimeInSession'])
    times1u=timeu.hour * 60 + timeu.minute+ timeu.second/60
    timesu=times1u.values.sum()

    times3t=df5.index
    aulast=len(times3t) 
    times3=df6.index
    aulas=len(times3)
    df['RoomOpened'] = pd.to_datetime(df['RoomOpened']).dt.strftime('%d-%m-%y')
    maxValue = df['RoomOpened'].max()
    minValue = df['RoomOpened'].min()
    st.write('Período:',minValue,' al ',maxValue)
    st.write('Salas: ',aulas)
    st.write('Minutos usados: ',round(times,1))
    #st.sidebar.markdown("<h3 style='text-align: left; color: black;font-weight:500;'>Minutos y salas del mes</h3>", unsafe_allow_html=True)
    st.sidebar.write('Minutos/mes: ',round(timesu,1))
    st.sidebar.write('Salas/mes: ',aulast)
    
    #st.sidebar.markdown("<h3 style='text-align: left; color: black;font-weight:500;'>Minutos totales</h3>", unsafe_allow_html=True)
    st.sidebar.write('Minutos/totales: ',14697740+round(timesu,1))
    #st.sidebar.write('Salas: ',aulast)
    
    dupli.index = [""] * len(dupli)
    #dupli.columns=['RoomClosed', 'SessionName']
    #dupli.rename(columns={'RoomClosed':'Fecha','SessioName':'Sala'})
    if st.checkbox('Mostrar Salas de la UA'):
       #st.table(df[above_352][bool_series][['RoomOpened','SessionName','NameOfAttendee','AttendeeTotalTimeInSession']])
       df['Minutos Usados']=round(pd.to_timedelta(df[above_352][bool_series]['AttendeeTotalTimeInSession']).dt.total_seconds()/60)
       totalesua=df[above_352][bool_series].groupby("SessionName")['Minutos Usados'].sum()
    #dupli=dupli.sort_values(by=['RoomClosed'])
      
       st.table(totalesua)
    if st.checkbox('Comparativo Salas x UA'):
       df['Minutos Usados']=round(pd.to_timedelta(df[above_352]['AttendeeTotalTimeInSession']).dt.total_seconds()/60)
       totalesuas=df[above_352].groupby("ua")['Minutos Usados'].sum() 
       st.bar_chart(totales)
    if st.checkbox('Tabla Salas x UA'):
       st.table(totales)
   
