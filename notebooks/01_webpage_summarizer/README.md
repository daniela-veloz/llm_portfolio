# 🌐 WebPage Summarizer

An intelligent web content summarization tool that extracts and condenses webpage information using advanced AI models.

## 📋 Overview

This Jupyter notebook creates concise, structured summaries of web content by leveraging state-of-the-art language models and robust web scraping techniques. Perfect for quickly understanding lengthy articles, blog posts, or documentation.

## ✨ Key Features

- **🤖 AI-Powered Summarization**: Uses OpenAI's `gpt-4o-mini` for high-quality text summarization
- **🕷️ Dual Web Scraping Approaches**: 
  - Selenium WebDriver for dynamic JavaScript-rendered content
  - Requests + BeautifulSoup for faster static content extraction
- **🎯 Smart Content Extraction**: Intelligently identifies main content areas while filtering out navigation, ads, and other irrelevant elements
- **📝 Markdown Output**: Generates clean, formatted summaries in Markdown for easy reading and sharing
- **⚡ Flexible Architecture**: Choose between comprehensive Selenium scraping or lightweight HTTP requests

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **AI Model** | OpenAI GPT-4o-mini | Content summarization |
| **Web Scraping** | Selenium WebDriver | Dynamic content extraction |
| **HTML Parsing** | BeautifulSoup | Static content processing |
| **HTTP Client** | Python Requests | Fast web requests |
| **Environment** | Jupyter Notebook | Interactive development |

## 🚀 Quick Start

### Prerequisites

1. **Python Environment**: Python 3.8+ with Jupyter Lab
2. **API Keys**: OpenAI API key for summarization
3. **Chrome Browser**: Required for Selenium WebDriver

### Installation

```bash
# Install required packages
pip install selenium beautifulsoup4 webdriver-manager openai python-dotenv

# Or use uv (if available)
uv pip install selenium beautifulsoup4 webdriver-manager openai python-dotenv
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
# Simple summarization
summarize("https://en.wikipedia.org/wiki/Marie_Curie")
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
- Uses OpenAI's GPT-4o-mini model
- Structured prompts for consistent output
- Returns markdown-formatted summaries

## 🔧 Configuration

### WebUrlCrawler Options
```python
crawler = WebUrlCrawler(
    headless=True,    # Run browser in background
    timeout=10        # Page load timeout in seconds
)
```

### Model Configuration
```python
MODEL_OPENAI = "gpt-4o-mini"  # Can be changed to other OpenAI models
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

## 🚧 Limitations

- Requires stable internet connection
- OpenAI API usage incurs costs
- Some websites may block automated scraping
- JavaScript-heavy sites may require the Selenium approach

## 🤝 Contributing

This is part of a larger LLM portfolio project. Feel free to:
- Suggest improvements to content extraction
- Add support for additional AI models
- Enhance error handling and robustness

## 📄 License

Part of the LLM Portfolio project. See main repository for license details.

---

*Perfect for developers learning web scraping, AI integration, and content processing pipelines.*