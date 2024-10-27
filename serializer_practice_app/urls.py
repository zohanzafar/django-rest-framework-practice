from django.urls import path
from . import views

urlpatterns = [
    path('get_student/<int:pk>', views.get_student, name='get_student'),
    path('get_all_student/', views.get_all_student, name='get_all_student'),
]