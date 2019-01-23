# Generated by Django 2.1.2 on 2019-01-23 22:31

from django.db import migrations
from revenue.utils import sku_generator
from django.utils.text import slugify

sku_names = [
    'kudos',
    'fee_free_marketplace',
    'codefund_impressions',
    'job_board_credits',
    'featured_bounties',
    'job_desc_attachment',
    'personal_consultation',
]

plan_entries = [
    {
        "name": 'Lite',
        "price": 30,
        "period": 30 * 24 * 60 * 60,
        "items": [
            {
                "quantity" : 1,
                "sku_name": "kudos"
            },
            {
                "quantity" : 1,
                "sku_name": "fee_free_marketplace"
            },
            {
                "quantity" : 1000,
                "sku_name": "codefund_impressions"
            },
            {
                "quantity" : 1,
                "sku_name": "job_board_credits"
            },
        ]
    },
    {
        "name": 'Premium',
        "price": 100,
        "period": 30 * 24 * 60 * 60,
        "items": [
            {
                "quantity" : 10,
                "sku_name": "kudos"
            },
            {
                "quantity" : 1,
                "sku_name": "fee_free_marketplace"
            },
            {
                "quantity" : 10000,
                "sku_name": "codefund_impressions"
            },
            {
                "quantity" : 1,
                "sku_name": "job_board_credits"
            },
            {
                "quantity" : 1,
                "sku_name": "featured_bounties"
            },
            {
                "quantity" : 1,
                "sku_name": "job_desc_attachment"
            },
            {
                "quantity" : 1,
                "sku_name": "personal_consultation"
            },
        ]
    },
]

def forwards_func(apps, schema_editor):
    ALaCartePurchase = apps.get_model('revenue', 'ALaCartePurchase')
    SKU = apps.get_model('revenue', 'SKU')
    Plan = apps.get_model('revenue', 'Plan')
    PlanItem = apps.get_model('revenue', 'PlanItem')

    for name in sku_names:
        SKU.objects.create(
            name=name,
            sku=sku_generator(),
            )

    for plan in plan_entries:
        plan_obj = Plan.objects.create(
            slug = slugify(plan['name']),
            name = (plan['name']),
            cost_per_period=plan['price'],
            period_length_seconds=plan['period'],
            )
        for item in plan['items']:
            PlanItem.objects.create(
                plan=plan_obj,
                quantity=item['quantity'],
                sku=SKU.objects.get(name=item['sku_name']),
                )




def backwards_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('revenue', '0005_auto_20190123_2229'),
    ]

    operations = [
        migrations.RunPython(forwards_func, backwards_func),
    ]