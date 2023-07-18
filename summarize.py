import openai
from scrape import content
import colorama
from colorama import Fore
from scrape import file_name

api_key = "REPLACE WITH YOUR OWN API KEY"

openai.api_key = api_key

chatCompletion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Summarize this: {content}"}],
)

print(Fore.GREEN + "Summarized Version:", chatCompletion.choices[0].message.content)

with open(f"{file_name}", "a") as f:
    f.write(
        f"""

Summarized Version: {chatCompletion.choices[0].message.content}"""
    )
