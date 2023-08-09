from django.contrib import admin
from .models import Article

# Register your models here.

class articleAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    search_fields = ['id','title']

admin.site.register(Article,articleAdmin)