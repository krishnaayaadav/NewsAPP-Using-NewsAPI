from django.shortcuts import render
from .newsapi import NewAppAPI
from django.views import View
from django.core.paginator import Paginator


# endpoint here
URL = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey='

# apikey
apikey = '<your_api_key_here>'


newapi = NewAppAPI(url=URL, apikey=apikey, file_name='allnews.dat', mode='ab+')
headlines = newapi.get_top_headlines()


class HomepageView(View):

    def get(self, request):
        # dict_keys(['source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'content'])
        p = Paginator(headlines, 14)
        page_num = request.GET.get('page')
        page_obj = p.get_page(page_num)

        context = {
            'headlines': page_obj
        }
        return render(request, 'home.html',context )


class Homepage2(View):

    def get(self, request):
        # dict_keys(['source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'content'])
        p = Paginator(headlines, 35)
        page_num = request.GET.get('page')
        page_obj = p.get_page(page_num)

        context = {
            'headlines': page_obj
        }
        return render(request, 'home2.html',context )

