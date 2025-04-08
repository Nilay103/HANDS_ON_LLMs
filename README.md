# Hands-on LLMs Project

This repository contains implementations and examples of working with different Large Language Model (LLM) services and platforms. The project is structured into three main components, each focusing on a different LLM integration.

## Project Structure

### 1. Azure OpenAI Integration
A comprehensive implementation for integrating with Azure OpenAI services, providing interfaces for chat completions and text generation tasks.

**Key Features:**
- Azure OpenAI service integration with configuration management
- Chat completion examples with various parameters
- Lyric completion demo using conversation history
- Environment variable management for secure configuration

[View Azure OpenAI Documentation](./OpenAI/README.md)

### 2. Hugging Face Integration
Integration with Hugging Face's transformers library and model hub, providing access to a wide range of open-source language models.

[View Hugging Face Documentation](./HuggingFace/README.md)

### 3. MCP (Model Control Panel)
A control panel implementation for managing and interacting with various language models.

[View MCP Documentation](./MCP/README.md)

## Getting Started

Each project has its own setup instructions and dependencies. Please refer to the individual README files in each directory for specific setup and usage instructions.

## Common Requirements

- Python 3.8+
- Virtual environment management
- API keys for respective services (where applicable)

## Repository Structure

```
.
├── OpenAI/          # Azure OpenAI integration
├── HuggingFace/     # Hugging Face models integration
└── MCP/             # Model Control Panel implementation
```

## Contributing

Feel free to contribute to any of the sub-projects by creating pull requests or reporting issues.
