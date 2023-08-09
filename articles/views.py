from django.shortcuts import render
from .models import Article
# Create your views here.

def article_details_view(request,id=None):
    article = None
    if id is not None:
        article = Article.objects.get(id=id)
    context = {
        "title": article.title,
        "id" : article.id,
        "content": article.content
    }
    return render(request,"articles/details.html",context=context)