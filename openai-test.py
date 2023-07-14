import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
print(f"OpenAI API key: {openai.api_key}")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "stet by step guide in detail on loading task definitions to aws ecs cluster"}
  ]
)

print(completion.choices[0].message)
