from django.urls import path
from . import views

urlpatterns = [
    path('login', views.HomePageView.as_view, name="login"),
    path('', views.HomePageView.as_view(), name='home'),
    path('forminfo', views.DataPageView.as_view(), name='data'),
]   