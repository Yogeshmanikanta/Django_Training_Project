from django.urls import path
from . import views

urlpatterns =[
    path('dashboard/', views.faculty_dashboard, name='faculty_dashboard'),
    path('',views.feedback_view,name='feedback_view')
]