# HuggingFace Integration

This folder contains code for integrating and using HuggingFace's transformers library for text generation tasks.

## Current Implementation

The project currently implements:
- Text generation using the Qwen2.5-0.5B-Instruct model
- Conversation handling with role-based chat history
- Pipeline-based inference

## Installation

1. Follow the installation steps from the [HuggingFace official documentation](https://huggingface.co/docs/transformers/installation)
2. Install required dependencies:
```bash
pip install transformers
```

## Usage

The main conversation script (`conversation.py`) demonstrates how to:
- Load a pre-trained model (Qwen2.5-0.5B-Instruct)
- Set up a text generation pipeline
- Handle conversation history
- Generate responses

Example usage:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Load model and tokenizer
model_name = "Qwen/Qwen2.5-0.5B-Instruct"
model = AutoModelForCausalLM.from_pretrained(model_name, device_map='auto')
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create pipeline
pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer)

# Example conversation
chat_history = [
    {"role": "system", "content": "You are a smart chatbot"},
    {"role": "user", "content": "What is the capital of France?"}
]

# Generate response
outputs = pipe(chat_history, max_new_tokens=512)
```

## Model Details

- **Model**: Qwen2.5-0.5B-Instruct
- **Type**: Instruction-tuned language model
- **Size**: 0.5B parameters
- **Capabilities**: Text generation, conversation, instruction following

## Notes

- The model is loaded with `device_map='auto'` for optimal device placement
- Maximum token generation is set to 512 tokens
- The system uses a role-based conversation format