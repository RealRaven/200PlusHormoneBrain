import os

import streamlit as st

from api_client import GatewayClient
from components import brain_panel, monologue_panel, response_panel

st.set_page_config(page_title="200+ Hormone Brain", layout="wide")
st.title("200+ Hormone Brain")

gateway_url = os.environ.get("GATEWAY_URL", "http://localhost:8000")
client = GatewayClient(gateway_url)

col_brain, col_mono, col_resp = st.columns([1, 1, 1])

with col_brain:
    try:
        state = client.get_state()
    except Exception as e:
        st.warning(f"Cannot reach gateway: {e}")
        state = {}
    brain_panel.render(state)

with col_mono:
    mono = st.empty()
    monologue_panel.render("")

with col_resp:
    resp = st.empty()
    response_panel.render("")

message = st.chat_input("Talk to the brain...")

if message:
    internal_acc: list[str] = []
    spoken_acc: list[str] = []

    for event in client.chat_stream(message):
        t = event.get("type")
        if t == "state":
            with col_brain:
                brain_panel.render(event["data"])
        elif t == "internal_delta":
            internal_acc.append(event["content"])
            mono.markdown(f"*{''.join(internal_acc)}*")
        elif t == "spoken_delta":
            spoken_acc.append(event["content"])
            resp.markdown("".join(spoken_acc))
        elif t == "error":
            st.error(event["message"])
        elif t == "done":
            break