import openai
from scrape import content

api_key = "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"

openai.api_key = api_key

chatCompletion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Summarize this: {content}"}],
)

print("this is openai:", chatCompletion.choices[0].message.content)
