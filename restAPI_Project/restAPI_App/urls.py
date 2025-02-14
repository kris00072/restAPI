from django.urls import path
from . import views
from drf_yasg.views import get_schema_view

from drf_yasg import openapi
schema_view=get_schema_view(
    openapi.Info(
        title="Student API",
        default_version='v1',
        description="Student API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="kris6uu7@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),public=True)



urlpatterns = [
    path('data/',views.get_data, name='get_data'),
    path('create/',views.create_student, name='create_student'),
    path('get/<int:pk>/',views.get_student, name='update_student'),
    path('update/<int:pk>/',views.update_student, name='update_student'),
    path('delete/<int:pk>/',views.delete_student, name='delete_student'),
    path('swagger/',schema_view.with_ui(cache_timeout=0),name='schema-swagger-ui'),
    path('redoc/',schema_view.with_ui(cache_timeout=0),name='schema-redoc'),

]