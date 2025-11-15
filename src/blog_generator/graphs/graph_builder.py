from langgraph.graph import StateGraph, START, END
from src.blog_generator.LLMS.groq_llm import GroqLLM
from src.blog_generator.states.blog_state import BlogState
from src.blog_generator.nodes.blog_nodes import BlogNode
import os
from typing_extensions import Dict, List

from dataclasses import dataclass


@dataclass
class LanguageConfig:
    code: str
    node_name: str
    display_name: str


class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)
        self.blog_node_obj = None
        self.language_configs = self._initialize_language_configs()

    def _initialize_language_configs(self) -> Dict[str, LanguageConfig]:
        """Initialize all supported language configurations"""
        return {
            "hindi": LanguageConfig("hindi", "hindi_translation", "Hindi"),
            "french": LanguageConfig("french", "french_translation", "French"),
            "yoruba": LanguageConfig("yoruba", "yoruba_translation", "Yoruba"),
            "german": LanguageConfig("german", "german_translation", "German"),
            "arabic": LanguageConfig("arabic", "arabic_translation", "Arabic"),
            "mandarin": LanguageConfig("mandarin", "mandarin_translation", "Mandarin"),
            "hausa": LanguageConfig("hausa", "hausa_translation", "Hausa"),
            "swahili": LanguageConfig("swahili", "swahili_translation", "Swahili"),
            "igbo": LanguageConfig("igbo", "igbo_translation", "Igbo"),
        }

    def build_topic_graph(self):
        print("Igot hertetetetet")
        """
        Build a graph to generate blogss based on topic
        """
        self.blog_node_obj = BlogNode(self.llm)
        print(self.llm)
        ## Nodes
        self.graph.add_node("title_creation", self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation", self.blog_node_obj.content_generation)

        ## Edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", END)
        return self.graph

    def _build_language_graph(self):
        """
        Build a graph for blog generation with proper routing.
        """
        self.blog_node_obj = BlogNode(self.llm)

        # Define all supported languages and their nodes
        SUPPORTED_LANGUAGES = {
            "hindi": "hindi_translation",
            "french": "french_translation",
            "yoruba": "yoruba_translation",
            "german": "german_translation",
            "arabic": "arabic_translation",
            "mandarin": "mandarin_translation",
            "hausa": "hausa_translation",
            "swahili": "swahili_translation",
            "igbo": "igbo_translation",
            "english": "english_translation",
            "spanish": "spanish_translation",
        }

        # Core nodes
        self.graph.add_node("title_creation", self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation", self.blog_node_obj.content_generation)
        self.graph.add_node("route", self.blog_node_obj.route)

        # Translation nodes
        for lang_code, node_name in SUPPORTED_LANGUAGES.items():
            self.graph.add_node(
                node_name,
                lambda state, lang=lang_code: self.blog_node_obj.translation(
                    {**state, "current_language": lang}
                ),
            )

        # Build edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", "route")

        # Conditional edges - FIXED mapping
        self.graph.add_conditional_edges(
            "route",
            self.blog_node_obj.route_decision,
            # Map return values from route_decision to node names
            {
                "hindi": "hindi_translation",
                "french": "french_translation",
                "yoruba": "yoruba_translation",
                "german": "german_translation",
                "arabic": "arabic_translation",
                "mandarin": "mandarin_translation",
                "hausa": "hausa_translation",
                "swahili": "swahili_translation",
                "igbo": "igbo_translation",
                "english": "english_translation",
                "spanish": "spanish_translation",
            },
        )

        # All translation nodes lead to END
        for node_name in SUPPORTED_LANGUAGES.values():
            self.graph.add_edge(node_name, END)

        return self.graph

    def setup_graph(self, usecase):
        if usecase == "topic":
            self.build_topic_graph()
        if usecase == "language":
            print("Language block")
            self._build_language_graph()

        return self.graph.compile()


## Below code is for the langsmith langgraph studio
# user_input = os.getenv("user_input")
# llm=GroqLLM(user_controls_input=user_input).get_llm_model()

# ## get the graph
# graph_builder=GraphBuilder(llm)
# graph=graph_builder.build_language_graph().compile()
