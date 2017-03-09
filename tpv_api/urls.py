from django.conf.urls import url
from tpv_api.views import ProductCategoryViewSet, ProductViewSet, TableViewSet, FloorViewSet, UserViewSet, EmployeeViewSet, AccountStatementViewSet, CompanyViewSet, PosConfigViewSet, OrderViewSet, OrderLineViewSet
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

product_category_list = ProductCategoryViewSet.as_view({
    'get': 'list',
})
product_category_detail = ProductCategoryViewSet.as_view({
    'get': 'retrieve',
})

product_list = ProductViewSet.as_view({
    'get': 'list',
})
product_detail = ProductViewSet.as_view({
    'get': 'retrieve',
})



floor_list = FloorViewSet.as_view({
    'get': 'list',
})

floor_detail = FloorViewSet.as_view({
    'get': 'retrieve',
})

table_list = TableViewSet.as_view({
    'get': 'list',
})

table_detail = TableViewSet.as_view({
    'get': 'retrieve',
})


user_list = UserViewSet.as_view({
    'get': 'list',
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
})


user_login = UserViewSet.as_view({
    'post': 'login'
})

employee_list = EmployeeViewSet.as_view({
    'get': 'list',
})

employee_detail = EmployeeViewSet.as_view({
    'get': 'retrieve',
})

account_statement_list = AccountStatementViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

account_statement_detail = AccountStatementViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

company_list = CompanyViewSet.as_view({
    'get': 'list',
})

company_detail = CompanyViewSet.as_view({
    'get': 'retrieve',
})

pos_config_list = PosConfigViewSet.as_view({
    'get': 'list',
})

pos_config_detail = PosConfigViewSet.as_view({
    'get': 'retrieve',
})

order_statement_list = OrderViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

new_orders = OrderViewSet.as_view({
    'get': 'news'
})

order_statement_detail = OrderViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

orderline_statement_list = OrderViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

orderline_statement_detail = OrderViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    url(r'^product_categories/$', product_category_list, name='product-category-list'),
    url(r'^product_categories/(?P<pk>[0-9]+)/$', product_category_detail, name='product-category-detail'),
    url(r'^products/$', product_list, name='product-list'),
    url(r'^products/(?P<pk>[0-9]+)/$', product_detail, name='product-detail')
    url(r'^floors/$', floor_list, name='floor-list'),
    url(r'^floors/(?P<pk>[0-9]+)/$', floor_detail, name='floor-detail')
    url(r'^tables/$', table_list, name='table-list'),
    url(r'^tables/(?P<pk>[0-9]+)/$', table_detail, name='table-detail')
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
    url(r'^users/login/$', user_login, name='user-login'),
    url(r'^employees/$', employee_list, name='employee-list'),
    url(r'^employees/(?P<pk>[0-9]+)/$', employee_detail, name='employee-detail')
    url(r'^account-statements/$', account_statement_list, name='account-statement-list'),
    url(r'^account-statements/(?P<pk>[0-9]+)/$', account_statement_detail, name='account-statement-detail')
    url(r'^companies/$', company_list, name='company-list'),
    url(r'^companies/(?P<pk>[0-9]+)/$', company_detail, name='company-detail')
    url(r'^pos-configs/$', pos_config_list, name='pos-config-list'),
    url(r'^pos-configs/(?P<pk>[0-9]+)/$', pos_config_detail, name='account_statement-detail')
    url(r'^orders/$', order_list, name='order-list'),
    url(r'^orders/(?P<pk>[0-9]+)/$', order_details, name='order-detail')
    url(r'^orders/news/)/$', new_orders, name='new-orders')
    url(r'^orderlines/$', orderline_list, name='orderline-list'),
    url(r'^orderlines/(?P<pk>[0-9]+)/$', orderline_details, name='orderline-detail')


])
