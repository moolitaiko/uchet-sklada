# Generated by Django 5.1.3 on 2024-12-03 05:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitsofMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='sales',
            name='product',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='sale_price',
        ),
        migrations.AddField(
            model_name='sales',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='sales',
            name='discount_type',
            field=models.CharField(choices=[('процент', 'процент'), ('общая скидка', 'общая скидка')], default='общая скидка', max_length=20),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('bin', models.CharField(blank=True, max_length=16, null=True)),
                ('fact_address', models.CharField(max_length=255)),
                ('ur_address', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SalePosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main_app.product')),
                ('units_of_measurement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main_app.unitsofmeasurement')),
            ],
        ),
        migrations.AddField(
            model_name='sales',
            name='positions',
            field=models.ManyToManyField(to='main_app.saleposition'),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main_app.owner')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='sales',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main_app.seller'),
        ),
    ]
