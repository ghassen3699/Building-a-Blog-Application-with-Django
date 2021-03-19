from django.shortcuts import render
from .models import post

# Create your views here.
def creation_blog(request) :
    posts = post.objects.all()
    return render(request,'blog/fichier.html',{'posts':posts})
