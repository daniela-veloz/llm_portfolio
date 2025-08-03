# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a portfolio repository containing machine learning and AI projects with a focus on language models and educational applications. The main components are:

1. **FastAPI Web Service** (`main.py`) - A simple REST API with basic endpoints
2. **Spanish Language Tutor** (`spanish_tutor/spanish_tutor.ipynb`) - An interactive Gradio-based language learning application using OpenAI's GPT and TTS models

## Architecture

### FastAPI Application
- Entry point: `main.py`
- Simple REST API with two endpoints: root (`/`) and personalized greeting (`/hello/{name}`)
- Uses async/await patterns

### Spanish Tutor Application
- Jupyter notebook-based interactive application
- Integration with OpenAI API for chat completions and text-to-speech
- Uses Gradio for web interface
- Audio playback functionality using simpleaudio and pydub
- Requires environment variables for API keys

## Development Commands

### Environment Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables (create .env file with OPENAI_API_KEY)
```

### Running Applications
```bash
# FastAPI development server
uvicorn main:app --reload

# Jupyter Lab for notebook development
jupyter lab

# Test FastAPI endpoints
# Use test_main.http file with REST client extensions
```

### Testing
```bash
# FastAPI endpoints can be tested using the test_main.http file
# Default server runs on http://127.0.0.1:8000
```

## Key Dependencies

- **AI/ML**: openai, anthropic, transformers, torch, langchain ecosystem
- **Web**: fastapi, gradio, jupyter
- **Audio**: pydub, simpleaudio
- **Data**: pandas, numpy, scipy, scikit-learn
- **Visualization**: matplotlib, plotly

## Environment Variables Required

- `OPENAI_API_KEY` - Required for Spanish tutor application

## Project Structure Notes

- `common/` directory exists but appears to be empty
- No formal testing framework configured
- Dependencies managed through requirements.txt only
- No build configuration files (package.json, pyproject.toml, etc.)