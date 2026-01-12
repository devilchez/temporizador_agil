import streamlit as st
from components.timer import show_timer
from pathlib import Path

# Configuración de la página
st.set_page_config(
    page_title="Daily",
    page_icon="⏱️",
    layout="centered"
)

# Cargar CSS
css_path = Path("assets/styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header
st.markdown(
    """
    <div class="header">
        <h1>⏱️ Daily</h1>
        <p>Digital Agile Timer</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Selector de tiempo
minutes = st.slider("Duración del timer (minutos)", 5, 15, 15)

# Mostrar timer
show_timer(minutes)
