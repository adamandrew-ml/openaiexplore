# source env/bin/activate
# pip install -r requirements.txt
# echo "export OPENAI_API_KEY='yourkey'" >> ~/.zshrc

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

gpt_prompt = "Tell me an interesting fact about Aston Villa"

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=gpt_prompt,
  temperature=0.01,
  max_tokens=256,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response['choices'][0]['text'])