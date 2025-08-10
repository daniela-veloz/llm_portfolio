# Spanish Language Tutor

**Purpose:** Interactive Spanish language learning assistant for English speakers using AI conversation and text-to-speech.

## Key Components

### 1. AI Chat System
- Uses OpenAI's GPT-4o-mini model for conversational responses
- System prompt configured for English-speaking Spanish learners
- Maintains conversation history for context

### 2. Text-to-Speech Integration
- OpenAI TTS model ("tts-1") with "onyx" voice
- Converts AI responses to spoken audio
- Audio pipeline: OpenAI TTS → MP3 → WAV conversion → playback

### 3. Audio Handling
- Uses `pydub` for audio format conversion
- `simpleaudio` for audio playback
- Creates temporary WAV files in ~/Documents
- **Fixed audio timing issue** - replaced problematic `wait_done()` with duration-based sleep

### 4. User Interface
- Gradio ChatInterface for web-based interaction
- Message-based conversation format
- Runs on local server (http://127.0.0.1:7885)

### 5. Environment Setup
- Requires `OPENAI_API_KEY` environment variable
- Loads configuration from `.env` file
- Error handling for missing API keys

## Usage

1. Set up your OpenAI API key in a `.env` file
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Jupyter notebook: `jupyter lab`
4. Execute all cells to start the tutor interface
5. Access the web interface at the provided local URLc