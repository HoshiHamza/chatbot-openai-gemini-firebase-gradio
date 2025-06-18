from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

model=ChatOpenAI(model="gpt-4o-mini")

chat_history=[]

system_message=SystemMessage(content="You are a helpful AI Assistant")

chat_history.append(system_message)

while True:
    query=input("You: ")
    if query.lower()== "quit":
        break
    chat_history.append(HumanMessage(content=query))

    result=model.invoke(chat_history)
    response=result.content
    chat_history.append(AIMessage(content=response))

    print("AI: ", response)

print("Message History: ",chat_history)
