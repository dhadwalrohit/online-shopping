from django.shortcuts import render

# importing api
from newsapi import NewsApiClient

# Create your views here.
def index(request):
	
	newsapi = NewsApiClient(api_key ='1871088eb95a47c19e05040f7fe63d76')
	top = newsapi.get_top_headlines(sources ='techcrunch')

	l = top['articles']
	desc =[]
	news =[]
	img =[]

	for i in range(len(l)):
		f = l[i]
		news.append(f['title'])
		desc.append(f['description'])
		img.append(f['urlToImage'])
	mylist = zip(news, desc, img)

	return render(request, 'news.html', context ={"mylist":mylist})
