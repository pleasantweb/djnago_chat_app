from django.urls import path
from apps import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home),

    path('chat/',views.group_page),
    path('chat/<str:group_name>/',views.chatting),

    path('signup/',views.SignupView.as_view(),name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='apps/registration/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout')
]
