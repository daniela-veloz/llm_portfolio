# 🌤️ Adventure Weather Agent

An intelligent activity planning assistant that combines real-time weather data with local event information to suggest personalized outdoor and indoor activities.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green.svg)
![Gradio](https://img.shields.io/badge/Gradio-Chat%20Interface-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 📋 Overview

The Adventure Weather Agent is a conversational AI system that helps users discover the best activities based on current weather conditions and available local events. By intelligently combining multiple data sources through advanced function calling, the agent provides personalized, weather-aware activity recommendations with a friendly and humorous personality.

### 🎯 What Makes It Special

- **Smart Weather Integration**: Real-time weather analysis to suggest appropriate activities
- **Multi-Source Event Discovery**: Aggregates events from TicketMaster and Google Places
- **Conversational AI**: Natural language interaction with personality and context awareness
- **Advanced Function Calling**: Sophisticated LLM function calling with error recovery
- **Interactive Web Interface**: Easy-to-use Gradio chat interface

## ✨ Key Features

### 🤖 AI-Powered Intelligence
- **Natural Conversation**: Chat naturally about your plans and preferences
- **Weather-Aware Planning**: Suggests indoor activities during bad weather, outdoor when sunny
- **Contextual Recommendations**: Remembers conversation context for better suggestions
- **Humorous Personality**: Engaging and entertaining interactions

### 🌦️ Real-Time Data Integration
- **Weather Forecasting**: Current conditions and multi-day forecasts
- **Live Events**: Real-time event discovery from multiple sources
- **Venue Information**: Detailed venue data and ratings
- **Location Intelligence**: Supports cities worldwide (where APIs provide coverage)

### ⚡ Technical Excellence
- **Robust Function Calling**: Handles complex multi-step API interactions
- **Parallel Processing**: Concurrent API calls for optimal performance
- **Error Recovery**: Graceful handling of API failures and edge cases
- **Extensible Architecture**: Easy to add new data sources and capabilities

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **AI Model** | OpenAI GPT-4o-mini | Conversational AI and decision making |
| **Weather Data** | WeatherAPI | Real-time weather and forecasts |
| **Event Discovery** | TicketMaster Discovery API | Live entertainment events |
| **Venue Information** | Google Places API | Event venues and locations |
| **Function Calling** | Custom LLMClient | Enhanced OpenAI function calling |
| **Web Interface** | Gradio ChatInterface | Interactive chat UI |
| **Parallel Processing** | ThreadPoolExecutor | Concurrent API operations |
| **Language** | Python 3.8+ | Core development |

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- API keys for required services (see setup below)

### 1. Clone the Repository

```bash
git clone <repository-url>
cd llm_portfolio/notebooks/04_adventure_weather_agent
```

### 2. Install Dependencies

```bash
pip install openai requests python-dotenv gradio concurrent-futures
```

### 3. Setup API Keys

Create a `.env` file in the project directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
WEATHER_API_KEY=your_weatherapi_key_here
TICKETMASTER_API_KEY=your_ticketmaster_api_key_here
GOOGLE_PLACES_API_KEY=your_google_places_api_key_here
```

### 4. Run the Application

```bash
jupyter lab adventure_weather_agent.ipynb
```

Then execute all cells to launch the Gradio interface.

## 🔑 API Key Setup

### Required API Keys

| Service | Purpose | Registration Link | Free Tier |
|---------|---------|------------------|-----------|
| **OpenAI** | AI conversation and reasoning | [platform.openai.com](https://platform.openai.com) | Pay-per-use |
| **WeatherAPI** | Weather data and forecasts | [weatherapi.com](https://www.weatherapi.com) | ✅ Free tier |
| **TicketMaster** | Live event discovery | [developer.ticketmaster.com](https://developer.ticketmaster.com) | ✅ Free tier |
| **Google Places** | Venue information and ratings | [developers.google.com/places](https://developers.google.com/places/web-service) | ✅ Free tier |

### Setup Instructions

1. **OpenAI API**: Create account → Generate API key → Add billing method
2. **WeatherAPI**: Sign up → Get free API key (1M calls/month)
3. **TicketMaster**: Register → Create app → Copy Consumer Key
4. **Google Places**: Enable Places API → Create credentials → Copy API key

## 🎨 Usage Examples

### Basic Weather Query
```
User: "What's the weather like in Seattle?"
Agent: *Fetches real-time Seattle weather and suggests appropriate activities*
```

### Activity Planning
```
User: "I'm visiting Austin this weekend. What should I do?"
Agent: *Checks Austin weather → Finds local events → Provides personalized recommendations*
```

### Weather-Aware Suggestions
```
User: "It's raining in Portland. Any indoor activities?"
Agent: *Suggests museums, theaters, shopping centers, and indoor entertainment*
```

### Event Discovery
```
User: "Any concerts happening in Denver this month?"
Agent: *Searches TicketMaster → Provides concert listings with dates, venues, and tickets*
```

## 🏗️ Architecture

### System Components

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Gradio UI     │────│  Adventure Agent │────│   LLM Client    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                       ┌────────┴────────┐
                       │                 │
                ┌──────────────┐  ┌─────────────────┐
                │ Weather API  │  │ Event Aggregator │
                └──────────────┘  └─────────────────┘
                                         │
                                ┌────────┴────────┐
                                │                 │
                        ┌───────────────┐ ┌──────────────┐
                        │ TicketMaster  │ │ Google Places│
                        └───────────────┘ └──────────────┘
```

### Function Calling Workflow

1. **User Input**: Natural language query received
2. **LLM Analysis**: GPT-4o-mini determines required data
3. **Function Calls**: Parallel API calls to weather and event services
4. **Data Aggregation**: Results combined and ranked
5. **Response Generation**: Personalized recommendations created
6. **User Output**: Formatted response with activities and details

## 🧪 Advanced Features

### Enhanced Function Calling System

- **Iterative Processing**: Handles multi-step function calling workflows
- **Error Recovery**: Robust handling of API failures and null responses
- **Message Management**: Proper conversation history throughout function calls
- **Debug Capabilities**: Optional debug output for development

```python
# Function registry maps LLM function calls to actual methods
function_registry = {
    "get_weather": self._get_weather,
    "get_events": self._get_events
}
```

### Event Intelligence

- **Smart Ranking**: Scores events based on relevance, ratings, and dates
- **Source Normalization**: Unified format across different event APIs
- **Venue Integration**: Combines event data with venue information
- **Geographic Filtering**: Location-aware event discovery

### Weather Analysis

- **Multi-Day Forecasts**: Up to 7-day weather predictions
- **Activity Suitability**: Weather condition analysis for activity recommendations
- **Seasonal Awareness**: Suggests season-appropriate activities

## 🔧 Development

### Project Structure

```
04_adventure_weather_agent/
├── adventure_weather_agent.ipynb    # Main notebook
├── README.md                        # This file
└── .env                            # API keys (not in repo)
```

### Key Classes

- **`LLMClient`**: Enhanced OpenAI client with advanced function calling, iterative processing, and error recovery
- **`WeatherService`**: WeatherAPI client with multi-day forecast support and static method descriptors
- **`EventService`**: Abstract base class defining interface for event service providers
- **`TicketMasterService`**: TicketMaster Discovery API client for live entertainment events
- **`GooglePlacesService`**: Google Places API client for event venues and entertainment locations
- **`EventServiceAggregator`**: Multi-source event aggregator with parallel processing and intelligent ranking
- **`ActivityAdventureAgent`**: Main conversational agent with function registry and Gradio chat interface

### Running Tests

Execute the test cells in the notebook to verify:
- API connections
- Function calling workflow
- Error handling
- Response generation

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- **New Data Sources**: Additional event APIs, restaurant data, transportation
- **Enhanced Recommendations**: ML-based preference learning
- **UI Improvements**: Better Gradio interface, mobile optimization  
- **Performance**: Caching, response time optimization
- **Testing**: Comprehensive test suite