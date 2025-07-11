from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_students, name='get_students'),
    path('add/', views.add_student, name='add_student'),
    path('update/<int:pk>/', views.update_student, name='update_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'), 
    path('class/', views.StudentListCreateAPIView.as_view(), name='student_class_list_create'),
    path('class/<int:pk>/', views.StudentDetailAPIView.as_view(), name='student_class_detail'),
]

