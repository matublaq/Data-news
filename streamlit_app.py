from utils import *
# Patela de colores: #3c2a30 = rgb(60, 42, 48); #5d4c4b = rgb(93, 76, 75); #79676c = rgb(121, 103, 108); #c5b6a6 = rgb(197, 182, 166); #eae4d2 = rgb(234, 228, 210)

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

#---------- test área ----------
st.markdown("""
    <style>
    .test-container {
        width: 100%; /* Ancho */
        height: 100px /* Alura */
    }
    </style>
""", unsafe_allow_html=True)
st.markdown("<div class='test-container'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1: 
    color1, color2, color3, color4, color5 = st.columns(5)
    with color1: 
        st.markdown("<style>background-color: #3c2a30;</style>", unsafe_allow_html=True)
    with color2: 
        st.markdown("<style>background-color: #5d4c4b;</style>", unsafe_allow_html=True)
    with color3: 
        st.markdown("<style>background-color: #79676c;</style>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
#---------- Home page ----------
st.markdown("<h1 style='text-align: center;'>Data news</h1>", unsafe_allow_html=True)

#---------- Sidebar ----------
# st.sidebar("<p>Options</p>")