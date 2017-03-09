from rest_framework import serializers
from tpv_api.models import ProductCategory, Product, Table, Floor, User, Employee, AccountStatement, Company, PosConfig, Order, OrderLine

class ProductCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductCategory
        fields = ('id', 'create_date', 'name', 'parent_id', 'image')

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'create_date', 'name', 'image', 'category_id', 'sale_price')


class FloorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Floor
        fields = ('id', 'create_date', 'name')


class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = ('id', 'create_date', 'name', 'seats', 'floor_id')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'create_date', 'name', 'alias', 'password', 'image')


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'create_date', 'pin', 'id_user')


class AccountStatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountStatement
        fields = ('id', 'create_date', 'name', 'total')

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'create_date', 'name', 'image')

class PosConfigSerializer(serializers.ModelSerializer):

    class Meta:
        model = PosConfig
        fields = ('id', 'create_date', 'name', 'company_id')


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'create_date', 'state', 'employee_id', 'table_id', 'pos_config_id', 'account_statement_id')

class OrderLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderLine
        fields = ('id', 'create_date', 'price_unit', 'qty', 'discount', 'product_id', 'order_id')



