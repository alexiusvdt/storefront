# old versions of restframework are borked af, see
# https://stackoverflow.com/questions/70738414/importerror-cannot-import-name-url-from-django-conf-urls-django-rest-auth

# swapped from django-rest-auth to Dj-rest-auth (newest fork)

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from order import views as orderviews
from product import views as productviews
from user import views as userviews

router = routers.DefaultRouter()
router.register(r"product", productviews.ProductViewSet, "product")
router.register(r"inventory", productviews.ProductInventoryViewSet, "inventory")
router.register(r"category", productviews.ProductCategoryViewSet, "category")
router.register(r"discount", productviews.DiscountViewSet, "discount")
router.register(r"users", userviews.UserViewSet, "user")
router.register(r"address", userviews.UserAddressViewSet, "address")
router.register(r"payment", userviews.UserPaymentViewSet, "payment")
router.register(r"session", userviews.ShoppingSessionViewSet, "session")
router.register(r"cart", userviews.CartViewSet, "cart")
router.register(r"payment_details", orderviews.PaymentDetailsViewSet, "payment_details")
router.register(r"order_details", orderviews.OrderDetailsViewSet, "order_details")
router.register(r"order_items", orderviews.OrderItemsViewSet, "order_items")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls), name="product"),
    path("auth/", include("dj_rest_auth.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
