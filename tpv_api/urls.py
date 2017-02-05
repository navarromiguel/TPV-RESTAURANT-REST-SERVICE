from django.conf.urls import url
from tpv_api.views import ProductCategoryViewSet, ProductViewSet
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

product_category_list = ProductCategoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
product_category_detail = ProductCategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

product_list = ProductViewSet.as_view({
    'get': 'list'
})
product_detail = ProductViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^product_categories/$', product_category_list, name='product_category-list'),
    url(r'^product_categories/(?P<pk>[0-9]+)/$', product_category_detail, name='product-category-detail'),
    url(r'^products/$', product_list, name='product-list'),
    url(r'^products/(?P<pk>[0-9]+)/$', product_detail, name='product-detail')
])
