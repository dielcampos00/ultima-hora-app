import feedparser
import json
from datetime import datetime

# FUENTES RSS (puedes agregar más después)
SOURCES = [
    {
        "name": "BBC World",
        "url": "https://feeds.bbci.co.uk/news/world/rss.xml"
    },
    {
        "name": "CNN World",
        "url": "http://rss.cnn.com/rss/edition_world.rss"
    }
]

news = []

for source in SOURCES:
    feed = feedparser.parse(source["url"])
    if feed.entries:
        entry = feed.entries[0]

        hora_actual = datetime.utcnow().strftime("%H:%M UTC")

        noticia = {
            "hora": hora_actual,
            "title": entry.title,
            "contexto": entry.summary if "summary" in entry else "",
            "fuente": source["name"],
            "link": entry.link
        }

        news.append(noticia)

# Guardar en JSON
with open("backend/news.json", "w", encoding="utf-8") as f:
    json.dump(news, f, ensure_ascii=False, indent=2)

print("Noticias actualizadas correctamente")