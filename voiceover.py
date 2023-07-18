from gtts import gTTS
from summarize import chatCompletion
from scrape import author
from scrape import file_name
import colorama
from colorama import Fore

content = (
    f"{file_name}. {chatCompletion.choices[0].message.content}. Written by {author} ago"
)

myobj = gTTS(text=content, lang="en", slow=False)
myobj.save(f"{file_name}.mp3")

print(Fore.YELLOW + "Voiceover Saved!")
