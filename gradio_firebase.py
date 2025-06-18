import os
import gradio as gr
from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain.chat_models import ChatOpenAI

# Load credentials
load_dotenv()

# Firestore setup
PROJECT_ID= "langchain-chatbot-aad4e"
SESSION_ID="new_chat"
COLLECTION_NAME="chat_history"

client = firestore.Client(project=PROJECT_ID)
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)

# LangChain model setup
model = ChatOpenAI(model="gpt-4o-mini")  # or any other model you're using

# Function to use in Gradio
def respond(user_input, history):
    # Add user message to Firestore
    chat_history.add_user_message(user_input)

    # Invoke model with full history from Firestore
    response = model.invoke(chat_history.messages)

    # Add AI message to Firestore
    chat_history.add_ai_message(response.content)

    return response.content

# Load past Firestore messages into UI-compatible format
def get_initial_history():
    history = []
    for msg in chat_history.messages:
        if msg.type == "human":
            history.append((msg.content, None))
        elif msg.type == "ai":
            if history:
                history[-1] = (history[-1][0], msg.content)
            else:
                history.append((None, msg.content))
    return history

# Launch Gradio app
gr.ChatInterface(fn=respond, 
                 chatbot=gr.Chatbot(value=get_initial_history()),
                 title="LangChain Firestore Chatbot").launch()
