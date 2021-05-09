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
        .css-d56p6e{text-align: left !important}

    </style>
    """, unsafe_allow_html=True) 
    st.markdown("<h3 style='text-align:  left; color: #008357;'>Usuarios Campus BBLearn</h3>", unsafe_allow_html=True)
   
    #SHEET_ID = '12D4hfpuIkT7vM69buu-v-r-UYb8xx4wM1zi-34Fs9ck'
    #df = pd.read_csv('https://docs.google.com/spreadsheets/d/' + SHEET_ID + '/export?format=csv')
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/1cZcUgS5AhhueUc3PXUcR6jWJgVmhzwQcp0E7RIYNuDU/export?format=csv&gid=1173523213')

    #df = pd.read_csv('/mydrive/MyDrive/multiapps/bbc204.csv')
    df=df.sort_values(by=['COURSE_NUMBER'])
    
    CHOICES = {456987: "PAD", 7896321: "FCEyE", 43: "MED", 453: "ELM", 45783: "ING", 8123: "LENGUAS", 48123: "FHGT", 457123: "JURI", 457823: "FCS", 4578128: "FLEO", 4578123: "HGT", 578128:"FCJ"}
    

    def format_func(option):
       return CHOICES[option] 
    
    buff, col, buff2 = st.beta_columns([1,3,1])

    option = buff.selectbox("Seleccionar Unidad", options=list(CHOICES.keys()), format_func=format_func)
    #st.write(f"Seleccionaste {format_func(option)}" )
    column = format_func(option)
    above_352 = df["COURSE_NUMBER"] == column
    sesionesu = df['STUDENT'].unique()
    df5=pd.value_counts(sesionesu)

    bool_series = df["COURSE_NUMBER"].str.startswith(column, na = False)
    dupli=df[above_352][bool_series].drop_duplicates(subset = ['COURSE'])
    cursos=df[bool_series]
    cursos.index = [""] * len(cursos)
    if st.checkbox('Usuarios por UA'):
       
       #dupli=cursos.drop_duplicates(subset = ['COURSE'])
       #st.table(dupli[['COURSE','COURSE_NUMBER','STUDENT']])
       options = ['#VALUE!'] 
    # selecting rows based on condition 
       dfv = df.loc[~df['ua'].isin(options)] 
       dupli=dfv.drop_duplicates(subset = ['STUDENT'])  
       totalesxua=dupli.groupby("ua")['STUDENT'].count() 
       
       st.bar_chart(totalesxua)
       st.table(totalesxua)
   
    sesiones = cursos['STUDENT'].unique()
    df6=pd.value_counts(sesiones)
    
    times3tt=df5.index
    aulastt=len(times3tt) 
  
    times3t=df6.index
    aulast=len(times3t) 
    #df['LAST_COURSE_ACCESS'] = pd.to_datetime(df['LAST_COURSE_ACCESS']).dt.strftime('%d-%m-%y')
    minValue = df['LAST_COURSE_ACCESS'].min()
    maxValue = df['LAST_COURSE_ACCESS'].max()
    st.write('Período:',minValue,' al ',maxValue)
    st.write('Usuarios: ',aulast)

    st.sidebar.write('Usuarios totales: ',aulastt)

    if st.checkbox('Mostrar Roles de la UA'):
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
       #df['Minutos Usados']=round(pd.to_timedelta(df[above_352]['AttendeeTotalTimeInSession']).dt.total_seconds()/60)
       #totalesua=df[above_352][bool_series].groupby("SessionName")['Minutos Usados'].sum() 
      roles=df[bool_series][['ROL','STUDENT']]
      dupli=roles.drop_duplicates(subset = ['STUDENT'])
      dupli=dupli.sort_values(by=['STUDENT'])
      dupli.index = [""] * len(dupli)
      totalesxuarol=dupli.groupby( ['ROL'])['STUDENT'].count()
      
      st.table(totalesxuarol)

    if st.checkbox('Mostrar Usuarios de la UA'):
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
       #df['Minutos Usados']=round(pd.to_timedelta(df[above_352]['AttendeeTotalTimeInSession']).dt.total_seconds()/60)
       #totalesua=df[above_352][bool_series].groupby("SessionName")['Minutos Usados'].sum() 
       roles=df[bool_series][['ROL','STUDENT']]
       dupli=roles.drop_duplicates(subset = ['STUDENT'])
       dupli=dupli.sort_values(by=['STUDENT'])
       dupli.index = [""] * len(dupli)

      
 
       st.table(dupli)
    #dupli=dupli.sort_values(by=['RoomClosed'])

      #st.table(totalesua)
    #st.markdown("### Sample Data")
    #df = create_table()
    #st.write(df)

    #st.write('Navigate to `Data Stats` page to visualize the data')
    if st.checkbox('Usuarios x curso'):
       #dupli=cursos.drop_duplicates(subset = ['COURSE'])
       #st.table(dupli[['COURSE','COURSE_NUMBER','STUDENT']])
       #reinput = st.text_input("Curso:")
       #if reinput:
          #df88 = df[df['COURSE'] == reinput]
       
          #st.table(df88[['COURSE','STUDENT']])
       totalesua=df[bool_series].groupby("COURSE")['STUDENT'].count() 
       st.table(totalesua)

