import streamlit as st


def render(content: str) -> None:
    st.subheader("💭 Internal Monologue")
    st.markdown(f"*{content}*" if content else "_(waiting...)_")