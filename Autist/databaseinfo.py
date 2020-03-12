from bs4 import BeautifulSoup
import urllib.request
import re

skin_url = "lolskinlistgenerator.com"

def gather_abilities():
    pass

def gather_champions():
    pass

def gather_skins():
    try:
        skin_page = urllib.request.urlopen(skin_url)
    except:
        print("The url {} could not be accessed".format(skin_url))
    soup = BeautifulSoup(skin_page, 'html.parser')

    regex = re.compile('skinclass')
    content_lis = soup.find_all('li', attrs={'class': regex})
    print(content_lis)

    pass
