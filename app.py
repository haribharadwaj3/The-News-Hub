from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import random

app = Flask(__name__)
ua = UserAgent()

def scrape_headlines(url, headline_tag, headline_class=None, headline_attrs={}):
    """Scrapes headlines from a website.

    Args:
        url: The URL of the website.
        headline_tag: The HTML tag containing the headlines.
        headline_class (optional): The class of the headline tag.
        headline_attrs (optional): Other attributes to filter by.

    Returns:
        A list of headlines or an empty list if an error occurs.
    """
    try:
        headers = {'User-Agent': ua.random}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        if headline_class:
            headlines = soup.find_all(headline_tag, class_=headline_class, attrs=headline_attrs)
        elif headline_attrs:
            headlines = soup.find_all(headline_tag, attrs=headline_attrs)
        else:
            headlines = soup.find_all(headline_tag)

        extracted_headlines = []
        if headlines:
            for headline in headlines:
                text = headline.get_text().strip()
                if text:
                    extracted_headlines.append(text)
        return extracted_headlines

    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return []
    except Exception as e:
        print(f"A general error occurred: {e}")
        return []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/news/<site>')
def show_news(site):
    news_data = {
        'BBC': {
            'url': 'https://www.bbc.com/news',
            'headline_tag': 'h2',
            'headline_class': 'sc-87075214-3'
        },
        'CNN': {
            'url': 'https://edition.cnn.com/',
            'headline_tag': 'span',
            'headline_class': 'container__headline-text'
        },
        'AP': {
            'url': 'https://apnews.com/',
            'headline_tag': 'span',
            'headline_class': 'PagePromoContentIcons-text'
        },
        'TOI': {
            'url': 'https://timesofindia.indiatimes.com/',
            'headline_tag': 'figcaption'
        },
         'NYT': {
            'url': 'https://www.nytimes.com/',
            'headline_tag': 'p',
            'headline_class': 'indicate-hover'
        },
        'HT':{
            'url':'https://www.hindustantimes.com/',
            'headline_tag':'h3',
            'headline_class':'hdg3'
        }
    }

    if site in news_data:
        site_data = news_data[site]
        headlines = scrape_headlines(site_data['url'], site_data['headline_tag'], site_data.get('headline_class'), site_data.get('headline_attrs',{}))
        if site == 'AP' and headlines:
            headlines = headlines[1:]
        return render_template('news.html', headlines=headlines, site=site)
    else:
        return "Invalid news source"

if __name__ == '__main__':
    app.run(debug=True)