# Azure OpenAI Integration

This folder contains code for integrating with Azure OpenAI services, providing a simple interface for chat completions and text generation tasks.

## Features

- Azure OpenAI service integration with proper configuration management
- Chat completion examples with various parameters
- Lyric completion demo using conversation history
- Environment variable management for secure configuration

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Configure your environment variables by copying `.env.example` to `.env`:
```bash
cp .env.example .env
```

3. Update the `.env` file with your Azure OpenAI credentials:
```env
OPENAPI_API_KEY=your_api_key
OPENAPI_API_VERSION=your_api_version
OPENAPI_API_BASE=your_azure_endpoint
OPENAPI_ENGINE=your_deployment_name
```

## Usage

### Chat Completion

The `chat_completion.py` demonstrates various ways to use the chat completion API with different parameters:
- Temperature control (0 to 2)
- Token limit configuration
- Multiple response generation

```python
from azure_connector import azure_openai_connector

# Simple chat completion
response = azure_openai_connector.send_message(
    messages=[{"role": "user", "content": "Your message"}],
    max_tokens=10,
    temperature=0.7
)
```

### Lyric Completion

The `lyrics_completion.py` shows how to maintain conversation history for contextual responses:
```python
messages = [
    {"role": "system", "content": "You are a lyric completion assistant..."},
    {"role": "user", "content": "Your lyrics..."}
]
response = azure_openai_connector.send_message(
    messages=messages,
    max_tokens=50,
    temperature=0.7
)
```

## Project Structure

- `azure_connector.py`: Core connector class for Azure OpenAI integration
- `chat_completion.py`: Examples of chat completion with different parameters
- `lyrics_completion.py`: Example of maintaining conversation history
- `.env.example`: Template for environment variables
- `requirements.txt`: Project dependencies

## Dependencies

- openai==1.69.0
- python-dotenv==1.1.0 