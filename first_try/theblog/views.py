from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

# Going to use class based views.
# Inherit the built in Django form ListView to be able to create a list of posts
class HomeView(ListView):
    # Tell Django what model we're using
    model = Post
    template_name = 'home.html'

# Inherit the built in Django form DetailView to allow us to see a post's detail
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'