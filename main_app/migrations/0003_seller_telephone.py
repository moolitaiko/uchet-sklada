# Generated by Django 5.1.3 on 2024-12-06 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_unitsofmeasurement_remove_sales_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='telephone',
            field=models.CharField(default='777', max_length=255),
            preserve_default=False,
        ),
    ]
