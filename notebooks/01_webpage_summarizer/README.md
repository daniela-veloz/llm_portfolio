# 🌐 WebPage Summarizer

An intelligent web content summarization tool that extracts and condenses webpage information using advanced AI models.

## 📋 Overview

This Jupyter notebook creates concise, structured summaries of web content by leveraging state-of-the-art language models and robust web scraping techniques. The tool supports both cloud-based and local AI models, including OpenAI's GPT-4o-mini and the open-source GPT-OSS:20B model through Ollama, providing flexibility for different deployment scenarios. Perfect for quickly understanding lengthy articles, blog posts, or documentation.

## ✨ Key Features

- **🤖 Dual AI Models**: Powered by OpenAI's `gpt-4o-mini` and open-source `gpt-oss:20b` through Ollama for high-quality text summarization
- **🔓 Local & Cloud Options**: Choose between cloud-based OpenAI models or run models locally with Ollama
- **🕷️ Dual Web Scraping Approaches**: 
  - Selenium WebDriver for dynamic JavaScript-rendered content
  - Requests + BeautifulSoup for faster static content extraction
- **🎯 Smart Content Extraction**: Intelligently identifies main content areas while filtering out navigation, ads, and other irrelevant elements
- **📝 Markdown Output**: Generates clean, formatted summaries in Markdown for easy reading and sharing
- **⚡ Flexible Architecture**: Choose between comprehensive Selenium scraping or lightweight HTTP requests

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **AI Models** | OpenAI GPT-4o-mini, GPT-OSS:20B | Content summarization |
| **Web Scraping** | Selenium WebDriver | Dynamic content extraction |
| **HTML Parsing** | BeautifulSoup | Static content processing |
| **HTTP Client** | Python Requests | Fast web requests |
| **AI Integration** | OpenAI API, Ollama | Model access and inference |
| **Local AI Runtime** | Ollama | Local model execution |
| **Environment** | Jupyter Notebook | Interactive development |

## 🚀 Quick Start

### Prerequisites

1. **Python Environment**: Python 3.8+ with Jupyter Lab
2. **API Keys**: OpenAI API key for cloud-based summarization (optional if using only Ollama)
3. **Chrome Browser**: Required for Selenium WebDriver
4. **Ollama** (Optional): For local model execution

### Installation

```bash
# Install required packages
pip install selenium beautifulsoup4 webdriver-manager openai python-dotenv

# Or use uv (if available)
uv pip install selenium beautifulsoup4 webdriver-manager openai python-dotenv
```

#### Ollama Setup (for local models)
To use the GPT-OSS:20B model locally:

1. **Install Ollama**: Visit [ollama.com](https://ollama.com) and download for your platform
2. **Pull the model**:
   ```bash
   ollama pull gpt-oss:20b
   ```
3. **Start Ollama service**: The service should start automatically, or run:
   ```bash
   ollama serve
   ```

### Environment Setup

1. Create a `.env` file in your project directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

2. Open the notebook:
```bash
jupyter lab webpage_summarizer.ipynb
```

### Basic Usage

```python
# Using OpenAI model
summarize("https://en.wikipedia.org/wiki/Marie_Curie", open_ai_llm_client)

# Using local Ollama model
summarize("https://en.wikipedia.org/wiki/Marie_Curie", gpt_oss_llm_client)
```

## 📚 How It Works

### 1. Web Content Extraction
Two scraping approaches available:

**Selenium WebUrlCrawler (Dynamic Content)**
- Handles JavaScript-rendered pages
- Waits for content to load
- More resource-intensive but comprehensive

**Requests WebUrlCrawler (Static Content)**
- Fast HTTP requests
- Lightweight and efficient
- Perfect for static HTML pages

### 2. Content Filtering
Both crawlers intelligently extract main content by:
- Removing unwanted elements: `script`, `style`, `img`, `input`, `button`, `nav`, `footer`, `header`
- Prioritizing main content containers: `main`, `article`, `[role="main"]`, `.content`, etc.
- Falling back to body content if no main containers found

### 3. AI Summarization
- Supports both OpenAI's GPT-4o-mini and local GPT-OSS:20B models
- Structured prompts for consistent output
- Returns markdown-formatted summaries
- Choose between cloud-based or local processing

## 🔧 Configuration

### WebUrlCrawler Options
```python
crawler = WebUrlCrawler(
    headless=True,    # Run browser in background
    timeout=10        # Page load timeout in seconds
)
```

### Model Configuration

**OpenAI Model**
```python
model_open_ai = "gpt-4o-mini"
open_ai_llm_client = LLMClient(model=model_open_ai)
```

**Local Ollama Model**
```python
model_gpt_oss = "gpt-oss:20b"
gpt_oss_llm_client = LLMClient(model=model_gpt_oss)
```

## 📁 Project Structure

```
notebooks/01_webpage_summarizer/
├── webpage_summarizer.ipynb    # Main notebook
├── README.md                   # This file
└── .env                        # Environment variables (create this)
```

## 🎯 Use Cases

- **📰 News Articles**: Quick summaries of current events
- **📚 Research Papers**: Extract key findings and methodology
- **📖 Documentation**: Condense technical guides
- **💼 Business Reports**: Extract actionable insights
- **🎓 Educational Content**: Study aid for academic materials
- **🔒 Private Content**: Use local Ollama models for sensitive information

## 🚧 Limitations

- Requires stable internet connection for web scraping
- OpenAI API usage incurs costs (Ollama is free for local use)
- Some websites may block automated scraping
- JavaScript-heavy sites may require the Selenium approach
- Local models (Ollama) require sufficient system resources

## 🤝 Contributing

This is part of a larger LLM portfolio project. Feel free to:
- Suggest improvements to content extraction
- Add support for additional AI models
- Enhance error handling and robustness

## 📄 License

Part of the LLM Portfolio project. See main repository for license details.

---

*Perfect for developers learning web scraping, AI integration, and content processing pipelines.*