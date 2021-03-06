from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.

def getdata(url):
    r = requests.get(url)
    return r.text

def index(request):

    images =[]

    if request.method == "POST":
        search = request.POST.get('search')
        link = "https://www.google.com/search?tbm=isch&q=" + str(search)
        htmldata = getdata(link)
        soup = BeautifulSoup(htmldata, 'html.parser')
        count = 0
        for item in soup.find_all('img'):
            if item['src'] == 'http://127.0.0.1:8000/images/branding/searchlogo/1x/googlelogo_desk_heirloom_color_150x55dp.gif':
                continue
            print(item['src'])
            images.append(str(item['src']))
            count += 1

        return render(request, 'index.html', {'images':images, 'search':search})
    return render(request, 'index.html', {})