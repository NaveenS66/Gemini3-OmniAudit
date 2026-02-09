import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# --- CONFIGURATION ---
st.set_page_config(page_title="Gemini 3 Omni-Audit", layout="wide")
st.title("🛡️ Gemini 3: Omni-Audit")
st.write("Real-time Multimodal Reasoning & Safety Auditor")


# --- API KEY LOGIC ---


        # --- UI FOR UPLOAD ---
uploaded_file = st.file_uploader("Upload a scenario (Image) to Audit...", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Scenario Loaded.', use_column_width=True)
            
            user_task = st.text_input("What is the goal/task being performed in this image?", "e.g., I am repairing this circuit board")

            if st.button("Run Logic Audit"):
                with st.spinner('Gemini 3 is reasoning...'):
                    prompt = f"""
                    Analyze this image based on the goal: {user_task}.
                    1. Identify the logical steps being taken.
                    2. Flag any immediate safety risks or logical inconsistencies.
                    3. Provide a 'Reasoning Chain' for why the current setup might fail.
                    4. Suggest the next best logical move.
                    Format as: **Risk**, **Reasoning**, **Recommendation**.
                    """
                    response = model.generate_content([prompt, image])
                    
                    st.subheader("Audit Results")
                    st.markdown(response.text)

    except Exception as e:
        st.error(f"An error occurred: {e}")
        





