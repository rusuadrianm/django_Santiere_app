from django.urls import path

from userextend import views

urlpatterns =[
    path('create-user/', views.UserExtendCreateView.as_view(), name='create_user'),
    path('edit_profile/<int:pk>/', views.EditProfileView.as_view(), name='edit_profile')
]