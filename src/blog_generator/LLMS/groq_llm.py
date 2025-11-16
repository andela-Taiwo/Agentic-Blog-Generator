from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import streamlit as st


class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        if self.user_controls_input is not None:
            try:
                groq_api_key = self.user_controls_input["API_KEY"]
                selected_groq_model = self.user_controls_input["selected_groq_model"]
                if groq_api_key == "" and os.environ["API_KEY"] == "":
                    st.error("Please Enter the Groq API KEY")

                llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)
                return llm
            except Exception as e:
                raise ValueError(f"Error Ocuured With Exception : {e}")
