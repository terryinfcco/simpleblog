from django.shortcuts import render
# Import Django's generic listview and detailview
from django.views.generic import ListView, DetailView
# Have to import our model so the views can find it
from .models import Post


# Create your views here.

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'