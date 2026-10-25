#---- Libraries ----
import streamlit as st
#Streamlit: Preview Current File
#Streamlit: Stop Preview

import numpy as np
import pandas as pd


# ---------- Settings ----------
st.set_page_config(
    page_title = "Matublaq"
)
# CSS
# st.markdown("""
#     <style>
#     /* Cambiar el color de fondo principal de la aplicación */
#     .stApp {
#         background-color: #5d4c4b;
#     }
    
#     /* Modificar el padding superior e inferior del contenedor principal */
#     .block-container {
#         padding-top: 2rem;
#         padding-bottom: 2rem;
#         padding-left: 3rem;
#         padding-right: 3rem;
#     }
    
#     /* Cambiar el color de fondo de la barra lateral (sidebar) */
#     [data-testid="stSidebar"] {
#         background-color: #3c2a30;
#     }
#     </style>
# """, unsafe_allow_html=True)
#---------- Home page ----------
st.markdown("<h1></h1>")

#---------- Sidebar ----------
# st.sidebar("<p>Options</p>")