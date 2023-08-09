from django.shortcuts import render
from .models import Article
# Create your views here.


def create_article(request):
    # print(request.POST)
    context = {}
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        article_obj = Article.objects.create(title=title,content=content)
        context['object'] = article_obj
        context['created'] = True
    return render(request,"articles/create.html",context=context)

def article_search(request):
    print(request.GET)
    query_dict = request.GET #dictionary of query and value, article_id

    try:
        query = int(query_dict.get("query"))
    except:
        query = None
    article_obj = None

    if query is not None:
        try:
            article_obj = Article.objects.get(id=query)
        except:
            article_obj = None
    # print(article_obj)
    context = {
        "article_data": article_obj
    }
    return render(request,'articles/search.html',context)

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