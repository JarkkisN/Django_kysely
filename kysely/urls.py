from django.urls import path
from . import views

urlpatterns = [
    path('', views.kysely_view, name='kysely_view'),
    path('kysely/', views.kysely_view, name='kysely'),
]
