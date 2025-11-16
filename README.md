### 🚀 Blog Generation Agent
A powerful, multi-language blog generation system built with LangGraph and Streamlit, featuring intelligent content creation, translation capabilities, and real-time streaming.

#### ✨ Features
🤖 AI-Powered Content Generation
    Advanced Language Models: GPT-4, Claude, and local LLM support

    Structured Blog Creation: Title generation, content development, and formatting

    SEO Optimization: Search-engine friendly content structure

    Professional Quality: Industry-standard blog formatting and tone

🌍 Multi-Language Support
    10+ Languages: English, French, Spanish, German, Hindi, Arabic, Yoruba, Hausa, Swahili, Igbo, Mandarin

    Smart Translation: Context-aware content translation

    Language Detection: Automatic routing based on target language

    Bilingual Display: View both original and translated versions

    ⚡ Real-time Streaming
    Live Progress Tracking: Watch content generate step-by-step

    Intermediate Results: See titles and sections as they're created

    Visual Feedback: Progress bars and status indicators

    Instant Updates: Content streams as it's generated

🎨 Professional Formatting
    Markdown Support: Headers, lists, bold, italics, and blockquotes

    Content Structure: Proper heading hierarchy (H1 → H2 → H3)

    Readable Layout: Clean, well-organized blog posts

    Mobile Responsive: Optimized for all screen sizes

🔄 Agentic Workflow
LangGraph Orchestration: Intelligent graph-based execution

Conditional Routing: Dynamic path selection based on language

Modular Design: Separate nodes for title, content, and translation

Error Recovery: Robust error handling and fallbacks

🛠️ Tech Stack
Core Frameworks
    LangGraph: Agent orchestration and workflow management

    Streamlit: Interactive web interface and UI components

    UV: Fast Python package management and dependency resolution

    Language Models
    OpenAI GPT: GPT-4, GPT-3.5 Turbo series

    Anthropic Claude: Claude-3 models for advanced reasoning

    Local LLMs: Optional local model support via Ollama

    Supporting Libraries
    LangChain: LLM integration and tool calling

    Pydantic: Data validation and settings management

    Python-dotenv: Environment configuration management

📦 Installation
Prerequisites
Python 3.12 or higher

UV package manager

API keys for your preferred LLM providers

Quick Start
Clone and setup

```bash
git clone <repository-url>
cd blog-generation-agent
uv sync
```

Configure environment

```bash
cp .env.example .env
```
# Add your API keys to .env
Launch application

```bash
uv run streamlit run app.py
```
🚀 Usage
Blog Generation Mode
-  Select "Blog Generation" from the use case dropdown

-  Choose your target language from 10+ supported options

-  Enter your blog topic or subject matter

-  Click "Generate" and watch real-time content creation

- Access original English version via dropdown for non-English outputs


#### 🏗️ Architecture
Core Components

    Workflow Pipeline
    text
    Start → Title Creation → Content Generation → Language Routing → Translation → End
        ↓                      ↓                   ↓
    Title Node           Content Node        Route Decision

#### ⚙️ Configuration
- Supported Languages
    English: Default language with full feature support

    European: French, Spanish, German

    Asian: Hindi, Arabic, Mandarin

    African: Yoruba, Hausa, Swahili, Igbo

#### Environment Variables
env
# Required: Choose at least one provider
OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key

# Optional: Enhanced features
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langchain_key
LANGCHAIN_PROJECT=your_project_name

### 🎯 Key Capabilities
#### Content Quality
- Research-Backed: Data-driven content with factual accuracy

- Engaging Writing: Compelling introductions and conclusions

- Actionable Insights: Practical advice and implementation guidance

- Reference Integration: Proper citations and source attribution

#### User Experience
- Intuitive Interface: Clean, modern Streamlit dashboard

- Progress Visibility: Real-time generation status and steps completed

- Error Handling: Graceful failure recovery and user feedback

- Export Options: Markdown download and copy-to-clipboard

#### Performance
- Fast Generation: 30-60 second typical blog creation time

- Streaming Output: Content displays as it's generated

- Memory Efficient: Optimized for continuous operation

- Scalable Design: Support for multiple concurrent users

🧪 Development
Project Setup
```bash
# Install with development dependencies
uv sync --dev

# Run code quality checks
uv run ruff check .
uv run black .
uv run mypy src/

# Execute test suite
uv run pytest tests/ -v
```
### Adding Features
- New Languages: Update language mapping in graph builder

- Content Types: Extend blog node with new templates

- UI Components: Add reusable Streamlit components

- Model Providers: Integrate additional LLM APIs



#### Development Workflow
Fork the repository and create a feature branch


📄 License
This project is licensed under the MIT License - see the LICENSE file for complete details.

#### To be Implemented
- 📊 Monitoring
- Quality check
- Correction feature
- Chatbot with Web Mode
    Select "Chatbot With Web" for interactive conversations

    Engage with AI assistant with web search capabilities

    Real-time message streaming and tool execution

    Context-aware responses and follow-up questions