from django.urls import path
from django.contrib import admin
from courses import views

urlpatterns = [
    path('', views.CourseAPIView.as_view(), name='courses_list'),
    path('<int:pk>/', views.CourseDetailAPIView.as_view(), name='courses_detail'),
]
