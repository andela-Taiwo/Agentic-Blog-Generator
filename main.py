from src.blog_generator.ui.streamlit import LoadStreamlitUI
import os
import time
import streamlit as st
from src.blog_generator.LLMS.groq_llm import GroqLLM
from src.blog_generator.LLMS.openai_llm import OpenAILLM
from src.blog_generator.graphs.graph_builder import GraphBuilder
from src.blog_generator.ui.display_result import DisplayResultStreamlit


def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while
    implementing exception handling for robustness.

    """

    ##Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return

    user_message = st.text_input(
        "Enter the Blog Topic you want to generate:",
    )

    if user_message:
        try:
            ## Configure The LLM's
            obj_llm_config = OpenAILLM(user_controls_input=user_input)
            if user_input["selected_llm"] == "Groq":
                obj_llm_config = GroqLLM(user_controls_input=user_input)

            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialized")
                return

            # Initialize and set up the graph based on use case
            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: No use case selected.")
                return

            ## Graph Builder

            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph("language")
                display = DisplayResultStreamlit(
                    usecase, graph, user_message, user_input
                )
                display.display_result_on_ui()

            except Exception as e:
                st.error(f"Error: 111Graph set up failed- {e}")
                return

        except Exception as e:
            st.error(f"Error: Graph set up failed- {e}")
            return
