# Generated by Django 3.1.7 on 2021-03-18 14:11

from django.db import migrations

def capitalize(apps, schema_editor):
    Product = apps.get_model('main', 'Product')
    for product in Product.objects.all():
        product.name = product.name.capitalize()
        product.save()

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_activemanager'),
    ]

    operations = [
    ]
