from django.urls import path, include
from . import views

urlpatterns = [
    path('upload/', views.upload),
    path('result/<int:image_id>/', views.result)
]