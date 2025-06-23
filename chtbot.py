import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def respond(message, history):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=history + [{"role": "user", "content": message}]
        )
        reply = response["choices"][0]["message"]["content"]
        
        # Build the new history
        new_history = history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": reply}
        ]

        # Return for Gradio: [textbox_content, chat_history]
        return "", new_history

    except Exception as e:
        err = f"Error: {str(e)}"
        new_history = history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": err}
        ]
        return "", new_history
