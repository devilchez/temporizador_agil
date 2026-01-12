import streamlit as st
from components.timer import show_timer
from pathlib import Path

# Configuración de la página
st.set_page_config(
    page_title="Digital Agile Timer",
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
        <h1>⏱️ Digital Agile Timer</h1>
        <p>Daily</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Selector de tiempo
minutes = st.slider("Duración del timer (minutos)", 5, 60, 25)

# Mostrar timer
show_timer(minutes)
