  import openai
  import os

  query = "give me  a chord progression that is sad with this synth soudn."

  openai.api_base = "https://api.endpoints.anyscale.com/v1"

  chat_completion = openai.ChatCompletion.create(
      model="codellama/CodeLlama-34b-Instruct-hf",
      messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": query}],
      temperature=0.1,
      stream=True
  )
  for message in chat_completion:
      message = message["choices"][0]["delta"]
      if "content" in message:
          print(message["content"], end="", flush=True)
