from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI


load_dotenv()

model=ChatOpenAI(model="gpt-4o-mini",max_tokens=30)

result=model.invoke("what is 81 divided by 9")

print("Full result",result)

print(result.content)






