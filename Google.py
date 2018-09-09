import requests
import webbrowser
import sys
from bs4 import BeautifulSoup
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"
url = 'https://www.google.com/search'

def google():
    global Q
    print("Search or input website(Press ctrl-c to exit):", end='\n--->', flush=True)
    try:
        Q = input()
    except KeyboardInterrupt:
        print('')
        sys.exit()
    if Q.split('.')[0]=='www' or Q.split('.')[0]=='https://www' or Q.split('.')[0]=='http://www':
        print('Opening website')
        return None
    print('')
    data = {'q': Q}
    soup = requests.get(url, data, headers=headers)
    soup = BeautifulSoup(soup.text, "lxml")
    return soup


while True:
    soup = google()
    a = 1
    sugs = []
    if soup==None:
       webbrowser.open_new_tab(Q) 
       continue
    for link in soup.find_all('h3', 'r'):
        temp = link.find('a')
        print(a, temp.text)
        sugs.append(temp['href'])
        a += 1
    while True:
        try:
            Choose = input('Choose one:')
            Choose = int(Choose) - 1
        except (KeyboardInterrupt, ValueError):
            print('')
            break
        webbrowser.open_new_tab(sugs[Choose])
