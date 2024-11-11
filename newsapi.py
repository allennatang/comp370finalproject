import requests
import json
from datetime import datetime, timedelta, date

def fetch_latest_news(api_key, news_keywords, lookback_days=10):
    
    if news_keywords == []:
        raise ValueError("Keywords must be provided")

    q = ""
    for keyword in news_keywords:
        if not(keyword.isalpha()):
            raise ValueError("Keyword must be alphabetic")
        q += (str(keyword) + " AND ")
    q = q[:-3]

    url = "https://newsapi.org/v2/everything?q=" + q + "&language=en" + "&from=" + str((date.today() - timedelta(days=lookback_days))) + "&to=" + str(date.today()) + "&apiKey=" + api_key 
    response = requests.get(url)
    posts = response.json().get("articles",[])
    #posts = response.json() 
    
    return posts
