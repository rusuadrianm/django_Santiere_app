from django.urls import path

from santiere import views

urlpatterns = [
    path('aduaga-santier/', views.SantiereCreateView.as_view(), name='aduaga_santier'),
    path('lista-santiere/', views.SantiereListView.as_view(), name='lista_santiere'),
    path('lista-santiere-dispacer/', views.SantiereListView_Dispacer.as_view(), name='ls_dispacer'),
    path('update-santier-dispacer/<int:pk>/', views.SantiereUpdateViewDispecer.as_view(), name='update_santier_dispacer'),
    path('lista-santiere-diriginte/', views.SantiereListView_Diriginte.as_view(), name='ls_diriginte'),
    path('update-santier-diriginte/<int:pk>/', views.SantiereUpdateViewDiriginte1.as_view(), name='update1_santier_diriginte'),
    path('delete-santier-diriginte/<int:pk>/', views.SantierDeleteDiriginteView.as_view(), name="delete_santier_diriginte"),
    path('lista_santiere_filtru/', views.SantiereListViewFilter.as_view(), name='lista_santiere_filtru')
]