from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
import os
import streamlit as st


class OpenAILLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        if self.user_controls_input is not None:
            try:
                openai_api_key = self.user_controls_input["API_KEY"]
                selected_groq_model = self.user_controls_input["selected_groq_model"]
                if openai_api_key == "" and os.environ["OPENAI_API_KEY"] == "":
                    st.error("Please Enter the OPENAI API KEY")

                llm = ChatOpenAI(api_key=openai_api_key, model=selected_groq_model)
                return llm
            except Exception as e:
                raise ValueError(f"Error Ocuured With Exception : {e}")
