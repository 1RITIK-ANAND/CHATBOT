import os
import openai
import gradio as gr
from dotenv import load_dotenv

# Load .env variables (for local dev if needed)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Async response function for Gradio
async def respond(message, history):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=history + [{"role": "user", "content": message}]
        )
        reply = response["choices"][0]["message"]["content"]
        return {"role": "assistant", "content": reply}
    except Exception as e:
        return {"role": "assistant", "content": f"Error: {str(e)}"}

# Optional styling (you can delete this if using main.py UI only)
css = """
#chatbox { background-color: black !important; }
.gr-button { background-color: orange !important; color: black !important; }
textarea, input { background-color: #111 !important; color: orange !important; }
"""
