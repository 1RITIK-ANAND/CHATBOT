import gradio as gr
from chtbot import respond

custom_css = """
body {
    background: linear-gradient(120deg, #e0f7fa, #fff);
    font-family: 'Segoe UI', sans-serif;
}
h1 {
    font-weight: 600;
    color: #004d40;
}
.gr-chatbot {
    border: 2px solid #004d40;
    border-radius: 10px;
    background-color: #ffffff;
}
.gr-textbox textarea {
    border: 1px solid #004d40 !important;
}
.gr-button {
    background-color: #00796b !important;
    color: white !important;
    border-radius: 10px;
    font-weight: bold;
}
"""

with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("""
        <h1 style="text-align: center;">🤖 Stylish AI ChatBot</h1>
        <p style="text-align: center;">Powered by OpenAI + Gradio</p>
    """)

    chatbot = gr.Chatbot(
        label="Chat with AI",
        type="messages",
        avatar_images=(
            "https://i.ibb.co/Y73Pz8vF/user-avatar.png",
            "https://i.ibb.co/gbccxFhS/bot-avatar.png"
        )
    )

    with gr.Row():
        msg = gr.Textbox(placeholder="Type your message here...", scale=8, show_label=False)
        clear = gr.Button("🧹 Clear", scale=1)

    state = gr.State([])

    msg.submit(respond, [msg, state], [msg, chatbot])
    clear.click(lambda: ([], ""), None, [chatbot, state])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
