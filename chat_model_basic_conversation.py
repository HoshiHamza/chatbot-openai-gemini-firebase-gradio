from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

model=ChatOpenAI(model="gpt-4o-mini",max_tokens=30)

# messages=[
#     SystemMessage(content="Solve the following maths problem"),
#     HumanMessage(content="What is 81 divided by 9?"),
# ]

# result=model.invoke(messages)
# print("Answer from AI: ",result.content)

messages=[
    SystemMessage(content="Solve the following maths problem"),
    HumanMessage(content="What is 81 divided by 9?"),
    AIMessage(content="81 divided by 9 is 9."),
    HumanMessage(content="What is 10 times 5?")
]

result=model.invoke(messages)
print("Answer from AI: ",result.content)
