# Generated by Django 2.1.2 on 2019-01-23 22:21

from django.db import migrations
from revenue.utils import sku_generator

def forwards_func(apps, schema_editor):
    ALaCartePurchase = apps.get_model('revenue', 'ALaCartePurchase')
    SKU = apps.get_model('revenue', 'SKU')

    avatar_sku = SKU.objects.create(
        name = 'Avatar Purchase',
        slug='avatar_purchase',
        sku=sku_generator(),
        )

    for alcp in ALaCartePurchase.objects.all():
        alcp.sku = avatar_sku
        alcp.save()

def backwards_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('revenue', '0003_auto_20190123_2218'),
    ]

    operations = [
        migrations.RunPython(forwards_func, backwards_func),
    ]