from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import DepartementCreateView,DepartementUpdateView,DepartementDeleteView

app_name = 'departement'

urlpatterns = [
    path('',login_required(DepartementCreateView.as_view()), name='departe'),
    path('update/<str:slug>/',login_required(DepartementUpdateView.as_view()), name='update'),
    path('delete/<str:slug>/',login_required(DepartementDeleteView.as_view()), name='delete'),
]
