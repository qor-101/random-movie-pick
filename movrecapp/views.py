from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from imdb import IMDb
# Create your views here.

def index(request):
    return render(request,"onlypage.html")
    #template = loader.get_template('onlypage.html')
    #return HttpResponse(template.render(request))
def getmov(request):
    ia = IMDb()
    # get a movie
    movie = ia.search_movie('matrix')

    mov_url = ia.get_imdbURL(movie[0])

    return redirect(mov_url) 
