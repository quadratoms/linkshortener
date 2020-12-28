from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
path('<str:short>/', views.direct, name='home'),
path('', views.shrink, name='shrink'),
path('shrinked/<str:short>/', views.shrinked, name='shrinked'),
]