from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import EmpruntCreateView,EmpruntListView,EmpruntDetailView,EmpruntUpdateView,EmpruntDeleteView,Update_statut

app_name = 'emprunt'
urlpatterns = [
    path('create/',login_required(EmpruntCreateView.as_view()), name='create'),
    path('',login_required(EmpruntListView.as_view()), name='index'),
    path('update_statut',login_required(Update_statut), name='update_statut'),
    path('detail/<str:slug>/',login_required(EmpruntDetailView.as_view()), name='detail'),
    path('update/<str:slug>/',login_required(EmpruntUpdateView.as_view()), name='update'),
    path('delete/<str:slug>/',login_required(EmpruntDeleteView.as_view()), name='delete'),
]
