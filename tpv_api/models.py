from django.db import models

class BaseModel(models.Model):
    create_date = models.DateTimeField(db_column='create_date', auto_now_add=True)

    class Meta:
       abstract = True

class ProductCategory(BaseModel):
    name = models.CharField(db_column='name', max_length=100, blank=True, default='')
    parent_id = models.ForeignKey('self', db_column='parent_id')
    image = models.TextField(db_column='image')
    
    class Meta:
        ordering = ('name',)
        db_table = 'tpv_product_category'

class Product(BaseModel):
    name = models.CharField(db_column='name', max_length=100, blank=True, default='')
    sale_price = models.FloatField(db_column='sale_price')
    image = models.TextField(db_column='image')
    category_id = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, db_column='category_id')

    class Meta:
        ordering = ('name',)
        db_table = 'tpv_product'
