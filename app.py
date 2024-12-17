import streamlit as st 
from streamlit_extras.bottom_container import bottom
from streamlit_chat_widget import chat_input_widget

st.markdown("###Testing chat input widget")
            
user_input_value_container = st.empty()
audio_container = st.empty()

user_input = chat_input_widget()

if user_input:
  user_input_value_container.write(user_input)
  if "audioFile" in user_input:
    with open("temp_audio_file.wav", "wb") as temp_audio:
      temp_audio.write(bytes(user_input["audioFile"]))
    with open("temp_audio_file.wav", "rb") as audio:
      audio_container.audio(audio)
      
