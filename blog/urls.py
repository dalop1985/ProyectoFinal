from django.urls import path
from blog.views import *
from django.db.models.query_utils import *
from django.contrib.auth.views import *

urlpatterns = [
    path('Blog/',blog, name="Blog"),
]

