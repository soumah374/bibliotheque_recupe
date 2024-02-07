from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import AuteurCreateView,AuteurListView,AuteurDetailView,AuteurUpdateView,AuteurDeleteView

app_name = 'auteur'
urlpatterns = [
    path('create/',login_required(AuteurCreateView.as_view()), name='create'),
    path('',login_required(AuteurListView.as_view()), name='index'),
    path('detail/<str:slug>/',login_required(AuteurDetailView.as_view()), name='detail'),
    path('update/<str:slug>/',login_required(AuteurUpdateView.as_view()), name='update'),
    path('delete/<str:slug>/',login_required(AuteurDeleteView.as_view()), name='delete'),
]
