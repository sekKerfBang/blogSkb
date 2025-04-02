from django.urls import path  # type: ignore
from .views import *

app_name= 'blog'

urlpatterns = [
    path('', liste_articles, name='liste_articles'),
    path('article/<uuid:id>/', detail_article, name='detail_article'),
]