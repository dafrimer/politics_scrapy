#EXample API: http://archive.org/wayback/available?url=example.com&timestamp=20060101

import requests
from lxml import etree
import datetime
import boto3
import json
scrape_victims = etree.parse('./scraping_features.xml').getroot()


def getLink(date_query, url_query):
    assert type(date_query) in (datetime.date, datetime.datetime)

    return requests.get('http://archive.org/wayback/available',
                        params={'url':url_query, 'timestamp':date_query.strftime("%Y%m%d")})

def parseURLContent(response):
    pass





i = 0
while i <= 120:
    date_to_search = datetime.date.today() + datetime.timedelta(days=-1 * i)
    for utree in scrape_victims.xpath('/scraperules/news_outlet/url_focus'):
        url_media = utree.text

        res = getLink(date_to_search, url_media)
        d = json.loads(res.content.decode('utf-8'))
        try:
            print(utree.getparent().attrib['name'], d['archived_snapshots']['closest'])
        except KeyError:
            print(utree.text, date_to_search.strftime('%Y-%m-%d'))
    i +=1


