from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'), # <- here we have added the new path
    path('about/', views.About.as_view(), name='about'),
    path('finches/', views.FinchList.as_view(), name='finch_list'),
    path('finches/new', views.FinchCreate.as_view(), name='finch_create'),
    path('finches/<int:pk>/', views.FinchDetail.as_view(), name="finch_detail"),
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name="finch_update"),
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name="finch_delete"),
    path('finches/<int:pk>/sighting/new/', views.SightingCreate.as_view(), name="sighting_create"),
    path('feathers/<int:pk>/finches/<int:finches_pk>/', views.FeathersAssoc.as_view(), name='feathers_assoc'),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]
