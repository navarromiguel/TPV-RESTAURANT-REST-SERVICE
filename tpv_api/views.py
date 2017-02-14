from tpv_api.models import ProductCategory, Product, Table, Floor, User, Employee, AccountStatement, Company, PosConfig, Order, OrderLine
from tpv_api.serializers import ProductCategorySerializer, ProductSerializer, FloorSerializer, TableSerializer, UserSerializer, EmployeeSerializer, AccountStatementSerializer, CompanySerializer, PosConfigSerializer, OrderSerializer, OrderLineSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route, list_route

class ProductCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class FloorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

class TableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @list_route(methods=["POST"])
    def login(self, request):
        if not request.data["alias"] or not request.data["password"]:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        logged = User.objects.all().filter(alias=request.data["alias"],password=request.data["password"])

        if len(logged):
            return Response({}, status=status.HTTP_200_OK)

        return Response({}, status=status.HTTP_400_BAD_REQUEST)

class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AccountStatementViewSet(viewsets.ModelViewSet):
    queryset = AccountStatement.objects.all()
    serializer_class = AccountStatementSerializer

class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class PosConfigViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PosConfig.objects.all()
    serializer_class = PosConfigSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderLineViewSet(viewsets.ModelViewSet):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer




