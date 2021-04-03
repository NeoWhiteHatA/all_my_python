from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('one_page/', views.OnePageView.as_view(), name='one_page'),
    path('second_page/', views.SecondPageView.as_view(), name='second_page'),
    path('three_page/', views.ThreePageView.as_view(), name='three_page'),
    path('six_page/', views.SixPageView.as_view(), name='six_page'),
]
