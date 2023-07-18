<h1 align="center">News Automator</h1>

A simple web-scraper and AI system to summarize tech news into super small, digestible bits for reading, listening, or micro-blogging!
News Automator can give you a random piece of tech news at a single command and provide a summary, mp3 file, and all original article sources!
For installation instructions, read below:

## How To Install

### Step One

First, fork this GitHub repository on your own account by clicking the 'Fork' button at the top of this page. From there, clone the repository from your own account to your local machine by using
the 'git clone' command followed the repository link:

'git clone https://github.com/YOUR_ACCOUNT/News-Automator'

### Step Two

Open the folder on your preferred code editor of choice and make sure you have Python 3 installed on your machine. If not, visit [python.org/install](https://www.python.org/downloads/).
Now open the terminal at the destination of the folder or by using the integrated terminal in your code editor or IDE if provided. Run 'pip install requests bs4 openai gTTS' to install all the
project dependencies. 

### Step Three

Visit the 'summarize.py' file and in line 4, replace the string with your own OpenAI API key. If you don't have an API key, visit [openai.com](https://openai.com) and create a free account.
From there, select 'API' when prompted with 3 options. Then click your account icon in the top-right corner and click 'View API Keys'. Click on 'Create new secret key' and copy and paste the 
generated API key into your project.

(MAKE SURE THIS DOES NOT GET SHOWN TO THE PUBLIC)

### Step Four

Once everything has been configured, you can finally run the script. There are 2 options for how to run the script depending on what you would like to be produced. If you just want a
short text summary with the article URL, title, author, and date published printed to the terminal, run 'python3 summarize.py'. You will see the article content, title, author, publishing date, 
and summarized version from OpenAI printed to the terminal.

If you would also like to get an mp3 file reading out the summarized news article, run 'python3 voiceover.py' instead. You will get all previous information plus an mp3 file with the title of
the article that was summarized added to the project folder root. 

### Step Five

If any issues arise with the project, please create a new GitHub issue on this repository and I will try to get it fixed as soon as I can! This project isn't open to any contributions currently
but feel free to fork the project and make any tweaks you would like! Please just give credit to this repository or to my GitHub profile as the original creator of the base project! Thanks!

## Features

### Web-Scraping

This project can scrape and entire tech news article and get the article content, title, author, the date it was published, and the URL it scraped it from. It uses the Python 'requests' module
to accomplish this along with 'bs4' or 'BeautifulSoup' to parse through the HTML content of the webpage.

### Summarization

The script can also use the powers of GPT from OpenAI to give you a quick and short summarized version of the scraped article for easy reading. It does this using the 'openai' Python library
and given you have an OpenAI API key.

### Voiceovers

It can also produce a voiceover of the summarized article that GPT provides in an mp3 file format. It does this using 'gTTS' or 'Google Text To Speech' using the provided Python package from
Google. Using this, it can provide a high-quality mp3 file without any hassle so you can listen to your tech news on the go!

## Thanks for checking News Automator out!
