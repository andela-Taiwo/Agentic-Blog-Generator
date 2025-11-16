from src.blog_generator.states.blog_state import BlogState
from langchain_core.messages import SystemMessage, HumanMessage
from src.blog_generator.states.blog_state import Blog


class BlogNode:
    """
    A class to represent he blog node
    """

    def __init__(self, llm):
        self.llm = llm

    def title_creation(self, state: BlogState):
        """
        create the title for the blog
        """

        if "topic" in state and state["topic"]:
            prompt = """
                You are an expert blog content writer. Use Markdown formatting. Generate
                a blog title for the {topic}. This title should be creative and SEO friendly

                """

            sytem_message = prompt.format(topic=state["topic"])
            response = self.llm.invoke(sytem_message)
            return {"blog": {"title": response.content}}

    def content_generation(self, state: BlogState):
        if "topic" in state and state["topic"]:
            # system_prompt = """You are expert blog writer. Use Markdown formatting.
            # Generate a detailed blog content with detailed breakdown for the {topic} using this structure.

            # You are a professional blog writer. Create a comprehensive blog post about {topic} using this structure example:

            # # Engaging Main Title

            # > Introduction
            # [Hook readers with compelling opening]

            # > Section Header in (H2)

            # > Subsection in (H3)

            # > Key points in bold** with supporting details
            # - Bullet points for lists
            # - Practical examples

            # ### Another Subsection (H3)
            # > Subtle emphasis with italics*
            # 1. Numbered steps where applicable
            # 2. Clear progression

            # > Important insights in blockquotes

            # ## Conclusion
            # [Memorable summary with key takeaways]

            # ## References
            # List out the references

            # Apply proper heading hierarchy, use bold/italics strategically, include examples, and maintain professional tone throughout.

            # """
            system_prompt = """You are a professional blog writer. Create a comprehensive blog post about {topic} using proper Markdown formatting.

            **FORMATTING GUIDELINES:**

            **HEADINGS:**
            # Main Title (H1 - Engaging and SEO-friendly)
            ## Section Headers (H2 - Major topics)
            ### Subsection Headers (H3 - Detailed breakdowns)
            #### Minor Points (H4 - When needed)

            **TEXT FORMATTING:**
            - **Bold** for key terms, definitions, and important concepts
            - *Italics* for emphasis, book titles, and foreign words
            - `Code format` for technical terms, commands, or specific references

            **LISTS:**
            - Bullet points (-) for features, benefits, and examples
            1. Numbered lists for steps, processes, and sequences

            **BLOCKQUOTES:**
            > Use for quotes, important insights, or highlighted information

            **STRUCTURE TEMPLATE:**
            """
            system_message = system_prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {
                "blog": {"title": state["blog"]["title"], "content": response.content}
            }

    def translation(self, state: BlogState):
        """
        Translate the content to the specified language.
        """
        translation_prompt = """
        Translate the following content into {current_language}.
        - Maintain the original tone, style, and formatting.
        - Adapt cultural references and idioms to be appropriate for {current_language}.

        ORIGINAL CONTENT:
        {blog_content}

        """

        blog_content = state["blog"]["content"]
        messages = [
            HumanMessage(
                translation_prompt.format(
                    current_language=state["current_language"],
                    blog_content=blog_content,
                )
            )
        ]
        translated_content = self.llm.with_structured_output(Blog).invoke(messages)
        return {
            "blog": {"translated_content": translated_content, "content": blog_content}
        }

    def route(self, state: BlogState):
        return {"current_language": state["current_language"]}

    def route_decision(self, state: BlogState) -> str:
        """
        Route the content to the respective translation function.

        Args:
            state: The current blog state containing language information

        Returns:
            str: The target language for translation
        """
        SUPPORTED_LANGUAGES = {
            "yoruba",
            "french",
            "german",
            "arabic",
            "mandarin",
            "hausa",
            "swahili",
            "igbo",
            "english",
        }

        current_lang = str(state["current_language"]).lower().strip()
        return current_lang if current_lang in SUPPORTED_LANGUAGES else current_lang

    def quality_check(self, state: BlogState) -> str:
        # [todo] add logic to perform quality check
        return "Moderate"
