import requests, bs4, os

def getMetroStatus(metroUrl):
    url=metroUrl
    res = requests.get(metroUrl)
    res.raise_for_status

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    text = soup.find_all(class_= 'views-row')

    for i in text:
        print(i.get_text() + "\n")


    #print(statusElem)


getMetroStatus('https://www.nexus.org.uk/metro/updates')
