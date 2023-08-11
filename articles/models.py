from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save,post_save
from articles.utils import slugify_instance_title
from django.db.models import Q
from django.conf import settings
# Create your models here.
# at the start when created also we need to migrate
#Every time we make changes to models we need to migrate it

# python manage.py makemigrations
# python manage.py migrate

#dataclasses-->used for creating classes that are primarily used to store data, automatically generating special methods like __init__, __repr__, and others.
User = settings.AUTH_USER_MODEL
class ArticleManager(models.Manager):
    def search(self,query):
        if query is None or query=="":
            return self.get_queryset().none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.get_queryset().filter(lookups)
        
 
class Article(models.Model): #every model in jango imports models.Model, it represents that everything we write in this workable with database taht works with jango
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=60)
    slug = models.SlugField(unique=True,blank=True,null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    published = models.DateTimeField(auto_now_add=False,auto_now=False,blank=True,null=True)

    objects = ArticleManager()
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)


def pre_save_Article(sender,instance,*args,**kwargs):
    if instance.slug is None:
        slugify_instance_title(instance,save=False)
        # instance.save()

pre_save.connect(pre_save_Article,sender=Article)

def post_save_Article(sender,instance,created,*args,**kwargs):
    if created:
        slugify_instance_title(instance,save=True)

post_save.connect(post_save_Article,sender=Article)