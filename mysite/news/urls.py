from django.urls import path
from .views import *


urlpatterns = [
    path(route='', view=index, name='home'),
    path(route='category/<int:category_id>/', view=get_category, name='category'),
    path(route='news/<int:news_id>/', view=view_news, name='view_news'),
]
