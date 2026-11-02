from utils import *

# ---------- Settings ----------
st.set_page_config(
    page_title = "Matublaq", 
    layout="wide"
)
st.html(
    """
    <style>
        hr { border-color: #0d0d38 !important; margin: 0px; padding: 0px;}
    </style>
    """
)

# Contenedor flex en HTML que NUNCA se romperá ni se pondrá en vertical
st.markdown("""
    <style>
        /* Estilos */
    </style>
    <div style="display: flex; gap: 8px; width: 100%;">
        <div style="flex: 1; height: 30px; background-color: #33322B; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#33322B</div>
        <div style="flex: 1; height: 30px; background-color: #413D2B; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#413D2B</div>
        <div style="flex: 1; height: 30px; background-color: #6B6236; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#6B6236</div>
        <div style="flex: 1; height: 30px; background-color: #968532; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#968532</div>
        <div style="flex: 1; height: 30px; background-color: #C0A520; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#C0A520</div>
        <div style="flex: 1; height: 30px; background-color: #EBC301; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#EBC301</div>
    </div>
""", unsafe_allow_html=True)

#---------- Home page ----------
#--- Title ---
st.markdown("<h1 style='text-align: center; color: #C0A520'>Data news</h1>", unsafe_allow_html=True)

with st.container(border=False, key="h2_info"):
    st.markdown("<p style='text-align: center; color: #C0A520'>Data-science applied to news.<br>100% official data.</p>", unsafe_allow_html=True)

st.divider()
#--- Main news ---
col1a, col2a = st.columns(2)
with col1a: 
    st.markdown("chart 1")
with col2a: 
    st.write("Text 1")

st.divider()
#--- Projects ---
# Functions.
def project_card(image, link, title):
    tarjeta_html = f"""
    <a href="{link}" target="_blank" style="text-decoration: none;">
        <div style="
            width: 324px;
            height: 204px;
            border: 3px solid #33322B;
            border-radius: 12px;
            overflow: hidden;
            position: relative;
            background-color: #000000;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin: 15px auto;
        ">
            <img src="{image}" style="
                width: 100%;
                height: 100%;
                object-fit: cover;
            ">
            <div style="
                position: absolute;
                bottom: 0;
                width: 100%;
                background: rgba(0, 0, 0, 0.35);
                color: white;
                text-align: center;
                padding: 10px;
                font-family: sans-serif;
                font-weight: bold;
                font-size: 15px;
            ">
                {title}
            </div>
        </div>
    </a>
    """
    st.markdown(tarjeta_html, unsafe_allow_html=True)

col1b, col2b = st.columns(2)
with col1b: 
    project_card(image="https://images.unsplash.com/photo-1579546929518-9e396f3cc809", link="https://streamlit.io", title="CO2_vehicle_contamination")
with col2b: 
    project_card(image="https://images.unsplash.com/photo-1557683316-973673baf926", link="https://github.com", title="Spain train")

