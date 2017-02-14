
from django.conf.urls import url, include
from tpv_api import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'product_categories', views.ProductCategoryViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'floors', views.FloorViewSet)
router.register(r'tables', views.TableViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'users/login/', views.UserViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'account-statements', views.AccountStatementViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'pos-configs', views.PosConfigViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'orderlines', views.OrderLineViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
"""
urlpatterns = [
    url(r'^', include('tpv_api.urls')),
]
"""
