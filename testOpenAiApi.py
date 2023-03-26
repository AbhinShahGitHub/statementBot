import openai

secrets = {
    "secret_key": "<your key here>"
}

openai.api_key = secrets["secret_key"]
#
# prompt = "Once upon a time"
# model = "gpt-3.5-turbo"
# response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1024)
# print(response["choices"][0]["text"])

model = "gpt-3.5-turbo"  # Or any other model that supports chat

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
]

response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    max_tokens=1024,
)

print(response.choices[0].message['content'])