from utils import *
# Patela de colores: #3c2a30 = rgb(60, 42, 48); #5d4c4b = rgb(93, 76, 75); #79676c = rgb(121, 103, 108); #c5b6a6 = rgb(197, 182, 166); #eae4d2 = rgb(234, 228, 210)

# ---------- Settings ----------
st.set_page_config(
    page_title = "Matublaq"
)

# Contenedor flex en HTML que NUNCA se romperá ni se pondrá en vertical
st.markdown("""
    <div style="display: flex; gap: 8px; width: 100%;">
        <div style="flex: 1; height: 30px; background-color: #3c2a30; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#3c2a30</div>
        <div style="flex: 1; height: 30px; background-color: #5d4c4b; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#5d4c4b</div>
        <div style="flex: 1; height: 30px; background-color: #79676c; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#79676c</div>
        <div style="flex: 1; height: 30px; background-color: #938287; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#938287</div>
        <div style="flex: 1; height: 30px; background-color: #aba0a4; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#aba0a4</div>
    </div>
""", unsafe_allow_html=True)

#---------- Home page ----------
st.markdown("<h1 style='text-align: center;'>Data news</h1>", unsafe_allow_html=True)
with st.container(border=True):
    st.markdown("<p style='text-align: left;'>Data-science applied to news.<br>100% official data.</p>", unsafe_allow_html=True)
