from rest_framework import serializers
from tpv_api.models import ProductCategory, Product

class ProductCategorySerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = ProductCategory
        fields = ('id', 'create_date', 'name', 'parent_id', 'image')

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'create_date', 'name', 'linenos', 'image', 'category_id', 'sale_price')
