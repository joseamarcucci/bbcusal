import streamlit as st
import pandas as pd
import numpy as np
from bokeh.plotting import figure
import bokeh, bokeh.plotting

from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models import DataTable, TableColumn, HTMLTemplateFormatter

import matplotlib.pyplot as plt
import streamlit.components.v1 as components
from data.create_data import create_table
from math import ceil
def app():


    #st.markdown('<img style="float: left;" src="https://virtual.usal.edu.ar/branding/themes/Usal_7Julio_2017/images/60usalpad.png" />', unsafe_allow_html=True)
    st.markdown('<style>div[data-baseweb="select"] > div {text-transform: capitalize;}body{background-color:#008357;}</style>', unsafe_allow_html=True)
    st.markdown(
    """<style>
        .css-1v3fvcr {
    display: flex;
    flex-direction: column;
    width: 100%;
    margin-top: -100px;
    overflow: auto;
    -webkit-box-align: center;
    align-items: center;
    }
        .grid-canvas{font-size:14px;}
        .slick-header-columns{font-size:16px;font-weight:500;color:#008357;}
    </style>
    """, unsafe_allow_html=True) 

    st.markdown("<h3 style='text-align: left; color: #008357;'>Uso Collaborate</h3>", unsafe_allow_html=True)

    st.subheader('Totales del mes') 
    st.subheader("Mayo")
    #st.write("Minutos consumidos: 38303371")
    
    col1, col2, col3 = st.beta_columns([1,2,1])
    buff, col, buff2,  = st.beta_columns([3,3,3]) 
    # MultiSelect
    # initialize list of lists
    #data = [['Febrero', '1yvDAVczwETC2JwcNeaYx2h2PD5fGCSWdJoY4QoMqR48'], ['Marzo', '1bFvGJ8q1C-H7QiUY395L3UzuQk_xrUAWsaNOagQ9c5s'], ['Abril', '1kNaXpaA0OiKZyWBfeBwm9SW6O9YfpSh6DcDQaFZGkSg'], ['Mayo', '1ZP1OcE1DWAr8lhWqo2apJH7V9xN9N-4mVaa87MC7HL4']]

