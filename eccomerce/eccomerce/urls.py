"""
URL configuration for eccomerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from products.views import ProductViewSet, CategoryViewSet
from users.views import RegisterView, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="E-Commerce API",
        default_version="v1",
        description="E-Commerce Backend API Documentation",
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path('api/', include('eccomerce.products.urls')),
    path("api/auth/register/", RegisterView.as_view(), name="register"),
    path("api/auth/login/", MyTokenObtainPairView.as_view(),
         name="token_obtain_pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("swagger/", schema_view.with_ui("swagger",
         cache_timeout=0), name="schema-swagger-ui"),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
