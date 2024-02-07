from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import VenteLivreCreateView,VenteLivreListView,VenteLivreDetailView,VenteLivreUpdateView,VenteLivreDeleteView

app_name = 'vente_livre'
urlpatterns = [
    path('create/',login_required(VenteLivreCreateView.as_view()), name='create'),
    path('',login_required(VenteLivreListView.as_view()), name='index'),
    path('detail/<str:slug>/',login_required(VenteLivreDetailView.as_view()), name='detail'),
    path('update/<str:slug>/',login_required(VenteLivreUpdateView.as_view()), name='update'),
    path('delete/<str:slug>/',login_required(VenteLivreDeleteView.as_view()), name='delete'),
]
