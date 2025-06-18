from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI


load_dotenv()

PROJECT_ID= "langchain-chatbot-aad4e"
SESSION_ID="new_chat"
COLLECTION_NAME="chat_history"

print("initializing firestore client..")
client=firestore.Client(project=PROJECT_ID)

chat_history= FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)


print("Current Chat History:" , chat_history.messages)

model=ChatOpenAI(model="gpt-4o-mini")

print("Start chatting with the AI. Type 'exit' to quit")

while True:
    human_input=input("You: ")
    if human_input.lower()== "exit":
        break
    chat_history.add_user_message(human_input)

    ai_response=model.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)

    print("AI: ", ai_response.content)

# print("Message History: ",chat_history)
# import os
# from google.cloud import firestore

# # Ensure this environment variable is set before running
# print("GOOGLE_APPLICATION_CREDENTIALS:", os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))

# client = firestore.Client(project="langchain-chatbot-aad4e")

# doc_ref = client.collection("chat_history").document("test_doc")
# doc_ref.set({"message": "Hello Firestore"})
# print(doc_ref.get().to_dict())