import os
from langchain_openai import ChatOpenAI

assert os.environ.get("OPENAI_API_KEY") is not None

print(ChatOpenAI(model="gpt-4.1").invoke("Convert the given Celsius temperature to Fahrenheit: "+input("Enter degrees Celsius: ")))