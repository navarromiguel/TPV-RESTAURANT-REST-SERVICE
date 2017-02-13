# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 15:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, db_column=b'create_date')),
                ('name', models.CharField(blank=True, db_column=b'name', default=b'', max_length=100)),
                ('sale_price', models.FloatField(db_column=b'sale_price')),
                ('image', models.TextField(db_column=b'image')),
            ],
            options={
                'ordering': ('name',),
                'db_table': 'tpv_product',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, db_column=b'create_date')),
                ('name', models.CharField(blank=True, db_column=b'name', default=b'', max_length=100)),
                ('image', models.TextField(db_column=b'image')),
                ('parent_id', models.ForeignKey(db_column=b'parent_id', on_delete=django.db.models.deletion.CASCADE, to='tpv_api.ProductCategory')),
            ],
            options={
                'ordering': ('name',),
                'db_table': 'tpv_product_category',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(db_column=b'category_id', on_delete=django.db.models.deletion.PROTECT, to='tpv_api.ProductCategory'),
        ),
    ]