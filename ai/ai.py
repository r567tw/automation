import openai

openai.api_key = ""
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="什麼是AI",
  temperature=0.9,
  max_tokens=200,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)
print(response["choices"][0]["text"])