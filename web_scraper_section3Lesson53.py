import urllib.request
from bs4 import BeautifulSoup

class Scraper:

    def __init__(self,site):
        self.site = site #take the website you want to scrape as a parameter

    def scrape(self):
        # the function urlopen from python built-in module urllib makes a request to a website and returns a response object with it's html and some aditional data
        response = urllib.request.urlopen(self.site)
        
        # call read on the response object, to get the website html
        html = response.read()
        
        # once the html is "collected" we need to parse it.
        parser = "html.parser"
        # The BeautifulSoup class, takes 2 parameters, the html we want to parse, and the string "html,parser" which lets the class know we are parsing html format, we instantiate the 'sp' object with those parameters
        sp = BeautifulSoup(html, parser)

        # Now we can use sp object "find_all" function to search the website html for the tag "a" (anchor). It returns a list of the matching tags it found. We iterate through this list of 'tag' objects and get the url
        # from each tag calling the '.get' function on every item of the list (passing the href property of anchor tag, as a parameter)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            print("\n" + url)


scrape = Scraper("http://www.xataca.com")
scrape.scrape()

