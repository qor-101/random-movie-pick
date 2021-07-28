from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from imdb import IMDb
import random
# Create your views here.

def index(request):
    return render(request,"onlypage.html")
    #template = loader.get_template('onlypage.html')
    #return HttpResponse(template.render(request))
def getmov(request):
    ia = IMDb()
    # get a movie
    movie = ia.get_movie(random.randint(1000000,5000000))

    mov_url = ia.get_imdbURL(movie)

    return redirect(mov_url) 
