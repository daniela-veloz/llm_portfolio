# 🤖 LLM Portfolio

A comprehensive collection of machine learning projects showcasing practical applications of Large Language Models (LLMs) and AI technologies for real-world use cases.

## 📋 Project Overview

This portfolio demonstrates proficiency in AI/ML development through three distinct applications, ranging from content processing to interactive educational tools. Each project showcases different aspects of modern AI development, from web scraping and content summarization to conversational interfaces and automated content generation.

### 🎯 Core Technologies

- **AI Models**: OpenAI GPT-4o-mini, GPT-OSS:20B (Ollama), Anthropic Claude
- **Web Frameworks**: FastAPI for REST APIs, Gradio for interactive interfaces
- **Data Processing**: Web scraping, content extraction, natural language processing
- **Development**: Jupyter notebooks, Python ecosystem
- **Infrastructure**: Local and cloud-based model deployment

## 🚀 Projects

### 1. 🌐 WebPage Summarizer
**`notebooks/01_webpage_summarizer/`**

An intelligent web content summarization tool that extracts and condenses webpage information using advanced AI models.

**Key Features:**
- Dual AI model support (OpenAI + local Ollama models)
- Advanced web scraping (Selenium + BeautifulSoup)
- Smart content extraction and filtering
- Markdown-formatted output

**Use Cases:** News summarization, research paper analysis, documentation condensing

[📖 Full Documentation](./notebooks/01_webpage_summarizer/README.md)

---

### 2. 📄 Brochure Generator  
**`notebooks/02_brochure_generator/`**

AI-powered tool that automatically creates professional company brochures by analyzing websites and extracting relevant content.

**Key Features:**
- Intelligent website crawling and content extraction
- AI-powered link selection and content synthesis
- Professional marketing-ready output
- Multi-page content processing

**Use Cases:** Marketing automation, sales enablement, competitive analysis

[📖 Full Documentation](./notebooks/02_brochure_generator/README.md)

---

### 3. 🎓 Spanish Language Tutor
**`notebooks/03_spanish_tutor/`**

Interactive AI-powered Spanish language learning companion with conversational chat and natural speech synthesis.

**Key Features:**
- Conversational AI tutoring with context memory
- Text-to-speech integration for pronunciation
- Interactive web interface via Gradio
- Personalized learning progression

**Use Cases:** Language learning, pronunciation practice, educational supplements

[📖 Full Documentation](./notebooks/03_spanish_tutor/README.md)

---

### 4. 🌐 FastAPI Web Service
**`main.py`**

A foundational REST API built with FastAPI demonstrating modern Python web development patterns.

**Features:**
- Async/await patterns
- REST API endpoints
- FastAPI framework integration

## 🛠️ Getting Started

### Prerequisites

- **Python 3.8+**
- **Jupyter Lab** for notebook development
- **OpenAI API Key** (for most projects)
- **Chrome Browser** (for web scraping projects)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd llm_portfolio
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Launch development environment:**
   ```bash
   # For notebook development
   jupyter lab
   
   # For FastAPI development
   uvicorn main:app --reload
   ```

### Quick Start Examples

**FastAPI Service:**
```bash
uvicorn main:app --reload
# Visit http://127.0.0.1:8000 for API endpoints
```

**WebPage Summarizer:**
```python
from webpage_summarizer import summarize, LLMClient
client = LLMClient(model="gpt-4o-mini")
summary = summarize("https://example.com", client)
```

**Brochure Generator:**
```python
generator = BrochureGenerator(llm_client, 'Company Name', 'https://company.com')
brochure = generator.generate()
```

**Spanish Tutor:**
```python
tutor = SpanishTutor("gpt-4o-mini")
response = tutor.chat("How do I say 'hello' in Spanish?", [])
```

## 📁 Project Structure

```
llm_portfolio/
├── main.py                              # FastAPI web service
├── requirements.txt                     # Python dependencies
├── test_main.http                       # API testing file
├── CLAUDE.md                            # Development instructions
├── common/                              # Shared utilities (empty)
└── notebooks/                           # Jupyter notebook projects
    ├── 01_webpage_summarizer/
    │   ├── webpage_summarizer.ipynb     # Web content summarization
    │   └── README.md                    # Project documentation
    ├── 02_brochure_generator/
    │   ├── brochure_generator.ipynb     # Company brochure generation
    │   └── README.md                    # Project documentation
    └── 03_spanish_tutor/
        ├── spanish_tutor.ipynb          # Interactive language tutor
        └── README.md                    # Project documentation
```

## 🎯 Skills Demonstrated

### **Machine Learning & AI**
- Large Language Model integration (OpenAI, Anthropic, Ollama)
- Natural language processing and text generation
- Conversational AI system design
- Local and cloud-based model deployment

### **Web Development**
- FastAPI REST API development
- Interactive web interfaces with Gradio
- Web scraping with multiple approaches (Selenium, BeautifulSoup)
- Async/await patterns and modern Python practices

### **Data Processing**
- Content extraction and cleaning
- Multi-source data synthesis
- Audio processing and text-to-speech integration
- Structured output generation (Markdown, JSON)

### **Software Engineering**
- Jupyter notebook development
- Environment configuration and dependency management
- API integration and error handling
- Modular, reusable code architecture

## 🔧 Configuration Options

### Model Selection
- **OpenAI Models**: GPT-4o-mini for cloud-based processing
- **Local Models**: GPT-OSS:20B via Ollama for privacy-sensitive tasks
- **Anthropic**: Claude integration for diverse AI capabilities

### Development Commands

```bash
# FastAPI development
uvicorn main:app --reload

# Jupyter Lab
jupyter lab

# Testing API endpoints
# Use test_main.http with REST client extensions
```

## 🌟 Use Cases & Applications

- **Content Automation**: Automated summarization and brochure generation
- **Educational Technology**: Interactive language learning applications  
- **Web Intelligence**: Smart content extraction and analysis
- **Marketing Automation**: Professional content generation from web sources
- **Research Tools**: Academic and news content processing
- **Multilingual Applications**: Language learning and cross-cultural communication

## 🚨 Important Notes

- **API Costs**: Be mindful of OpenAI API usage, especially with TTS and frequent requests
- **Environment Variables**: Ensure proper `.env` setup for API keys
- **Web Scraping**: Respect robots.txt and website terms of service
- **Audio Requirements**: Spanish Tutor requires audio output capabilities
- **Local Models**: Ollama setup required for offline AI processing

## 🤝 Contributing

This portfolio welcomes contributions and improvements:

1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

**Contribution Areas:**
- Additional AI model integrations
- Enhanced web scraping capabilities
- New language support for the tutor
- Performance optimizations
- Additional educational applications

## 📄 License

This project is for educational and portfolio demonstration purposes.

---

**🎯 Perfect for developers interested in:**
- AI/ML application development
- Web scraping and content processing
- Interactive educational tools
- Modern Python web development
- LLM integration patterns

*This portfolio showcases practical AI applications combining web technologies, natural language processing, and user-friendly interfaces to solve real-world problems.*