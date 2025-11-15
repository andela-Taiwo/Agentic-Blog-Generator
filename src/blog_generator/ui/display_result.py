import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json


class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message, user_input_control):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message
        self.language = user_input_control.get("selected_language", "english")

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        if usecase == "Blog Generation":
            llm_input_data = {"topic": user_message, "current_language": self.language}

            response = graph.invoke(llm_input_data)

            blog = response["blog"]

            if self.language.lower() != "english":
                translated_blog = blog["translated_content"]

                st.markdown(translated_blog.translated_content)
            st.markdown(blog["content"])
            # st.write("======================================")

        elif usecase == "Chatbot With Web":
            # Prepare state and invoke the graph
            initial_state = {"messages": [user_message]}
            res = graph.invoke(initial_state)
            for message in res["messages"]:
                if type(message) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message) == ToolMessage:
                    with st.chat_message("ai"):
                        st.write("Tool Call Start")
                        st.write(message.content)
                        st.write("Tool Call End")
                elif type(message) == AIMessage and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)
