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
        <p>Impulsando foco, agilidad y transformación digital</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Inicialización global de estados
if "running" not in st.session_state:
    st.session_state.running = False

if "paused" not in st.session_state:
    st.session_state.paused = False

if "last_minutes" not in st.session_state:
    st.session_state.last_minutes = 25

# Slider protegido
minutes = st.slider(
    "Duración del timer (minutos)",
    5,
    60,
    st.session_state.last_minutes,
    disabled=st.session_state.running or st.session_state.paused
)

# Sincronizar solo si el timer está detenido
if not st.session_state.running and not st.session_state.paused:
    if minutes != st.session_state.last_minutes:
        st.session_state.remaining_seconds = minutes * 60
        st.session_state.last_minutes = minutes

# Estado visual
if st.session_state.running:
    st.success("⏱️ Timer en ejecución")
elif st.session_state.paused:
    st.warning("⏸️ Timer en pausa")

# Timer
show_timer(minutes)
