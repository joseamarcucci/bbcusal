"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
import usuarios0
import usuarios
import todas0
#from load_css import local_css
#local_css("/mydrive/MyDrive/multiapps/style.css")
class MultiApp2:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """
    
    
    def __init__(self):

        
 
        self.apps = []

    def add_app(self, title, func):
        
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
   
             
        })
  
    def run(self):
        PAGES = {
        "Blackboard ULTRA:": todas0,
        "Usuarios del campus por UA": usuarios,
        "Usuarios totales del campus": usuarios0
        }

        selection = st.sidebar.radio("", list(PAGES.keys()))
        page = PAGES[selection]
        page.app()
            

        app['function']()
    