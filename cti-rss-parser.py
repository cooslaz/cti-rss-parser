import feedparser

cti_rss_url = "http://www.XXX.com/cti/feed.xml"
cti_feed = feedparser.parse(cti_rss_url)

for entry in cti_feed.entries:
    print("Threat Title:", entry.title)
    print("Threat Description:", entry.description)
    print("Threat URL:", entry.link)
    print()
