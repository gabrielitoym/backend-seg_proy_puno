from django.urls import path
from . import views
from .views import MyTokenObtainPairView, ProyectoApiView


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('', views.getRoutes),
    path('notes/', views.getNotes),
    path('empleados/', views.getEmpleado),
    path('proyectos/', ProyectoApiView.as_view()),

    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
