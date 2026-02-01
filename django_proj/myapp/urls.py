from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('article/<int :id>',views.article_det,name='article_det'),
    path('category/<slug:slug',views.category,name='category'), 
    path('profile/<str:username>',views.profile,name='profile')
    

]