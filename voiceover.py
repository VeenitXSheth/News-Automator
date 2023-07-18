from gtts import gTTS
from summarize import chatCompletion
from scrape import articleTitle
from scrape import articleAuthor

content = f"{articleTitle}. {chatCompletion.choices[0].message.content}. Written by {articleAuthor}"

myobj = gTTS(text=content, lang="en", slow=False)
myobj.save(f"{articleTitle}.mp3")

# Issue with reciting author's name; it will add in random letters and symbols between characters; Fix will be added at some point
