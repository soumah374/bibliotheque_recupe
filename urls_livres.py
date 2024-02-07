from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import LivreCreateView,LivreListView,LivreDetailView,LivreUpdateView,LivreDeleteView,update_publiciter
# ,CategorieLivre

app_name = 'livre'
urlpatterns = [
    path('',login_required(LivreCreateView.as_view()), name='create'),
    path('index/',login_required(LivreListView.as_view()), name='index'),
    path('update_publiciter/',login_required(update_publiciter), name='update_publiciter'),
    path('detail/<str:slug>/',login_required(LivreDetailView.as_view()), name='detail'),
    # path('categories_livre/<int:pk>/',login_required(CategorieLivre), name='categorie_livre'),
    path('update/<str:slug>/',login_required(LivreUpdateView.as_view()), name='update'),
    path('delete/<str:slug>/',login_required(LivreDeleteView.as_view()), name='delete'),
]
