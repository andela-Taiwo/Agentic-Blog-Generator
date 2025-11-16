import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json
import asyncio
import time


import asyncio
import streamlit as st
from typing import Optional


class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message, user_input_control):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message
        self.language = user_input_control.get("selected_language", "english")

    def display_result_on_ui(self):
        if self.usecase == "Blog Generation":
            self._simple_blog_stream()
        elif self.usecase == "Chatbot With Web":
            self._simple_chat_stream()

    def _simple_chat_stream(self):
        """Simple streaming implementation for chatbot"""
        initial_state = {"messages": [self.user_message]}

        # Display user message
        with st.chat_message("user"):
            st.write(self.user_message)

        # Stream AI response
        with st.chat_message("assistant"):
            response_placeholder = st.empty()

            for state in self.graph.stream(initial_state):
                if "messages" in state:
                    messages = state["messages"]
                    ai_messages = [
                        msg
                        for msg in messages
                        if type(msg) == AIMessage and msg.content
                    ]

                    if ai_messages:
                        response_placeholder.write(ai_messages[-1].content)

    def _simple_blog_stream(self):
        """Enhanced streaming with robust content extraction"""
        llm_input_data = {"topic": self.user_message, "current_language": self.language}
        config = {"configurable": {"thread_id": 123}}

        # Store both versions
        content_store = {"english": "", "translated": ""}

        # Stream the execution
        with st.spinner(f"🔄 Generating blog in {self.language}..."):
            for state in self.graph.stream(
                llm_input_data, config, stream_mode="values"
            ):
                # Update content store with latest content
                self._update_content_store(state, content_store)

                # Display current content
                current_content = self._get_display_content(content_store)
                if current_content:
                    if self.language.lower() != "english":
                        st.markdown(content_store["translated"])
                    else:
                        st.markdown(content_store["english"])

        # Display final results
        self._display_final_results(content_store)

    def _update_content_store(self, state, content_store):
        """Update content store with latest English and translated content"""
        for node_name, node_output in state.items():
            if hasattr(node_output, "get"):
                # Capture English content from content_generation node or similar
                if node_name in ["content_generation", "blog"] and node_output.get(
                    "content"
                ):
                    content_store["english"] = node_output.get("content")

                # Capture translated content from translation nodes
                if "_translation" in node_name and node_output.get(
                    "translated_content"
                ):
                    content_store["translated"] = node_output.get("translated_content")

                # Fallback: if we have a blog object with both contents
                if node_name == "blog":
                    if node_output.get("content"):
                        content_store["english"] = node_output.get("content")
                    if node_output.get("translated_content"):
                        content_store["translated"] = node_output.get(
                            "translated_content"
                        ).translated_content

    def _get_display_content(self, content_store):
        """Get the appropriate content to display during streaming"""
        if self.language.lower() != "english" and content_store["translated"]:
            return content_store["translated"]
        return content_store["english"]

    def _display_final_results(self, content_store):
        """Display final results with English dropdown for non-English languages"""
        if content_store["english"] or content_store["translated"]:
            st.success(f"✅ Blog successfully generated in {self.language}!")

            # Show English version in dropdown for non-English languages
            if self.language.lower() != "english" and content_store["english"]:
                st.markdown("---")
                with st.expander("🌐 View Original English Version", expanded=False):
                    st.markdown("### English Version")
                    st.markdown(content_store["english"])

                    # Optional: Add download button for English version
                    st.download_button(
                        label="📥 Download English Version",
                        data=content_store["english"],
                        file_name=f"blog_english_{int(time.time())}.md",
                        mime="text/markdown",
                    )
        else:
            st.error("❌ No content was generated")
