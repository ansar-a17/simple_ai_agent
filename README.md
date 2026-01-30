# Simple Agent

 I built this to practise the fundamentals of an AI agent, pydantic models, and unit tests. This is a simple AI agent built with Ollama that can perform mathematical operations using tools.

## Features

- **Tool-based Function Calling**: Uses Ollama's function calling capabilities to execute tools when needed
- **Mathematical Operations**: Built-in `add` and `multiply` tools for basic arithmetic
- **Structured Responses**: Uses Pydantic models for consistent output formatting

## Requirements

- Python 3.7+
- Ollama with llama3.1:8b model
- Dependencies listed in `requirements.txt`

## Installation

1. Install Ollama and pull the required model:
   ```bash
   ollama pull llama3.1:8b
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the agent:
```bash
python agent.py
```

The agent will start an interactive chat session where you can:
- Ask mathematical questions (e.g., "what is 5 + 3?", "multiply 10 by 7")
- Have normal conversations
- The agent will automatically use tools when needed for calculations

Example interactions:
```
You: what is 15 + 27?
[using tool: add]
Agent: 15 + 27 equals 42
[Tools used: add]

You: hello, how are you?
[no tool needed]
Agent: I'm doing well, thank you for asking! How can I help you today?
```

## Testing

Run the test suite:
```bash
python test_agent.py
```

or with pytest:
```bash
pytest test_agent.py
```

## Project Structure

- `agent.py` - Main agent implementation with Ollama integration
- `tools.py` - Tool functions (add, multiply)
- `test_agent.py` - Unit tests
- `requirements.txt` - Python dependencies

## How It Works

1. User input is sent to Ollama with available tool definitions
2. The model decides whether to use a tool or respond directly
3. If a tool is needed, it's executed and the result is fed back to the model
4. The final response is structured using a Pydantic schema
5. Conversation history is maintained for context

## License

This project is open source and available for educational purposes.