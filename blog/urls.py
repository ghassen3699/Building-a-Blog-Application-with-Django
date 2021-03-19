from django.urls import path
from . import views


urlpatterns = [
    path('creation_blog',views.creation_blog),
]
