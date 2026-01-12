import streamlit as st
import time
from utils.time_utils import format_time

def show_timer(minutes: int):
    total_seconds = minutes * 60

    # Inicialización de estados
    if "remaining_seconds" not in st.session_state:
        st.session_state.remaining_seconds = total_seconds

    if "running" not in st.session_state:
        st.session_state.running = False

    if "paused" not in st.session_state:
        st.session_state.paused = False

    col1, col2, col3 = st.columns(3)

    # ▶ INICIAR / REANUDAR
    with col1:
        if st.button("▶ Iniciar / Reanudar"):
            st.session_state.running = True
            st.session_state.paused = False

    # ⏸ PAUSA
    with col2:
        if st.button("⏸ Pausa"):
            st.session_state.running = False
            st.session_state.paused = True

    # ⏹ RESET
    with col3:
        if st.button("⏹ Reset"):
            st.session_state.running = False
            st.session_state.paused = False
            st.session_state.remaining_seconds = total_seconds

    timer_placeholder = st.empty()

    # Mostrar tiempo actual
    timer_placeholder.markdown(
        f"""
        <div class="timer">
            {format_time(st.session_state.remaining_seconds)}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Lógica de cuenta regresiva
    if st.session_state.running and st.session_state.remaining_seconds > 0:
        time.sleep(1)
        st.session_state.remaining_seconds -= 1
        st.rerun()

    # Cuando termina
    if st.session_state.remaining_seconds == 0:
        st.session_state.running = False
        st.session_state.paused = False
