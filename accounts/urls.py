from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (SignUpView,
                    LoginView,
                    LogoutView,
                    ProfileView,
                    ProfileEdit,
                    PasswordChangeView,
                    )

urlpatterns =[
    path('signup/',SignUpView,name='signup'),
    path('login/',LoginView,name='login'),
    path('logout/',LogoutView,name='logout'),
    path('profile/',ProfileView,  name='profile'),
    path('profile_edit/',ProfileEdit,  name='profile_edit'),
    path('password_change/',PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
]