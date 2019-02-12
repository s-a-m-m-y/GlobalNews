# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from news.models import Article

# Create your views here.
def articles(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'news/articles.html', context)
# Create your views here.
def article(request, articleId):
    article = Article.objects.get(id=articleId)
    context = {
        'article': article,
    }
    return render(request, 'news/article.html', context)
