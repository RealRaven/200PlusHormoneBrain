import streamlit as st


def render(content: str) -> None:
    st.subheader("💬 Spoken Response")
    st.markdown(content or "_(waiting...)_")