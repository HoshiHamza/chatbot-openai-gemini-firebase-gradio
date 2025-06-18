from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.chat_models import ChatAnthropic
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


load_dotenv()

messages=[
    SystemMessage(content="Solve the following maths problem"),
    HumanMessage(content="What is 81 divided by 9?"),
]

model=ChatGoogleGenerativeAI(model="gemini-1.5-flash")
result=model.invoke(messages)
print(result.content)
