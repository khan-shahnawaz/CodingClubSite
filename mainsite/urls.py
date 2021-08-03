from django.urls import path
from . import views
urlpatterns =[
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('resources/',views.resources,name='resources'),
    path('contact/',views.contact,name='contact'),
    path('leaderboard/',views.leaderboard,name='leaderboard'),    
]
