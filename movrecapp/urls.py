from django.urls import path
from . import views

urlpatterns = [
        path('',views.index,name='onlypage'),
        path('mov',views.getmov,name='getmov'),
]
