# import gradio as gr
# from langchain.chat_models import ChatOpenAI
# from langchain_google_firestore import FirestoreChatMessageHistory
# from google.cloud import firestore
# from dotenv import load_dotenv
# import os
# from gradio.components import Dropdown

# load_dotenv()

# PROJECT_ID = "langchain-chatbot-aad4e"
# COLLECTION_NAME = "chat_history"

# client = firestore.Client(project=PROJECT_ID)
# model = ChatOpenAI(model="gpt-4o-mini")

# # Helper to get session list from Firestore
# def get_session_ids():
#     collection_ref = client.collection(COLLECTION_NAME)
#     docs = collection_ref.stream()
#     return sorted(set(doc.id for doc in docs))

# # Init session and return empty chat
# def start_new_chat(session_id):
#     global chat_history
#     chat_history = FirestoreChatMessageHistory(
#         session_id=session_id,
#         collection=COLLECTION_NAME,
#         client=client
#     )
#     updated_sessions = get_session_ids()
#     return [], session_id, Dropdown.update(choices=updated_sessions, value=session_id)

# # Continue existing session
# def load_chat(session_id):
#     global chat_history
#     chat_history = FirestoreChatMessageHistory(
#         session_id=session_id,
#         collection=COLLECTION_NAME,
#         client=client
#     )
#     history = []
#     for msg in chat_history.messages:
#         if msg.type == "human":
#             history.append((msg.content, None))
#         elif msg.type == "ai" and history:
#             history[-1] = (history[-1][0], msg.content)
#     return history

# # Handle user message
# def chat(user_input, history_display):
#     chat_history.add_user_message(user_input)
#     response = model.invoke(chat_history.messages)
#     chat_history.add_ai_message(response.content)
#     history_display.append((user_input, response.content))
#     return history_display

# # UI layout
# with gr.Blocks(theme="soft") as demo:
#     with gr.Row():
#         with gr.Column(scale=1):
#             gr.Markdown("### 💬 Chat Sessions")

#             session_id_box = gr.Textbox(label="New Session ID")
#             new_chat_btn = gr.Button("➕ Start New Chat")
#             old_sessions = gr.Dropdown(label="Load Previous Chat", choices=get_session_ids())
#             load_chat_btn = gr.Button("📂 Load Selected Chat")

#         with gr.Column(scale=4):
#             chatbot = gr.Chatbot(label="Chat with AI", height=500)
#             msg = gr.Textbox(label="Your message", placeholder="Type and press Enter")
#             send = gr.Button("Send")

#     # Events
#     new_chat_btn.click(start_new_chat, inputs=[session_id_box], outputs=[chatbot, session_id_box, old_sessions])
#     load_chat_btn.click(load_chat, inputs=[old_sessions], outputs=chatbot)
#     send.click(chat, inputs=[msg, chatbot], outputs=[chatbot])
#     msg.submit(chat, inputs=[msg, chatbot], outputs=[chatbot])

# demo.launch()


# import gradio as gr
# from langchain.chat_models import ChatOpenAI
# from langchain_google_firestore import FirestoreChatMessageHistory
# from google.cloud import firestore
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()

# # Firestore project setup
# PROJECT_ID = "langchain-chatbot-aad4e"
# COLLECTION_NAME = "chat_history"

# # Firestore client and model
# client = firestore.Client(project=PROJECT_ID)
# model = ChatOpenAI(model="gpt-4o-mini")

# # 🔁 Fetch list of all session IDs from Firestore
# def get_session_ids():
#     collection_ref = client.collection(COLLECTION_NAME)
#     docs = collection_ref.stream()
#     return sorted(set(doc.id for doc in docs))

# # 🆕 Start a new chat session
# def start_new_chat(session_id):
#     global chat_history
#     chat_history = FirestoreChatMessageHistory(
#         session_id=session_id,
#         collection=COLLECTION_NAME,
#         client=client
#     )
#     return [], session_id

# # 📂 Load an existing session from Firestore
# def load_chat(session_id):
#     global chat_history
#     chat_history = FirestoreChatMessageHistory(
#         session_id=session_id,
#         collection=COLLECTION_NAME,
#         client=client
#     )
#     history = []
#     for msg in chat_history.messages:
#         if msg.type == "human":
#             history.append((msg.content, None))
#         elif msg.type == "ai" and history:
#             history[-1] = (history[-1][0], msg.content)
#     return history

# # 💬 Handle user input and generate AI response
# def chat(user_input, history_display):
#     chat_history.add_user_message(user_input)
#     response = model.invoke(chat_history.messages)
#     chat_history.add_ai_message(response.content)
#     history_display.append((user_input, response.content))
#     return history_display

