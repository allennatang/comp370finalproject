import newsapi as news

posts = news.fetch_latest_news("05f58823626a47728f17c77d33f0e5c5", ["Justin","Trudeau"], 29)

#print(posts["totalResults"])

for i in range(1,100):
    print(posts[i]['title'])
