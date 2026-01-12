import streamlit as st
import time
from utils.time_utils import format_time

def show_timer(minutes: int):
    total_seconds = minutes * 60

    if "running" not in st.session_state:
        st.session_state.running = False

    col1, col2 = st.columns(2)

    with col1:
        if st.button("▶ Iniciar"):
            st.session_state.running = True

    with col2:
        if st.button("⏹ Reset"):
            st.session_state.running = False

    timer_placeholder = st.empty()

    if st.session_state.running:
        for remaining in range(total_seconds, -1, -1):
            timer_placeholder.markdown(
                f"""
                <div class="timer">
                    {format_time(remaining)}
                </div>
                """,
                unsafe_allow_html=True
            )
            time.sleep(1)
        st.session_state.running = False

