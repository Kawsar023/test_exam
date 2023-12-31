from django.urls import path
from adminpannel import views

urlpatterns = [
    path('reg', views.registration,name= 'reg'),
    path('login', views.loginUser,name= 'login'),
    path ('dashboard',views.dashboard,name='dashboard'),
    path ('logout',views.logoutUser,name='logout'),
]