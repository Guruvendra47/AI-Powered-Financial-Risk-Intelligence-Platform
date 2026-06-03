from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="Hello World"
)

print("Success")
print(len(response.data[0].embedding))