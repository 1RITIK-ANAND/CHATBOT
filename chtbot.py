import os
from openai import OpenAI
import gradio as gr
from dotenv import load_dotenv

load_dotenv()
try:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    client = OpenAI(api_key=api_key)
except Exception as e:
    print(f"Failed to initialize OpenAI client: {str(e)}")
    raise

async def respond(message, history):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=history + [{"role": "user", "content": message}]
        )
        reply = response.choices[0].message.content
        return {"role": "assistant", "content": reply}
    except Exception as e:
        return {"role": "assistant", "content": f"Error: {str(e)}"}

if __name__ == "__main__":
    print("Running chtbot.py directly (not used in Render)")
    with gr.Blocks() as app:
        gr.Markdown("# Test Chatbot")
        chat_interface = gr.ChatInterface(fn=respond, type="messages")
    app.launch()
