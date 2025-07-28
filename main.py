import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
load_dotenv()

gemini_api_key= os.getenv("GEMINI_API_KEY")

provider=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)
    
model=OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)
user = input("Please Enter Your Question: ")
agent= Agent(
    name="Greeting Agent",
    instructions="you are a Greeting Agent, your task is to Greet the user with a friendly message, when someone say Hi you hve to reply that Salam from Noureen, when someone says bye then you hve to say Allah Hafiz from Noureen, when someone ask other than greeting then say, Noureen is here just for greeting, i can't answer anything else, I'm sorry Allah Hafiz",
    model=model
)
result = Runner.run_sync(agent, user)
print(result.final_output)
