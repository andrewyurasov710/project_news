from django.urls import path
from .views import *


urlpatterns = [
    # path(route='', view=index, name='home'),
    path(route='', view=HomeNews.as_view(), name='home'),
    # path(route='category/<int:category_id>/', view=get_category, name='category'),
    path(route='category/<int:category_id>/', view=NewsByCategory.as_view(), name='category'),
    # path(route='news/<int:news_id>/', view=view_news, name='view_news'),
    path(route='<int:pk>/', view=ViewNews.as_view(), name='view_news'),
    # path(route='news/add-news/', view=add_news, name='add_news'),
    path(route='add-news/', view=CreateNews.as_view(), name='add_news'),
]
