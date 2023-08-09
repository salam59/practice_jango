from django.urls import path
from .views import article_details_view

urlpatterns = [
    
    path("<int:id>",article_details_view), #dynamic url routing
]