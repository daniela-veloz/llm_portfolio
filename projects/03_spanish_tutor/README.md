# 🎓 Spanish Language Tutor

An interactive AI-powered Spanish language learning companion that combines conversational chat with natural speech synthesis for immersive language learning.

## 📋 Overview

This project creates an engaging Spanish tutoring experience using advanced AI technology. The system provides personalized Spanish lessons through interactive conversations, helping English speakers learn Spanish naturally. Each response includes both text and audio feedback using OpenAI's text-to-speech capabilities, creating an immersive learning environment that mimics real conversations with a native Spanish tutor.

## ✨ Key Features

- **🤖 AI-Powered Tutoring**: Uses OpenAI's `gpt-4o-mini` for intelligent, contextual Spanish language instruction
- **🔊 Text-to-Speech Integration**: Natural voice synthesis using OpenAI's TTS API with high-quality voice options
- **💬 Interactive Chat Interface**: Gradio-powered web interface for seamless conversation flow
- **📚 Conversation History**: Maintains context across interactions for personalized learning progression
- **🎯 English-Focused Explanations**: Provides explanations in English while teaching Spanish vocabulary and grammar
- **🌐 Web-Based Interface**: Accessible through any web browser for convenient learning sessions

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **AI Model** | OpenAI GPT-4o-mini | Language instruction and conversation |
| **Text-to-Speech** | OpenAI TTS API | Natural voice synthesis |
| **Web Interface** | Gradio | Interactive chat interface |
| **Audio Processing** | PyDub, SimpleAudio | Audio file handling and playback |
| **Language** | Python | Core development |
| **Environment** | Jupyter Notebook | Development and demonstration |

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Jupyter Lab or Jupyter Notebook
- OpenAI API key
- Audio output capability (speakers/headphones)

### Installation

1. **Install Python dependencies**:
   ```bash
   pip install openai gradio python-dotenv pydub simpleaudio jupyter
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
   Navigate to `spanish_tutor.ipynb` and run the cells

### Quick Start Example

```python
# Create Spanish tutor instance
spanish_tutor = SpanishTutor("gpt-4o-mini")

# Start a conversation (with audio response)
response = spanish_tutor.chat("How do I say 'I'm hungry' in Spanish?", [])
print(response)  # Text response + audio playback
```

### Launching the Web Interface

```python
# Launch interactive web interface
gr.ChatInterface(fn=chat, type="messages").launch()
```

## 📁 Project Structure

```
03_spanish_tutor/
├── README.md                    # This file
└── spanish_tutor.ipynb          # Main Jupyter notebook

# Note: .env file should be created at the project root level
```

## 🔧 Core Components

### `LLMClient` Class
Handles OpenAI API integration for both text generation and speech synthesis with support for conversation history.

**Key Methods:**
- `generate_text()`: Generates conversational responses with history context
- `generate_speech()`: Creates speech audio from text using TTS API

### `TextToSpeech` Class  
Manages text-to-speech conversion with audio file processing, playback, and cleanup functionality.

**Features:**
- Multiple voice options (alloy, echo, fable, onyx, nova, shimmer)
- Automatic audio file management
- Cross-platform audio playback

### `SpanishTutor` Class
Main orchestration class that combines language model responses with audio output for comprehensive tutoring experience.

**Workflow:**
1. Processes user input with conversation history
2. Generates contextual Spanish tutoring response
3. Converts response to speech and plays audio
4. Returns text response for display

## 🎯 Use Cases

- **📖 Spanish Learning**: Interactive Spanish language instruction
- **🗣️ Pronunciation Practice**: Hear correct Spanish pronunciation
- **💬 Conversation Practice**: Engage in Spanish conversations with AI tutor
- **📝 Grammar Instruction**: Learn Spanish grammar through examples
- **🎯 Vocabulary Building**: Expand Spanish vocabulary through context
- **🏫 Educational Supplement**: Support traditional Spanish language courses

## 🎪 Interactive Features

- **Chat History**: Maintains conversation context for natural dialogue flow
- **Audio Playback**: Automatic speech synthesis for every tutor response
- **Web Interface**: Clean, user-friendly Gradio chat interface
- **Real-time Responses**: Immediate feedback and instruction

## 📚 Learning Approach

The AI tutor provides:
- **Spanish Translations**: Direct translations with pronunciation
- **Grammar Explanations**: Rules and patterns explained in English
- **Cultural Context**: Usage examples and cultural insights
- **Progressive Learning**: Adapts to your learning pace
- **Audio Pronunciation**: Hear correct Spanish pronunciation
- **Conversation Practice**: Natural dialogue in Spanish

## 💡 Benefits

- **🎧 Immersive Learning**: Audio responses create natural conversation experience
- **⏰ Available 24/7**: Practice Spanish anytime without scheduling constraints
- **🎯 Personalized Instruction**: AI adapts to individual learning pace and style
- **🔄 Immediate Feedback**: Instant responses and corrections
- **📱 Accessible**: Web-based interface works on any device with a browser
- **🎨 Engaging**: Interactive chat format makes learning enjoyable

## 🏆 Skill Level

**Beginner to Intermediate** - Perfect for developers learning:
- OpenAI API integration (Chat & TTS)
- Interactive web applications with Gradio
- Audio processing and playback
- Conversational AI system design
- Language learning application development

## 🚨 Important Notes

- Ensure you have a valid OpenAI API key for both chat and TTS functionality
- Audio output device (speakers/headphones) required for speech synthesis
- TTS functionality uses OpenAI's official API (cannot use local models)
- Be mindful of API usage costs, especially with frequent TTS requests
- Conversation history improves learning but increases token usage

## 📖 Example Conversations

**Learning Basic Phrases:**
```
User: "How do I say 'good morning' in Spanish?"
Tutor: "In Spanish, you say 'Buenos días' for 'good morning'. 
       'Buenos' means 'good' and 'días' means 'days'..."
[Audio plays with correct pronunciation]
```

**Grammar Practice:**
```
User: "Help me conjugate 'to eat' in present tense"
Tutor: "The verb 'comer' (to eat) conjugates like this in present tense:
       - Yo como (I eat)
       - Tú comes (You eat)..."
[Audio demonstrates pronunciation of each form]
```

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements or additional features like:
- Different language support
- Voice selection options
- Learning progress tracking
- Interactive exercises

## 📄 License

This project is for educational and demonstration purposes.

---

*This project demonstrates the integration of conversational AI, text-to-speech technology, and web interfaces to create an engaging language learning experience.*