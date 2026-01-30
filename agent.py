from tools import add, multiply
import ollama
import json
from pydantic import BaseModel, Field

class Response(BaseModel):
    text: str = Field(description="the main response text")
    tools_used: str = Field(description="names of the tools used")


tools = [
    {
        "type": "function",
        "function": {
            "name": "add",
            "description": "Add two numbers together. ONLY use this when the user explicitly asks to add, sum, or calculate the total of two specific numbers. Do NOT use for general conversation.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "The first number to add"},
                    "b": {"type": "number", "description": "The second number to add"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "multiply",
            "description": "Multiply two numbers together. ONLY use this when the user explicitly asks to multiply, times, or calculate the product of two specific numbers. Do NOT use for general conversation.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "The first number to multiply"},
                    "b": {"type": "number", "description": "The second number to multiply"}
                },
                "required": ["a", "b"]
            }
        }
    }
]


messages = [
    {"role": "system", "content": "You are a helpful assistant. You have access to two tools: 'add' for addition and 'multiply' for multiplication. ONLY call these tools when the user explicitly asks for mathematical operations (e.g., 'what is 5 + 3?', 'multiply 4 by 7', '10 times 2'). For normal conversation, greetings, questions, or any non-mathematical requests, respond directly WITHOUT using any tools. Be conversational and friendly, but never use tools unless the user clearly needs a mathematical operation."}
]
if __name__ == '__main__':
    while True:
        user_input = input("\nYou: ")
        messages.append({"role": "user", "content": user_input})

        response = ollama.chat(
            model="llama3.1:8b",
            messages=messages,
            tools=tools
        )

        message = response["message"]

        if message.get("tool_calls"):
            print(f"[using tool: {message["tool_calls"][0]["function"]["name"]}]")
            tool_call = message["tool_calls"][0]
            tool_name = tool_call["function"]["name"]
            args = tool_call["function"]["arguments"]
            if isinstance(args, str):
                args = json.loads(args)

            if tool_name == "add":
                result = add(**args)
            elif tool_name == "multiply":
                result = multiply(**args)

            messages.append(message)
            messages.append({
                "role": "tool",
                "tool_name": tool_name,
                "content": str(result)
            })

            final_response = ollama.chat(
                model="llama3.1:8b",
                messages=messages,
                format=Response.model_json_schema()
            )

            response_data = json.loads(final_response["message"]["content"])
            print("Agent:", response_data["text"])
            print(f"[Tools used: {response_data['tools_used']}]")
            messages.append(final_response["message"])

        else:
            print("[no tool needed]")
            
            formatted_response = ollama.chat(
                model="llama3.1:8b",
                messages=messages,
                format=Response.model_json_schema()
            )
            
            response_data = json.loads(formatted_response["message"]["content"])
            print("Agent:", response_data["text"])
            messages.append(formatted_response["message"])
