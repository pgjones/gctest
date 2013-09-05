import urllib2
import json
from dateutil import parser

from gctest.models import News

def pull_feed():
    feed = json.load(urllib2.urlopen("https://www.facebook.com/feeds/page.php?format=json&id=183540721656189"))
    print feed["updated"]
    if News.objects.count() > 0:
        latest = News.objects.order_by('-updated')[:1]
        if parser.parse(feed["updated"]) < latest[0].updated:
            return # Up to date
    for entry in feed["entries"]:
        print entry["title"]
        updated_time = parser.parse(entry["updated"])
        news = News(title=entry["title"], updated=updated_time, link=entry["alternate"])
        news.save()
        
