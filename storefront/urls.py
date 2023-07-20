# old versions of restframework are borked af, see
# https://stackoverflow.com/questions/70738414/importerror-cannot-import-name-url-from-django-conf-urls-django-rest-auth

# swapped from django-rest-auth to Dj-rest-auth (newest fork)

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from order import views as orderviews
from product import views as productviews

# from user import views as userviews

router = routers.DefaultRouter()
# router.register(r"products", productviews.ProductViews, "product")
# router.register(r"inventory", productviews.ProductInventoryView, "inventory")
# router.register(r"category", productviews.ProductCategoryView, "category")
# router.register(r"discount", productviews.DiscountView, "discount")
# router.register(r"users", userviews.UserView, "user")
# router.register(r"address", userviews.UserAddressView, "address")
# router.register(r"payment", userviews.UserPaymentView, "payment")
# router.register(r"session", userviews.ShoppingSessionView, "session")
# router.register(r"cart", userviews.CartView, "cart")
# router.register(r"payment_details", orderviews.PaymentDetailsView, "payment_details")
# router.register(r"order_details", orderviews.OrderDetailsView, "order_details")
# router.register(r"order_items", orderviews.OrderItemsView, "order_items")
router.register(r"product", productviews.ProductViewSet, "product")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls), name="product"),
    # path("api/", include(router.urls), name="inventory"),
    # path("api/", include(router.urls), name="category"),
    # path("api/", include(router.urls), name="discount"),
    # path("api/", include(router.urls), name="user"),
    # path("api/", include(router.urls), name="order"),
    path("auth/", include("dj_rest_auth.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
