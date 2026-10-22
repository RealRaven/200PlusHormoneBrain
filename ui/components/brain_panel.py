import streamlit as st

def render(state):
    st.subheader("🧠 Brain State")
    
    # Example of how it might display the state:
    if not state:
        st.write("Waiting for state...")
        return
        
    for chem, level in state.items():
        st.progress(level / 100.0, text=f"{chem}: {level}")