from bs4 import BeautifulSoup as bs
from lxml import etree
import requests

#request headers
headers = {'user-agent':"Mozilla/5.0"}
# EX: requests.get([url], headers = headers)

regex_namespace = {'re':'http://exslt.org/regular-expressions'}
## http://exslt.org/regexp/index.html
# EX: root.xpath('//div//a[re:match(@href, ".*entry.*")]'',namespaces= regex_namespace)




def grabMainPage(soup_url):
    pass



def ParseArticle():
    pass
    # when you get a super hyperlinked body of text pass the lxml element
    # in to a soup and let BeautifulSoup parse the text