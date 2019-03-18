import requests
import asyncio
from bs4 import BeautifulSoup as BSHTML
import json

def get_html(url):
    html = requests.get(url)
    return html.text

def prepare_text(htmlText):
    soup = BSHTML(htmlText, features="html5lib")
    [x.extract() for x in soup("script")]
    [x.extract() for x in soup("style")]
    text = soup.get_text()
    return text 

def prepare_img(htmlText):   
    soup = BSHTML(htmlText, features="html5lib")
    images = soup.findAll('img')
    img_urls = [x['src'] for x in images]
    return json.dumps(img_urls)

async def text_worker(url):
    htmlText = get_html(url)
    return prepare_text(htmlText)

async def img_worker(url):
    htmlText = get_html(url)
    return prepare_img(htmlText)