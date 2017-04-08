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
GO_BACK_DAYS = 100
GO_BACK_YEARS = 8
while i <= GO_BACK_DAYS:
    date_to_search = datetime.date.today() + datetime.timedelta(days=-1 * i)
    temp_timestamp = datetime.datetime.today().timestamp()

    for utree in scrape_victims.xpath('/scraperules/news_outlet/url_focus'):
        url_media = utree.text

        res = getLink(date_to_search, url_media)


        d = json.loads(res.content.decode('utf-8'))

        if int(d['archived_snapshots']['closest']['timestamp']) >= temp_timestamp:
            continue
        else:
            temp_timestamp = d['archived_snapshots']['closest']['timestamp']

        try:

            utree.getparent().attrib['name'], d['archived_snapshots']['closest']
        except KeyError:
            print(utree.text, date_to_search.strftime('%Y-%m-%d'))
    i +=1


