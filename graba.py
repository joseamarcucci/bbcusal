import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import timedelta
from datetime import datetime
from data.create_data import create_table
from math import ceil
from bokeh.plotting import figure
import bokeh, bokeh.plotting

from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models import DataTable, TableColumn, HTMLTemplateFormatter

def app():
    buff,  buff2 = st.beta_columns([2,3])
    #buff.markdown('<img style="float: left;" src="https://virtual.usal.edu.ar/branding/themes/Usal_7Julio_2017/images/60usalpad.png" />', unsafe_allow_html=True)
    st.markdown(
    """<style>
        .grid-canvas{font-size:14px;}
        .slick-header-columns{font-size:16px;font-weight:500;color:#008357;}
    </style>
    """, unsafe_allow_html=True) 
    buff.markdown("<h3 style='text-align:  left; color: #008357;'>Grabaciones</h3>", unsafe_allow_html=True)
    buff.markdown("<h3 style='text-align:  left; color: #008357;'>Learn, Moodle y salas Collaborate</h3>", unsafe_allow_html=True)
   
    SHEET_ID = '1KTE7TM2xclv6PM7blUyApXLopBUvYWY9gbWWlJKBXwI' 
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/' + SHEET_ID + '/export?format=csv&gid=1396712')
    df=df.sort_values(by=['SessionOwner'])
    df1 = pd.read_csv('https://docs.google.com/spreadsheets/d/1KTE7TM2xclv6PM7blUyApXLopBUvYWY9gbWWlJKBXwI/export?format=csv&gid=249253768')
    #antes = pd.read_csv('https://docs.google.com/spreadsheets/d/1KTE7TM2xclv6PM7blUyApXLopBUvYWY9gbWWlJKBXwI/export?format=csv&gid=1158662089')
    
    if st.checkbox('Ver Cronograma de borrado'):

       df1.index = [""] * len(df1)
       st.table(df1)
    #gigasantes=antes['StorageUsageGigabytes'].sum()/1000000000
    gigas=df['StorageUsageGigabytes'].sum()/1000000000
    times3=df.index
    graba=len(times3)
    #times33=antes.index
    #graba2=len(times33)

    #st.sidebar.markdown("<h3 style='text-align: left; color: black;font-weight:500;'>Almacenamiento y cantidad</h3>", unsafe_allow_html=True)
    
    #st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    #st.sidebar.write('Semanal: ',round(gigas,1)," Gbytes")
    #st.sidebar.write('Semanal: ',graba)
  
  
    
    
    
   
    
    #df = pd.read_csv('/mydrive/MyDrive/multiapps/bbc204.csv')

  
    # selecting rows based on condition 
    options = ['ALEJANDRA.LAMBERTI','josemarcucci'] 
    # selecting rows based on condition 
    df = df.loc[~df['SessionOwner'].isin(options)] 
    countries = df['SessionOwner'].unique()
    
    
    country = buff.selectbox('Usuario BBC', countries)
    df[df['SessionOwner'] == country]   
    
 

    #option = st.selectbox("Seleccionar Unidad", options=list(CHOICES.keys()), format_func=format_func)
    #st.write(f"Seleccionaste {format_func(option)}" )
    #column = format_func(option)
    above_352 = df["SessionOwner"] == country
    
    bool_series = df[above_352]["SessionOwner"].str.startswith(country, na = False)
    time = pd.DatetimeIndex(df[above_352][bool_series]['RecordingDuration'])
    times1=time.hour * 60 + time.minute+ time.second/60
    times=times1.values.sum()
    #df[above_352][bool_series]['StorageUsageGigabytes']=df[above_352][bool_series]['StorageUsageGigabytes'].replace(",", "")
    #df[above_352][bool_series]['StorageUsageGigabytes']=df[above_352][bool_series]['StorageUsageGigabytes'].astype(int)
    gigast=df[above_352][bool_series]['StorageUsageGigabytes'].sum()/1000000000
    
    times3=df[above_352][bool_series].index
    aulas=len(times3)
    timee = pd.DatetimeIndex(df['RecordingDuration'])
    timees1=(timee.hour * 60 + timee.minute+ timee.second/60)
    timees=timees1.values.sum()
    st.sidebar.markdown("<h3 style='text-align: left; color: black;font-weight:500;'>Almacenamiento y cantidad</h3>", unsafe_allow_html=True)
   
    st.sidebar.write('Total: ',round(gigas,1)," Gbytes")
    st.sidebar.write('Total grabaciones: ',graba)
    #st.sidebar.write('Minutos grabados: ',timees)  

    df['RecordingCreated'] = pd.to_datetime(df['RecordingCreated']).dt.strftime('%y/%m/%d')
    #df.style.format({"RecordingCreated": lambda t: t.strftime("%d-%m-%Y")})
    maxValue = df['RecordingCreated'].max()
    minValue = df['RecordingCreated'].min()

    st.write('Período:',minValue,' al ',maxValue)
    
    st.write('Grabaciones: ',aulas)
    #st.write('Minutos grabados: ',round(times,1))
    
    from bokeh.models.widgets import Div


    #if st.button('Go to Streamlit'):
       #js = "window.open('https://www.streamlit.io/')"  # New tab or window
       #js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
       #html = '<img src onerror="{}">'.format(js)
       #div = Div(text=html)
       #st.bokeh_chart(div)
   


 
    
   
    if st.checkbox('Mostrar Grabaciones de la UA'):
       #df[above_352][bool_series][['RecordingCreated','SessionOwner','SessionName','RecordingDuration','StorageUsageGigabytes']].index = [""] * len(df[above_352][bool_series][['RecordingCreated','SessionOwner','SessionName','RecordingDuration','StorageUsageGigabytes']])
       todas=df[above_352][bool_series]
       todas.index = [""] * len(todas)
       todas=todas.sort_values(by=['RecordingCreated'])
       todas['RecordingCreated'] = pd.to_datetime(todas['RecordingCreated']).dt.strftime('%d-%m-%y')
       
       #todas['RecordingCreated']=todas['RecordingCreated'].apply(lambda _: datetime.strptime(_,"%m/%d/%Y, %H:%M:%S"))
       #datefmt = bokeh.models.DateFormatter(format="%d/%m/%Y")
       #st.table(todas[['RecordingCreated','SessionName','RecordingDuration','StorageUsageGigabytes']])
       df991 = pd.DataFrame({
       "Fecha": todas['RecordingCreated'],"Nombre":todas['SessionName'],"Autor": todas['SessionOwner'],"Duracion": todas['RecordingDuration'],"Tamaño": todas['StorageUsageGigabytes']
        })
       cds = ColumnDataSource(df991)
       columns = [
       TableColumn(field="Fecha", title="Fecha",width = 100),
       TableColumn(field="Nombre", title="Nombre",formatter=HTMLTemplateFormatter(template='<%= value %>'),width = 500),
       TableColumn(field="Autor", title="Autor", formatter=HTMLTemplateFormatter(template='<%= value %>'),width = 200),
       TableColumn(field="Duracion", title="Duracion", formatter=HTMLTemplateFormatter(template='<%= value %>'),width = 100),
       TableColumn(field="Tamaño", title="Tamaño", formatter=HTMLTemplateFormatter(template='<%= value %>'),width = 100),
        ]
       p3 = DataTable(source=cds, columns=columns, css_classes=["my_table"],index_position=None,width=1100, height=550)
       st.bokeh_chart(p3)
      
    if st.checkbox('Buscar Grabaciones de la UA'):
       buff8,  buff2 = st.beta_columns([2,3])
       #df[above_352][bool_series][['RecordingCreated','SessionOwner','SessionName','RecordingDuration','StorageUsageGigabytes']].index = [""] * len(df[above_352][bool_series][['RecordingCreated','SessionOwner','SessionName','RecordingDuration','StorageUsageGigabytes']])
       todas=df[above_352][bool_series]
       todas.index = [""] * len(todas)
       
       todas=todas.sort_values(by=['RecordingCreated'])
       todas['RecordingCreated'] = pd.to_datetime(todas['RecordingCreated']).dt.strftime('%d-%m-%y')
       solo=df[above_352][bool_series]
       solo=solo.sort_values(by=['SessionName'])
       solo=solo['SessionName'].unique()
       reinput = buff8.selectbox('Curso', solo)
       if reinput:
          df88 = todas[todas['SessionName'] == reinput]       
          df99 = pd.DataFrame({
          "Fecha": df88['RecordingCreated'],"Nombre":df88['SessionName'],"links": df88['RecordingLink']
          })
          cds = ColumnDataSource(df99)
          columns = [
          TableColumn(field="Fecha", title="Fecha",formatter=HTMLTemplateFormatter(template='<%= value %>'),width = 200),
          TableColumn(field="Nombre", title="Nombre",formatter=HTMLTemplateFormatter(template='<%= value %>'),width = 300),
          TableColumn(field="links", title="Grabacion", formatter=HTMLTemplateFormatter(template='<a href="<%= value %>"target="_blank"><%= value %></a>'),width = 400),


          ]
          p = DataTable(source=cds, columns=columns, css_classes=["my_table"],index_position=None,width=1000, height=250)
          st.bokeh_chart(p) 
       #st.table(todas[['RecordingCreated','SessionName','RecordingDuration','StorageUsageGigabytes']])
    if st.checkbox('Mostrar Todas las Grabaciones'):
       #df[above_352][bool_series][['RecordingCreated','SessionOwner','SessionName','RecordingDuration','StorageUsageGigabytes']].index = [""] * len(df[above_352][bool_series][['RecordingCreated','SessionOwner','SessionName','RecordingDuration','StorageUsageGigabytes']])
       todas1=df
       todas1.index = [""] * len(todas1)
       todas1=todas1.sort_values(by=['RecordingCreated'])
       todas1['RecordingCreated'] = pd.to_datetime(todas1['RecordingCreated']).dt.strftime('%d-%m-%y')
       df992 = pd.DataFrame({
       "Fecha": todas1['RecordingCreated'],"Nombre":todas1['SessionName'],"Autor": todas1['SessionOwner'],"Duracion": todas1['RecordingDuration'],"Tamaño": todas1['StorageUsageGigabytes']
        })
       cds = ColumnDataSource(df992)
       columns = [
       TableColumn(field="Fecha", title="Fecha",formatter=HTMLTemplateFormatter(template='<%= value %>'),width = 100),
       TableColumn(field="Nombre", title="Nombre",formatter=HTMLTemplateFormatter(template='<%= value %>'),width = 500),
       TableColumn(field="Autor", title="Autor", formatter=HTMLTemplateFormatter(template='<%= value %>'),width = 200),
       TableColumn(field="Duracion", title="Duracion", formatter=HTMLTemplateFormatter(template='<%= value %>'),width = 100),
       TableColumn(field="Tamaño", title="Tamaño", formatter=HTMLTemplateFormatter(template='<%= value %>'),width = 100),
        ]
       p2 = DataTable(source=cds, columns=columns, css_classes=["my_table"],index_position=None,width=1100, height=550)
       st.bokeh_chart(p2)
       #st.table(todas1[['RecordingCreated','SessionOwner','SessionName','RecordingDuration','StorageUsageGigabytes']])
   