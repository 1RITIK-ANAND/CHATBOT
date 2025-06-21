import os
from openai import OpenAI
import gradio as gr
from dotenv import load_dotenv

load_dotenv()
try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
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

css = """
#chatbox { background-color: black !important; }
.gr-button { background-color: orange !important; color: black !important; }
textarea, input { background-color: #111 !important; color: orange !important; }
"""

with gr.Blocks(css=css) as app:
    gr.Markdown("## 🤖 <span style='color:orange;'>AI Chatbot Powered by OpenAI</span>")
    chat_interface = gr.ChatInterface(
        fn=respond,
        chatbot=gr.Chatbot(elem_id="chtbox"),
        title=None,
        theme="default",
        type="messages"
    )

if __name__ == "__main__":
    print("Running chtbot.py directly (not used in Render)")
    app.launch()
