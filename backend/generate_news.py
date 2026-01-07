import json
import feedparser
from datetime import datetime

SOURCES_FILE = "backend/sources.json"
NEWS_FILE = "backend/news.json"

def load_sources():
    with open(SOURCES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)["sources"]

def load_news():
    try:
        with open(NEWS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_news(news):
    with open(NEWS_FILE, "w", encoding="utf-8") as f:
        json.dump(news, f, ensure_ascii=False, indent=2)

def already_exists(news, title):
    return any(n["title"] == title for n in news)

def generate_note(entry, source):
    now = datetime.now().strftime("%H:%M")
    return {
        "hora": now,
        "title": entry.title,
        "contexto": entry.summary[:400],
        "fuente": source["name"],
        "link": entry.link
    }

def main():
    sources = load_sources()
    news = load_news()

    for source in sources:
        feed = feedparser.parse(source["rss"])
        for entry in feed.entries[:1]:
            if not already_exists(news, entry.title):
                note = generate_note(entry, source)
                news.insert(0, note)
                save_news(news)
                return

if __name__ == "__main__":
    main()