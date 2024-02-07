from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CategorieCreateView,CategorieUpdateView,CategorieDeleteView

app_name = 'categorie'

urlpatterns = [
    path('',login_required(CategorieCreateView.as_view()), name='categorie'),
    path('update/<str:slug>/',login_required(CategorieUpdateView.as_view()), name='update'),
    path('delete/<str:slug>/',login_required(CategorieDeleteView.as_view()), name='delete'),
]
