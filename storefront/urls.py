"""
URL configuration for storefront project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from product import views as productviews
from user import views as userviews

router = routers.DefaultRouter()
router.register(r"products", productviews.ProductView, "product")
router.register(r"inventory", productviews.ProductInventoryView, "inventory")
router.register(r"category", productviews.ProductCategoryView, "category")
router.register(r"discount", productviews.DiscountView, "discount")
router.register(r"users", userviews.UserView, "user")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls), name="product"),
    path("api/", include(router.urls), name="inventory"),
    path("api/", include(router.urls), name="category"),
    path("api/", include(router.urls), name="discount"),
    path("api/", include(router.urls), name="user"),
    # path('auth/', include('rest_auth.urls')),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
