import streamlit as st
import sys
import os
import usuarios0
import usuarios
from multiapp import MultiApp

#import multiapp2 

import home, data_stats,tmayo,tmayo2,meses,mesesxuym,home5,moodle5,todas0,todasu,moodle,abril25,tjunio1,graba,tfebrero,tmarzo,tabril,home4,home2,moodle2,moodle4,usuarios,usuarios0,usuariosbbc # import your app modules here


st.set_page_config(
page_title="USAL Uso plataformas Blackboard",
page_icon="https://webinars.usal.edu.ar/sites/default/files/favicon.ico",
layout="wide",
initial_sidebar_state="expanded",)
app = MultiApp()

# Add all your application here

#st.sidebar.markdown("<h3 style='text-align: left; color: black;font-weight:500;'>Blackboard Collaborate y ULTRA</h3>", unsafe_allow_html=True)
app.add_app("Blackboard Collaborate:", todasu.app)
app.add_app("Febrero", tfebrero.app)
#app.add_app("Campus BBLearn ", home2.app)
#app.add_app("Campus Moodle ", moodle2.app)
app.add_app("Marzo", tmarzo.app)
#app.add_app("Campus BBLearn", home.app)
#app.add_app("Campus Moodle ", moodle.app)
app.add_app("Abril", tabril.app)
#app.add_app("16 al 21 de abril", data_stats.app)
#app.add_app("22 al 25 de abril", abril25.app)
#app.add_app("Campus BBLearn", home4.app)
#app.add_app("Campus Moodle", moodle4.app)
app.add_app("Mayo", tmayo.app)
app.add_app("Mayo30", tmayo2.app)
app.add_app("Junio15", tjunio1.app)
#app.add_app("16 al 21 de abril", data_stats.app)
#app.add_app("22 al 25 de abril", abril25.app)
#app.add_app("Campus BBLearn", home5.app)
#app.add_app("Campus Moodle", moodle5.app)
app.add_app("Grabaciones", graba.app)
#app.add_app("Usuarios BBC x mes", mesesxuym.app)
#app.add_app("Usuarios Collaborate", usuariosbbc.app)
app.add_app("Blackboard ULTRA:", todasu.app)
app.add_app("Usuarios del campus por UA", usuarios.app)
app.add_app("Usuarios totales del campus", usuarios0.app)

#app.add_app("16 al 21 de abril", data_stats.app)
#app.add_app("22 al 25 de abril", abril25.app)
#app.add_app("Datos x UA", todas.app)




app.run()

#PAGES = {
#    "Blackboard ULTRA:": todas0,
 #   "Usuarios del campus por UA": usuarios,
 #   "Usuarios totales del campus": usuarios0
#}
#st.sidebar.title('Navigation')
#election = st.sidebar.radio("", list(PAGES.keys()))
#page = PAGES[selection]
#page.app()

   
#app = MultiApp2()

#app.run()

