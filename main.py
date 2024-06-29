import tkinter as tk
from tkinter import scrolledtext
import feedparser


RSS_FEEDS = {
    'Technology': 'http://feeds.bbci.co.uk/news/technology/rss.xml',
    'Sports': 'http://feeds.bbci.co.uk/sport/rss.xml',
    'World': 'http://feeds.bbci.co.uk/news/world/rss.xml',
    'Business': 'http://feeds.bbci.co.uk/news/business/rss.xml',
}


def fetch_news(category):
    news_feed = feedparser.parse(RSS_FEEDS[category])
    articles = news_feed.entries

    news_display.delete(1.0, tk.END)
    news_display.insert(tk.INSERT, f"Top news in {category}:\n\n")

    for article in articles[:10]:
        title = article.title
        link = article.link
        summary = article.summary

        news_display.insert(tk.INSERT, f"Title: {title}\n")
        news_display.insert(tk.INSERT, f"Link: {link}\n")
        news_display.insert(tk.INSERT, f"Summary: {summary}\n\n")


root = tk.Tk()
root.title("Personalized News Aggregator")


category_var = tk.StringVar(root)
category_var.set('Technology')
categories = list(RSS_FEEDS.keys())
category_menu = tk.OptionMenu(root, category_var, *categories)
category_menu.pack(pady=10)


fetch_button = tk.Button(root, text="Fetch News", command=lambda: fetch_news(category_var.get()))
fetch_button.pack(pady=10)


news_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
news_display.pack(pady=10)


root.mainloop()
