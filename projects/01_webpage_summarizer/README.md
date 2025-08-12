---
title: WebPage Summarizer
emoji: 🌐
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: mit
---

# 🌐 WebPage Summarizer

An intelligent web content summarization tool that extracts and condenses webpage information using advanced AI models.

## 📋 Overview

This application creates concise, structured summaries of web content by leveraging state-of-the-art language models and robust web scraping techniques. Perfect for quickly understanding lengthy articles, blog posts, or documentation.

## ✨ Key Features

- **AI-Powered**: Powered by OpenAI's `gpt-4o-mini` for intelligent summaries
- **Advanced Web Scraping**: Uses BeautifulSoup to handle static websites efficiently
- **Markdown Output**: Generates clean, formatted summaries in Markdown
- **Smart Caching**: Repeated URLs use cached results for instant responses
- **Rate Limiting**: Fair usage protection with 10 hourly / 25 daily requests per user
- **IP-based Protection**: 60-second cooldown between requests
- **Easy Interface**: Simple Gradio web interface for immediate use

## 🛠️ Technology Stack

- **AI Models**: OpenAI GPT-4o-mini
- **Web Scraping**: BeautifulSoup, Python Requests  
- **Interface**: Gradio 4.44.0
- **Backend**: Modular Python architecture with caching, rate limiting, and IP extraction
- **AI Integration**: OpenAI API

## 🚀 Usage

1. **Enter URL**: Paste the webpage URL you want to summarize
2. **Click Summarize**: Get an intelligent markdown summary powered by GPT-4o-mini
3. **Smart Features**: Cached results for repeated URLs, rate limiting for fair usage

## 🎯 Perfect For

- **News Articles**: Quickly digest lengthy news content
- **Research Papers**: Extract key points from academic materials
- **Documentation**: Summarize technical documentation
- **Business Reports**: Extract insights from corporate content

## 🔧 Setup Requirements

### Environment Setup
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set OpenAI API Key**:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
   Or create a `.env` file:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

## 📝 Examples

Try these sample URLs:
- https://en.wikipedia.org/wiki/Marie_Curie
- https://en.wikipedia.org/wiki/Artificial_intelligence

## 💡 Tips

- Works best with content-rich pages (articles, blogs, documentation)
- Repeated requests to the same URL use cached results instantly
- Rate limits: 10 requests/hour, 25 requests/day per user
- 60-second cooldown between requests for abuse prevention
- Summaries include TL;DR sections for quick insights

---

**🚀 [Try it live on Hugging Face Spaces!](https://huggingface.co/spaces/daniela-veloz/webpage-summarizer)**



