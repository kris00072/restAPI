from django.urls import path
from .import views
urlpatterns = [
path('customers/', views.CustomerList.as_view()),   
path('customers/<int:pk>/', views.CustomerDetail.as_view()),
]