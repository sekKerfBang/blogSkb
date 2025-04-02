from django.shortcuts import render # type: ignore
from .models import Article

def liste_articles(request):
    articles = Article.objects.order_by('-date_publication')
    return render(request, 'blog/listes_articles.html', {'articles': articles})

def detail_article(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'blog/details_articles.html', {'article': article})