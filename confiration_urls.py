from django.urls import path
from configuration.views import index
from django.contrib.auth.decorators import login_required

app_name = 'configuration'
urlpatterns = [
    path('', login_required(index), name='index')
]
