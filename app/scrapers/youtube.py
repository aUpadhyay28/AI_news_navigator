import feedparser

def fetch_ai_news(limit=5):
    feed = feedparser.parse("https://news.google.com/rss/search?q=AI")

    articles = []

    for entry in feed.entries[:limit]:
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "content": entry.get("summary", entry.title),  # better than just title
            "published": entry.get("published", "")
        })

    return articles