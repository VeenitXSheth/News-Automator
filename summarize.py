import openai
from scrape import content

api_key = "REPLACE WITH YOUR OWN API KEY"

openai.api_key = api_key

chatCompletion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Summarize this: {content}"}],
)

print("this is openai:", chatCompletion.choices[0].message.content)
