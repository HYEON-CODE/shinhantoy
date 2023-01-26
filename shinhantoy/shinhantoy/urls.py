from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenRefreshView,
    TokenObtainPairView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/member', include('member.urls')),
    path('api/order', include('order.urls')),
    path('api/token', TokenObtainPairView.as_view()),
]
