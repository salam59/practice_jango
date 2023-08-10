from django.http import HttpResponse
import random
from articles.models import Article
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string,get_template
#use get_template when u have multiple contexts otherwise use render_to_string

@login_required
def home_view(request):
    """
    Take in a request (Django sends requests)
    return HTML as a respose
    Note: we pick which html to send
    """
    # print(request)
    #rendering the html template in the view
    
    random_id = random.randint(1,3)
    # fromm database??
    article = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()
    context ={
        "object_list": article_queryset,
        "title": article.title,
        "id" : article.id,
        "content": article.content
    }
    # HTML_STRING = """
    # <h1>{title}-->{id}</h1>
    # <p>{content}-->{id}</p>
    # """.format(**context)
    HTML_STRING = render_to_string("home_view.html",context=context)
    return HttpResponse(HTML_STRING)