#! /usr/bin/env python3
#This program takes an argument, the url to scrape for receipes
import bs4, requests, sys

url = 'https://my.forksmealplanner.com/#!/archive'
MENU_LINK = 'h3.ng-binding'

#If a url is passed, use it, otherwise use demo url
if len(sys.argv) > 1:
    url = sys.argv[1]

#Get the urls for the menus
def getMenuPages(pageUrl):
    res = requests.get(pageUrl)
    res.raise_for_status()

    #parse the html
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select(MENU_LINK)

    return elems[0].text

menuLinks = getMenuPages(url)
print('These are the menus ' + menuLinks)
