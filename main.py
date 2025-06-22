import gradio as gr
import os
from chtbot import respond

def test_respond(message):
    """Test function to ensure respond works without UI issues."""
    try:
        history = [{"role": "user", "content": message}]
        result = respond(message, history)
        return result["content"]
    except Exception as e:
        return f"Error in test_respond: {str(e)}"

try:
    demo = gr.Interface(
        fn=test_respond,
        inputs="text",
        outputs="text",
        title="Minimal AI Chatbot",
        description="Test deployment on Render"
    )

    if __name__ == "__main__":
        port = int(os.environ.get("PORT", 7860))
        print(f"Attempting to start Gradio server on 0.0.0.0:{port}")
        demo.launch(server_name="0.0.0.0", server_port=port, share=False, debug=True, show_error=True)
except Exception as e:
    print(f"Failed to start Gradio server: {str(e)}")
    raise
