from django.urls import path
from .api import RegisterView, DashboardView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register_api"),
    path("dashboard/", DashboardView.as_view(), name="dashboard_api"),
    path("logout/", LogoutView.as_view(), name="logout_api"),

    # JWT auth
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),   # login
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # refresh access
]
