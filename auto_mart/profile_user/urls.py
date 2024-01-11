from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    # path('profile/edit', views.EditProfileView.as_view(), name='edit_profile'),
    # path('profile/edit/pass_change/', views.PasswordChangeCustomView.as_view(), name='pass_change'),
    # path('profile/buy_now/<int:pk>/', views.BuyNowView.as_view(), name='buy_now'),
    # path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='user_login'),
    # path('logout/', views.user_logout, name='user_logout'),
    # path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/edit/pass_change/', views.pass_change, name='pass_change'),
    path('profile/buy_now/<int:id>/', views.buy_now, name='buy_now'),
    # path('details/<int:id>/', views.DetailCarView.as_view(), name='detail_car'),
]