# Create the pandas DataFrame
    #df0 = pd.DataFrame(data, columns=['Name', 'ID'])

    #values = df0['Name'].tolist()
    #options = df0['ID'].tolist()
    #dic = dict(zip(options, values))

    #a = buff.selectbox('Seleccionar mes:', options, format_func=lambda x: dic[x])

    
   
    #SHEET_ID = '12D4hfpuIkT7vM69buu-v-r-UYb8xx4wM1zi-34Fs9ck'






    #st.write(a)
  
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/1ZP1OcE1DWAr8lhWqo2apJH7V9xN9N-4mVaa87MC7HL4/export?format=csv')
    
    #df = pd.read_csv('/mydrive/MyDrive/multiapps/bbc204.csv')
    df=df.sort_values(by=['SessionOwner'])
    options = ['ALEJANDRA.LAMBERTI','josemarcucci']
    df22 = df.loc[~df['SessionOwner'].isin(options)] 
    df22['Minutos']=round(pd.to_timedelta(df22['AttendeeTotalTimeInSession']).dt.total_seconds()/60)

    options = ['ALEJANDRA.LAMBERTI','josemarcucci','USAL_lti_production','USAL_rest_production'] 
    # selecting rows based on condition 
    df = df.loc[~df['SessionOwner'].isin(options)] 


    duplit=df.drop_duplicates(subset = ['SessionName'])
    df5=pd.value_counts(duplit['SessionName'])
    #tim = pd.DatetimeIndex(df['AttendeeTotalTimeInSession'])
    #tims1=df[tim.hour * 60 + tim.minute+ tim.second/60]
    #tims=tims1.values.sum()

    #totales0=df['AttendeeTotalTimeInSession'].apply(lambda x: sum([a*b for a,b in zip(list(map(int,x.split(':')))[::-1],[1/60,1,60])]))
    df['Minutos']=round(pd.to_timedelta(df['AttendeeTotalTimeInSession']).dt.total_seconds()/60)
    totales=df['Minutos'].sum()
    #st.write(totales)

    
    '## Tipo de plataforma'
    #if st.checkbox('Ver comparativo UAs'):
       #st.bar_chart(totales)
    #country = st.sidebar.selectbox('Usuario BBC o plataforma', countries)
  
    #df[df['SessionOwner'] == country]

    #above_352 = df["SessionOwner"] == country


    #option = st.selectbox("Seleccionar Unidad", options=list(CHOICES.keys()), format_func=format_func)
    #st.write(f"Seleccionaste {format_func(option)}" )
    #column = format_func(option)
     
    #moderador = df["AttendeeRole"] == "Moderator" 
    
    #bool_series = df[above_352]["SessionOwner"].str.startswith(country, na = False)
    #dupli=df[above_352][bool_series].drop_duplicates(subset = ['SessionName'])
    #df[above_352][bool_series]['AttendeeFirstJoinTime'] = pd.to_datetime(df[above_352][bool_series]['AttendeeFirstJoinTime']).dt.strftime('%y-%m-%d')
    #dupliu=df[above_352][bool_series].groupby("SessionOwner", as_index=False)['NameOfAttendee'].nunique()
    #dupli=df[above_352][bool_series].drop_duplicates(['SessionName']).groupby('SessionName').agg({'AttendeeTotalTimeInSession':'sum'})
    #sesiones = df[above_352][bool_series]['SessionName'].unique()
   
    #partic= df[above_352][bool_series]['SessionName'].unique()
    usuarios=df.groupby("SessionOwner", as_index=False).agg({ 'NameOfAttendee' : 'nunique',  'Minutos' : 'sum'})
    #st.bokeh_chart(p3)
    usuarios.index = [""] * len(usuarios)
    usuarios.columns = ['UA', 'Usuarios','Minutos']
    #usuarios.to_csv('/mydrive/MyDrive/multiapps/survey_data.csv',index=False)
   
    df55=(usuarios['Usuarios']).sum()
    timeu = pd.DatetimeIndex(df22['AttendeeTotalTimeInSession'])
    times1u=timeu.hour * 60 + timeu.minute+ timeu.second/60
    timesu=times1u.values.sum()
    times3t=df5.index
    aulast=len(times3t)
    #buff.write(round(timesu,))
    st.sidebar.write('Minutos/mes: ',round(timesu,0))
    st.sidebar.write('Minutos/totales: ',29969107+round(timesu,0))
    df8 = pd.DataFrame({
 
  
    'Minutos totales': [round(timesu,0)]
       })
    #df8=df8.sort_values(by=['Minutos'])
    df8.index = [""] * len(df8)
    
   
    
    #buff.header('Salas')
    df81 = pd.DataFrame({

    'Minutos': [round(totales,0)]
       })
    #df8=df8.sort_values(by=['Minutos'])
    df81.index = [""] * len(df81)
    #buff.table(df81) 
    
    #buff.table(usuarios)
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/1ZP1OcE1DWAr8lhWqo2apJH7V9xN9N-4mVaa87MC7HL4/export?format=csv')
    options = ['ALEJANDRA.LAMBERTI','josemarcucci'] 
    # selecting rows based on condition 
    df = df.loc[~df['SessionOwner'].isin(options)] 
    above_352 = df["SessionOwner"] == 'USAL_lti_production'
    sesionesu = df[above_352]['SessionName'].unique()
    df5=pd.value_counts(sesionesu)
    above_3522 = df["SessionOwner"] == 'USAL_rest_production'
    df52=pd.value_counts(df[above_3522]['SessionName'])

    #bool_series = df[above_352]["ContextIdentifier"].str.startswith(column, na = False)
    dupli=df[above_3522].drop_duplicates(subset = ['SessionName'])



    df['Minutos']=round(pd.to_timedelta(df[above_352]['AttendeeTotalTimeInSession']).dt.total_seconds()/60)

    usuariosl=df[above_352].groupby("ua", as_index=False).agg({ 'NameOfAttendee' : 'nunique',  'Minutos' : 'sum'})
    totales=usuariosl['Minutos'].sum()
    usu=usuariosl['NameOfAttendee'].sum()
    
    #col.header('Learn')

    df81 = pd.DataFrame({
     'Usuarios':[round(usu,0)],
    'Minutos': [round(totales,0)]
       })
    #df8=df8.sort_values(by=['Minutos'])
    df81.index = [""] * len(df81)
    #col.table(df81)

    usuariosl.columns = ['UA', 'Usuarios','Minutos']
    usuariosl.index = [""] * len(usuariosl)
    
    #col.table(usuariosl)


    df['Minutos']=round(pd.to_timedelta(df[above_3522]['AttendeeTotalTimeInSession']).dt.total_seconds()/60)

    usuariosm= df[above_3522].groupby("SessionName", as_index=False).agg({ 'NameOfAttendee' : 'nunique',  'Minutos' : 'sum'})

    #st.markdown("### Sample Data")
    #df = create_table()
    #st.write(df)
    totales=usuariosm['Minutos'].sum()
    usu=usuariosm['NameOfAttendee'].sum()
    #buff2.header('Moddle')
    df81 = pd.DataFrame({
     'Usuarios':[round(usu,0)],
    'Minutos': [round(totales,0)]
       })
    #df8=df8.sort_values(by=['Minutos']) 
    df81.index = [""] * len(df81)
    #buff2.table(df81) 
    #totalesua.columns = ['UA', 'Usuarios','Minutos']
    #usuariosm['SessionName'] = usuariosm['SessionName'].str.slice(0,12)
    usuariosm.columns = ['UA', 'Usuarios','Minutos']
    usuariosm.index = [""] * len(usuariosm)
    
    #buff2.table(usuariosm)
    dfin = usuarios.groupby('UA').sum().add(usuariosl.groupby('UA').sum(), fill_value=0).reset_index()
    usuarios['%']= 100*usuarios['Minutos']/usuarios['Minutos'].sum()
    usuariosl['%']= 100*usuariosl['Minutos']/usuariosl['Minutos'].sum()
    dfin['%']= 100*dfin['Minutos']/dfin['Minutos'].sum()
    dfin.index = [""] * len(dfin)
    #col.line_chart(dfin['UA','Minutos'])

    

    
    #if st.checkbox('Distribución x plataforma'):
    col.header('Salas')
    col.table (usuarios[['UA','Minutos','%']])
    buff2.header('Learn')
    buff2.table (usuariosl[['UA','Minutos','%']])
    st.header('Moddle')
    st.table (usuariosm[['UA','Minutos']])
    buff.header('Totales')
    buff.table (dfin[['UA','Minutos','%']])
    




  

