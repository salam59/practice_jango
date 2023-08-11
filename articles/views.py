from django.shortcuts import render,redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from articles.forms import articleForm

# Create your views here.

@login_required
def create_article(request):
    # print(request.POST)
    
    form = articleForm(request.POST or None) # decides GET or POST
    context = {
        "form":form
    }
    if form.is_valid(): # triggers only when the POST is used i.e, data entered
        article_obj = form.save()
        # context['object'] = article_obj
        # context['created'] = True
        context['form'] = articleForm()
    return render(request,"articles/create.html",context=context)

@login_required
def article_search(request):
    # print(request.GET)
    query_dict = request.GET #dictionary of query and value, article_id
    query = query_dict.get("query")
    article_obj = Article.objects.search(query)
    context = {
        "article_data": article_obj
    }
    return render(request,'articles/search.html',context)

@login_required
def article_details_view(request,slug=None):
    article = None
    if slug is not None:
        article = Article.objects.get(slug=slug)
    context = {
        "article":article
    }
    return render(request,"articles/details.html",context=context)