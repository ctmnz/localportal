from flask import Flask
import datetime
import json
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

def get_news(url):
    result = ""
    hnews_page = requests.get(url)
    hnews_page_html = BeautifulSoup(hnews_page.text, 'html.parser')
    hnews_table = hnews_page_html.find('table', attrs={'class':'itemlist'})
    for link in hnews_table.find_all('a'):
        if link.get('href').startswith('http') and link.text:
            link_href = link.get('href')
            link_text = link.text
            result += "<a href='{}'> {} </a> <br>".format(link_href, link_text)
    return result

@app.route("/")
def home():
    result = """
<html>
<head>
	<title> Local portal</title>
</head>
<body>

<h1> Point of interest </h1>
<ul>
	<li> <a href="/news.html">Hacker news </a> </li>
</ul>

</body>
    """
    return result


@app.route("/hello")
def hello():
    result = {}
    result['datetime'] = "{}".format(datetime.datetime.now())
    result['message'] = "Hello There!"
    r = json.dumps(result)
    return r

@app.route("/news")
def news():
    result = {}

    news_hackernews = {}
    news_count = 1
    hackernews_request = requests.get("https://news.ycombinator.com/")
    html_hackernews = BeautifulSoup(hackernews_request.text, 'html.parser')
    for link in html_hackernews.find_all('a'):
        if link.get('href').startswith('http'):
            link_href = link.get('href')
            link_text = link.text
            news_hackernews[news_count] = {"href":link_href, "text":link_text}
            news_count += 1
    result['hackernews'] = news_hackernews
    
    r = json.dumps(result)
    return r

@app.route("/news.html")
def newshtml():
    result = """
<html><head><title>Hackernews</title></head><body style="font-size: 19px; margin: 25px;">
"""
    result += get_news("https://news.ycombinator.com/")
    result += get_news("https://news.ycombinator.com/news?p=2")
    result += get_news("https://news.ycombinator.com/news?p=3")
    result += "</body></html>"
    return result

