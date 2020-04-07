import requests
from bs4 import BeautifulSoup

# First Download Coreys Website.
source = requests.get('http://coreyms.com')
coreys_website = source.text

soup = BeautifulSoup(coreys_website, 'lxml')

# Then process it.
for article in soup.find_all('article'):

    # Extract the title and the text
    title = article.h2.text
    print(f"title: \n{title}")
    text = article.find('div', class_="entry-content").text.strip()
    print(f"text: \n{text}")

    # Extract the youtube video id from the link
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0].strip()
        yt_link=f"https://youtube.com/watch?v={vid_id}"

    except TypeError:
        yt_link = None

    print(f"yt_link: \n{yt_link}")
    print('\n')

    # Put the ID back into a standard youtube link.
