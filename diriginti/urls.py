from django.urls import path

from diriginti import views

urlpatterns = [
    path('creaza_diriginte/', views.DiriginteCreateView.as_view(), name='creaza_diriginte'),
    path('lista_diriginti/', views.DiriginteListView.as_view(), name='lista_diriginti'),
    path('update_diriginte/<int:pk>/', views.DiriginteUpdateView.as_view(), name='update_diriginte')
]