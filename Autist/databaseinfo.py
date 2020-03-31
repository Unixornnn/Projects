from bs4 import BeautifulSoup
import urllib.request
import requests

skin_url = "lolskinlistgenerator.com"

def gather_abilities():
    pass

def gather_champions():
    pass

def gather_skins():
    try:
        skin_page = get(skin_url)
    except:
        print("The url {} could not be accessed".format(skin_url))
    soup = BeautifulSoup(skin_page, 'html.parser')
    skin_containers = soup.find_all('div',class_ = 'champ-skins champ-skins--cards')
    for i in skin_containers:
        i.a.

    pass
