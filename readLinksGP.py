from lxml import html
from numpy import real
import requests


def raceresult():
    url = 'https://www.formula1.com/en/results.html/2022/races/race-result.html'
    F1URL = 'https://www.formula1.com'

    AY = '2022'

    page = requests.get(url)
    webpage = html.fromstring(page.content)

    page = webpage.xpath('//a/@href',first=True)

    #print(ls)

    namesGP = ['bahrain','italy','australia','miami','portugal','spain','monaco','azerbaijan','france','austria','great-britain','hungary','belgium','netherlands','russia','turkey','united-states','mexico','brazil','qatar','saudi-arabia','abu-dhabi']

    def noresult(PREFIX,sufix):
        from requests_html import HTMLSession

        session = HTMLSession()
        try:
            r = session.get(PREFIX+sufix)

            noresults = r.html.find("main",first=True)

            txtNoresults = noresults.find(".no-results",first=True).text

            if "no results".upper() in txtNoresults.upper():
                x = False
                return x
            else:
                pass
        except AttributeError:
            pass
        except Exception as e:
            print(e)

    oldLinks = []
    for p in page:
        for n in namesGP:
            if n in p and  AY in p:
                oldLinks.append(p)
            else:
                pass

    links = list(set(oldLinks))


    activeLinks = []

    for l in links:
        x = noresult(F1URL,l)
        if x == False:
            pass
        else:
            noresult(F1URL,l)
            activeLinks.append(F1URL+l)

    activelinks = activeLinks
    return activelinks