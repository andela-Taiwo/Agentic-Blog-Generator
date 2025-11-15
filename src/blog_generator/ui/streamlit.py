import streamlit as st
import os

from src.blog_generator.ui.ui_config_file import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(
            page_title="🤖 " + self.config.get_page_title(), layout="wide"
        )
        st.header("🤖 " + self.config.get_page_title())

        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] in ["OpenAI", "Groq"]:
                # Model selection
                model_options = (
                    self.config.get_openai_model_options()
                    if self.user_controls["selected_llm"] == "OpenAI"
                    else self.config.get_groq_model_options()
                )
                language_options = self.config.get_language_options()
                self.user_controls["selected_groq_model"] = st.selectbox(
                    "Select Model", model_options
                )
                self.user_controls["API_KEY"] = st.session_state["API_KEY"] = (
                    st.text_input("API Key", type="password")
                )
                # self.user_controls["OPENAI_API_KEY"] = st.session_state["OPENAI_API_KEY"]=st.text_input("API Key",type="password")

                self.user_controls["selected_language"] = st.selectbox(
                    "Select Language", language_options
                )

                # Validate API key
                if not self.user_controls["API_KEY"]:
                    st.warning(
                        "⚠️ Please enter your API key to proceed. Don't have? refer : https://console.groq.com/keys "
                    )

            ## USecase selection
            self.user_controls["selected_usecase"] = st.selectbox(
                "Select Usecases", usecase_options
            )

            if self.user_controls["selected_usecase"] == "Chatbot With Web":
                os.environ["TAVILY_API_KEY"] = self.user_controls[
                    "TAVILY_API_KEY"
                ] = st.session_state["TAVILY_API_KEY"] = st.text_input(
                    "TAVILY API KEY", type="password"
                )

                # Validate API key
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning(
                        "⚠️ Please enter your TAVILY_API_KEY key to proceed. Don't have? refer : https://app.tavily.com/home"
                    )

        return self.user_controls
