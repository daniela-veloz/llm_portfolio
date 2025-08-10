# 📄 Brochure Generator

An AI-powered tool that automatically creates professional company brochures by analyzing websites and extracting relevant content using advanced web scraping and natural language processing.

## 📋 Overview

This project intelligently crawls company websites, identifies and extracts relevant content from multiple pages (About, Products, Contact, etc.), and generates polished marketing brochures using AI language models. The tool leverages OpenAI's GPT-4o-mini to create engaging, professional content suitable for potential customers, investors, and job seekers.

## ✨ Key Features

- **🤖 AI-Powered Content Generation**: Uses OpenAI's `gpt-4o-mini` for intelligent brochure writing
- **🕷️ Smart Web Crawling**: Automatically identifies and crawls relevant company website pages
- **🎯 Intelligent Link Selection**: Uses AI to filter and select only brochure-relevant links (About, Products, Contact, etc.)
- **📝 Professional Output**: Generates clean, marketing-ready content in Markdown format
- **🔗 Multi-Page Processing**: Combines content from multiple website pages for comprehensive brochures
- **🚀 Automated Workflow**: End-to-end automation from URL input to finished brochure

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **AI Model** | OpenAI GPT-4o-mini | Content generation and link analysis |
| **Web Scraping** | BeautifulSoup + Requests | Website content extraction |
| **JSON Processing** | Python JSON | AI response parsing |
| **Content Processing** | Custom classes | Website data management |
| **Output Format** | Markdown | Professional document formatting |
| **Language** | Python | Core development |

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Jupyter Lab or Jupyter Notebook
- OpenAI API key

### Installation

1. **Install Python dependencies**:
   ```bash
   pip install requests beautifulsoup4 openai python-dotenv jupyter
   ```

2. **Set up environment variables**:
   Create a `.env` file in the project root (not in this folder, but at the top level of the repository):
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. **Launch Jupyter**:
   ```bash
   jupyter lab
   ```

4. **Open the notebook**:
   Navigate to `brochure_generator.ipynb` and run the cells

### Quick Start Example

```python
# Initialize the brochure generator
brochure_generator = BrochureGenerator(
    llm_client=open_ai_llm_client, 
    company_name='Your Company', 
    url='https://yourcompany.com'
)

# Generate brochure content
brochure_content = brochure_generator.generate()
display(Markdown(brochure_content))
```

## 📁 Project Structure

```
02_brochure_generator/
├── README.md                    # This file
└── brochure_generator.ipynb     # Main Jupyter notebook

# Note: .env file should be created at the project root level
```

## 🔧 Core Components

### `WebSite` Class
Data structure for storing website information including URL, title, body content, and links.

### `WebUrlCrawler` Class
Handles web scraping using BeautifulSoup and requests. Extracts clean text content from web pages while filtering out unwanted elements.

### `LLMClient` Class
Manages OpenAI API integration for text generation. Supports both cloud-based OpenAI models and local configurations.

### `BrochureGenerator` Class
Main orchestration class that:
1. Crawls the main company website
2. Uses AI to identify relevant sub-pages
3. Extracts content from selected pages
4. Synthesizes everything into a professional brochure

## 🎯 Use Cases

- **🏢 Marketing Materials**: Generate professional company brochures
- **📈 Sales Enablement**: Create compelling company overviews for sales teams
- **💼 Investor Relations**: Extract key information for investor presentations
- **🎯 Content Automation**: Automate marketing content creation pipelines
- **📊 Competitive Analysis**: Analyze and summarize competitor websites

## 🔄 Workflow

1. **Input**: Provide company name and website URL
2. **Main Page Crawling**: Extract content from the primary webpage
3. **Link Analysis**: AI identifies relevant sub-pages (About, Products, Contact, etc.)
4. **Content Extraction**: Crawl and extract content from selected pages
5. **Content Synthesis**: AI generates cohesive brochure combining all content
6. **Output**: Professional markdown-formatted brochure

## 💡 Benefits

- **⏰ Time-Saving**: Reduces brochure creation time by 90%
- **🎯 Professional Quality**: AI-generated marketing content
- **📱 Consistent Format**: Standardized brochure structure across companies
- **🔄 Scalable**: Process multiple companies efficiently
- **🤝 Marketing-Ready**: Professional output ready for immediate use

## 🏆 Skill Level

**Intermediate** - Perfect for developers learning:
- AI-assisted content creation workflows
- Multi-step web scraping processes
- JSON parsing and data processing
- OpenAI API integration patterns
- Content synthesis techniques

## 📝 Example Output

The tool generates professional brochures with sections like:
- Company Overview
- Products & Services
- Company Culture
- Contact Information
- Key Differentiators

All formatted in clean Markdown for easy sharing and further processing.

## 🚨 Important Notes

- Ensure you have a valid OpenAI API key
- Be mindful of API usage costs when processing multiple companies
- Some websites may have anti-scraping measures
- Always respect robots.txt and website terms of service

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements or bug fixes.

## 📄 License

This project is for educational and demonstration purposes.

---

*This project demonstrates advanced AI integration for automated marketing content creation, combining web scraping, natural language processing, and content generation technologies.*