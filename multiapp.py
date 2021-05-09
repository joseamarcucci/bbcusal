"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
#from load_css import local_css
#local_css("/mydrive/MyDrive/multiapps/style.css")

class MultiApp:
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
        st.sidebar.markdown('<img style="float: left;width:80%;margin-top:-70px;" src="https://virtual.usal.edu.ar/branding/themes/Usal_7Julio_2017/images/60usalpad.png" />', unsafe_allow_html=True)

        st.sidebar.title('Seleccionar plataforma:')
 
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
        
        app = st.sidebar.radio(
            '',
            self.apps,
            
            format_func=lambda app: app['title'])
      
              

        app['function']()


