from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ActualiteCreateView,ActualiteListView,ActualiteDetailView,ActualiteUpdateView,ActualiteDeleteView,update_publiciter

app_name = 'actualite'
urlpatterns = [
    path('create/',login_required(ActualiteCreateView.as_view()), name='create'),
    path('',login_required(ActualiteListView.as_view()), name='index'),
    path('update_publiciter/',login_required(update_publiciter), name='update_publiciter'),
    path('detail/<str:slug>/',login_required(ActualiteDetailView.as_view()), name='detail'),
    path('update/<str:slug>/',login_required(ActualiteUpdateView.as_view()), name='update'),
    path('delete/<str:slug>/',login_required(ActualiteDeleteView.as_view()), name='delete'),
]
