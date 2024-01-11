from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView

urlpatterns = [
    # path('', views.home, name="home"),
    # path for class based view
    path('', HomeView.as_view(), name="home"),
    # pk is primary key of each blog entry
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
]
