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
    monologue_panel.render("")
    mono_placeholder = st.empty()

with col_resp:
    response_panel.render("")
    resp_placeholder = st.empty()

message = st.chat_input("Talk to the brain...")

if message:
    full_text = ""
    
    # Clear the placeholders when a new message starts
    mono_placeholder.empty()
    resp_placeholder.empty()
    
    for event in client.chat_stream(message):
        t = event.get("type")
        
        if t == "state":
            with col_brain:
                brain_panel.render(event["data"])
                
        elif t in ("delta", "internal_delta", "spoken_delta"):
            full_text += event.get("content", "")
            
            # Robust parsing: Split by the <spoken> tag
            internal_text = ""
            spoken_text = ""
            
            if "<spoken>" in full_text:
                # Everything before <spoken> is the internal monologue
                parts = full_text.split("<spoken>", 1)
                internal_raw = parts[0]
                spoken_text = parts[1]
                
                # Clean up closing spoken tag if it has arrived
                if "</spoken>" in spoken_text:
                    spoken_text = spoken_text.split("</spoken>", 1)[0]
            else:
                # If no <spoken> tag yet, everything is still internal
                internal_raw = full_text
                
            # Clean up the internal tags
            internal_text = internal_raw.replace("<internal>", "").replace("</internal>", "").strip()
            spoken_text = spoken_text.replace("</spoken>", "").strip()
            
            # Render to the UI
            if internal_text:
                mono_placeholder.markdown(f"*{internal_text}*")
            if spoken_text:
                resp_placeholder.markdown(spoken_text)
                
        elif t == "error":
            st.error(event.get("message", "Unknown error"))
        elif t == "done":
            break