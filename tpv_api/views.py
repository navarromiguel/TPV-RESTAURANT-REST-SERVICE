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

    @list_route()
    def news(self, request):
        res=[]
        orders = Order.objects.all().filter(state="new")
        for order in orders:
            obj = OrderSerializer(order).data
            table = TableSerializer(Table.objects.all().filter(id=order.table_id.id)[0]).data
            lines = OrderLine.objects.all().filter(order_id=order.id)
            new_lines = []
            for line in lines:
                new_line = OrderLineSerializer(line).data
                new_line["product"] =  ProductSerializer(Product.objects.all().filter(id=line.product_id.id)[0]).data
                new_lines.append(new_line)

            obj.update({
                    "table": table,
                    "floor": FloorSerializer(Floor.objects.all().filter(id=table['floor_id'])[0]).data,
                    "lines": new_lines
                })
            res.append(obj)


       # serializer = OrderSerializer(orders, many=True)
        return Response(res, status=status.HTTP_200_OK)


class OrderLineViewSet(viewsets.ModelViewSet):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer




