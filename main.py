import streamlit as st
from streamlit_option_menu import option_menu
import Home, Exercises, Contact

st.set_page_config(
    page_title="Health"
)

class MultiApp:
    def __init__(self):
        self.app=[]
    def add_app(self,title,function):
        self.apps.append({
            "title":title,
            "function":function
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Contents ',
                options=['Home','Exercises','Contact'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "15px"}, 
        "nav-link": {"color":"white","font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Home":
            Home.app()
        if app == "Exercises":
            Exercises.app()
        if app == "Contact":
            Contact.app() 
          
             
    run()            
         