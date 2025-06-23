import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# history format: list of [user, assistant] pairs
async def respond(message, history):
    try:
        # Convert Gradio history (list of [user, assistant]) to OpenAI format
        messages = []
        for user_msg, assistant_msg in history:
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": assistant_msg})

        # Add latest user message
        messages.append({"role": "user", "content": message})

        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = response["choices"][0]["message"]["content"]

        # Append to history as a [user, assistant] pair
        return "", history + [[message, reply]]

    except Exception as e:
        err = f"Error: {str(e)}"
        return "", history + [[message, err]]