# # 🔄 Refresh dropdown choices manually
# def refresh_sessions():
#     return gr.update(choices=get_session_ids())

# # UI layout
# with gr.Blocks(theme="soft") as demo:
#     with gr.Row():
#         with gr.Column(scale=1):
#             gr.Markdown("### 💬 Chat Sessions")

#             session_id_box = gr.Textbox(label="New Session ID")
#             new_chat_btn = gr.Button("➕ Start New Chat")

#             old_sessions = gr.Dropdown(label="Load Previous Chat", choices=get_session_ids())
#             refresh_btn = gr.Button("🔄 Refresh Chat List")  # NEW BUTTON
#             load_chat_btn = gr.Button("📂 Load Selected Chat")

#         with gr.Column(scale=4):
#             chatbot = gr.Chatbot(label="Chat with AI", height=500)
#             msg = gr.Textbox(label="Your message", placeholder="Type and press Enter")
#             send = gr.Button("Send")

#     # Event bindings
#     new_chat_btn.click(start_new_chat, inputs=[session_id_box], outputs=[chatbot, session_id_box])
#     load_chat_btn.click(load_chat, inputs=[old_sessions], outputs=chatbot)
#     send.click(chat, inputs=[msg, chatbot], outputs=[chatbot])
#     msg.submit(chat, inputs=[msg, chatbot], outputs=[chatbot])
#     refresh_btn.click(refresh_sessions, outputs=old_sessions)  # Bind refresh

# demo.launch()


import gradio as gr

from langchain_openai import ChatOpenAI
from langchain_google_firestore import FirestoreChatMessageHistory
from google.cloud import firestore
from dotenv import load_dotenv
import os


load_dotenv()

PROJECT_ID = "langchain-chatbot-aad4e"
COLLECTION_NAME = "chat_history"

client = firestore.Client(project=PROJECT_ID)
model = ChatOpenAI(model="gpt-4o-mini")
chat_history = None

# Get session list from Firestore
def get_session_ids():
    collection_ref = client.collection(COLLECTION_NAME)
    docs = collection_ref.stream()
    return sorted(set(doc.id for doc in docs))


# Start a new session
def start_new_chat(session_id):
    global chat_history
    # Initialize chat history
    chat_history = FirestoreChatMessageHistory(
        session_id=session_id,
        collection=COLLECTION_NAME,
        client=client
    )
    
    # Create the document in Firestore explicitly
    doc_ref = client.collection(COLLECTION_NAME).document(session_id)
    doc_ref.set({'created': firestore.SERVER_TIMESTAMP})
    
    # Get updated session list AFTER creating the document
    updated_sessions = get_session_ids()
    
    # Make sure the new session is in the list
    if session_id not in updated_sessions:
        updated_sessions.append(session_id)
        updated_sessions.sort()
    
    return [], "", gr.update(choices=updated_sessions, value=session_id)


# Load an existing chat session
def load_chat(session_id):
    global chat_history
    chat_history = FirestoreChatMessageHistory(
        session_id=session_id,
        collection=COLLECTION_NAME,
        client=client
    )
    history = []
    for msg in chat_history.messages:
        if msg.type == "human":
            history.append((msg.content, None))
        elif msg.type == "ai" and history:
            history[-1] = (history[-1][0], msg.content)
    return history


# Handle chatting
def chat(user_input, history_display):
    chat_history.add_user_message(user_input) # type: ignore
    response = model.invoke(chat_history.messages) # type: ignore
    chat_history.add_ai_message(response.content) # type: ignore
    history_display.append((user_input, response.content))
    return history_display, ""  # Return empty string to clear input


# Build Gradio UI
with gr.Blocks(css=".gradio-container {height: 100vh !important;} .chatbot {height: 100% !important;}") as demo:
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 💬 Chat Sessions")

            session_id_box = gr.Textbox(label="New Session ID", placeholder="Enter a new session ID")
            new_chat_btn = gr.Button("➕ Start New Chat")

            chat_sessions = gr.Dropdown(choices=get_session_ids(), label="Previous Chats", interactive=True)

        with gr.Column(scale=4):
            chatbot = gr.Chatbot(label="Chat with AI", height=500)
            msg = gr.Textbox(
                label="Your message",
                placeholder="Type your message here...",
                show_label=False
            )
            msg.submit(
                chat, 
                inputs=[msg, chatbot], 
                outputs=[chatbot, msg]
            )

    # Bind events
    new_chat_btn.click(
        start_new_chat, 
        inputs=[session_id_box], 
        outputs=[chatbot, session_id_box, chat_sessions]
    )
    chat_sessions.change(load_chat, inputs=chat_sessions, outputs=chatbot)

demo.launch(server_name="0.0.0.0", server_port=8080)
