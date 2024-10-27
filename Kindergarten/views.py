from django.shortcuts import render
from .models import KindergartenArticle

def kindergarten_articles(request):
    articles = KindergartenArticle.objects.all().order_by('-created_at')
    return render(request, "articles.html", {"articles": articles})
