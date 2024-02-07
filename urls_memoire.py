from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import MemoireCreateView,MemoireListView,MemoireDetailView,MemoireUpdateView,MemoireDeleteView

app_name = 'memoire'
urlpatterns = [
    path('create/',login_required(MemoireCreateView.as_view()), name='create'),
    path('',login_required(MemoireListView.as_view()), name='index'),
    path('detail/<str:slug>/',login_required(MemoireDetailView.as_view()), name='detail'),
    path('update/<str:slug>/',login_required(MemoireUpdateView.as_view()), name='update'),
    path('delete/<str:slug>/',login_required(MemoireDeleteView.as_view()), name='delete'),
]
