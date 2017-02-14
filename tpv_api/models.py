from django.db import models

class BaseModel(models.Model):
    create_date = models.DateTimeField(db_column='create_date', auto_now_add=True)

    class Meta:
       abstract = True

class ProductCategory(BaseModel):
    name = models.CharField(db_column='name', max_length=100, blank=True, default='')
    parent_id = models.ForeignKey('self', db_column='parent_id', blank=True, null=True)
    image = models.TextField(db_column='image', blank=True)
    
    class Meta:
      #  ordering = ('name',)
        db_table = 'tpv_product_category'

class Product(BaseModel):
    name = models.CharField(db_column='name', max_length=100, blank=True, default='')
    sale_price = models.FloatField(db_column='sale_price')
    image = models.TextField(db_column='image', blank=True, default="placeholder.png")
    category_id = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, db_column='category_id')

    class Meta:
        ordering = ('name',)
        db_table = 'tpv_product'

class Floor(BaseModel):
    name = models.CharField(db_column='name', max_length=30)

    class Meta:
        ordering = ('name',)
        db_table = 'tpv_floor'

class Table(BaseModel):
    name = models.CharField(db_column='name', max_length=30)
    seats = models.IntegerField(db_column='seats', default = 1)
    floor_id = models.ForeignKey(Floor, db_column='floor_id')

    class Meta:
        ordering = ('name',)
        db_table = 'tpv_table'

class User(BaseModel):
    name = models.CharField(db_column='name', max_length=50)
    alias = models.CharField(db_column='alias', max_length=50)
    password = models.CharField(db_column='password', max_length=200)
    image = models.TextField(db_column='image', blank=True)

    class Meta:
        db_table = 'tpv_user'

class Employee(BaseModel):
    pin = models.IntegerField(db_column='pin')
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, db_column='user_id')

    class Meta:
        db_table = 'tpv_employee'

class AccountStatement(BaseModel):
    name = models.CharField(db_column='name', max_length=50)
    total = models.FloatField(db_column="total")

    class Meta:
        db_table = 'tpv_account_statement'

class Company(BaseModel):
    name = models.CharField(db_column='name', max_length=100, blank=True, default='')
    image = models.TextField(db_column='image', blank=True)

    class Meta:
        ordering = ('name',)
        db_table = 'tpv_company'

class PosConfig(BaseModel):
    name = models.CharField(db_column='name', max_length=100, blank=True, default='')
    company_id = models.ForeignKey(Company, on_delete=models.PROTECT, db_column='company_id')

    class Meta:
        ordering = ('name',)
        db_table = 'tpv_pos_config'

class Order(BaseModel):
    state = models.CharField(db_column='state', max_length=100, blank=True, default='')
    employee_id = models.ForeignKey(Employee, db_column='employee_id')
    table_id = models.ForeignKey(Table, db_column='table_id', blank=True)
    pos_config_id = models.ForeignKey(PosConfig, on_delete=models.PROTECT, db_column='pos_config_id')
    account_statement_id = models.ForeignKey(AccountStatement, on_delete=models.PROTECT, db_column='account_statement_id', blank=True, null=True)

    class Meta:
        db_table = 'tpv_order'

class OrderLine(BaseModel):
    price_unit = models.FloatField(db_column='price_unit')
    qty = models.IntegerField(db_column='qty')
    discount = models.FloatField(db_column='discount')
    product_id = models.ForeignKey(Product, db_column='product_id', blank=True, null=True, on_delete=models.SET_NULL)
    order_id = models.ForeignKey(Order, db_column='order_id')
    
    """
    def delete(self):
        print "delete \n\n\n"

        self.order_id = None;
        self.update()
            
        super(OrderLine, self).delete()
    """
    class Meta:
        db_table = 'tpv_order_line'



