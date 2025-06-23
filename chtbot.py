import os
import openai
import gradio as gr
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Respond function for Gradio chatbot
async def respond(message, history):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=history + [{"role": "user", "content": message}]
        )
        reply = response["choices"][0]["message"]["content"]

        # Return two outputs: textbox content, updated chat history
        return "", history + [{"role": "user", "content": message}, {"role": "assistant", "content": reply}]
    
    except Exception as e:
        err = f"Error: {str(e)}"
        return "", history + [{"role": "user", "content": message}, {"role": "assistant", "content": err}]
