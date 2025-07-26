import os
from langchain_community.utilities import SearchApiAPIWrapper
from langchain_core.tools import Tool
from langchain_openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

#using the api keys
api_key = os.getenv("SEARCHAPI_API_KEY")
api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0)
search = SearchApiAPIWrapper()

result = search.run("Empstein's first name?")

print(result)

tools = [
    Tool(
        name="intermediate_answer",
        func=search.run,
        description="useful for when you need to ask with search",
    )
]

print(tools)