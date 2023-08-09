from django.db import models

# Create your models here.
# at the start when created also we need to migrate
#Every time we make changes to models we need to migrate it

# python manage.py makemigrations
# python manage.py migrate

#dataclasses-->used for creating classes that are primarily used to store data, automatically generating special methods like __init__, __repr__, and others.

class Article(models.Model): #every model in jango imports models.Model, it represents that everything we write in this workable with database taht works with jango
    title = models.TextField()
    content = models.TextField()