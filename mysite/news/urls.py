from django.urls import path
from .views import *


urlpatterns = [
    path(route='', view=index),
    path(route='test/', view=test),
]
