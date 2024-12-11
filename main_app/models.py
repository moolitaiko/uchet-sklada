from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    article = models.CharField(max_length=50)
    name = models.CharField(max_length=255, null=False, blank=False)
    category = models.ForeignKey('Category', on_delete = models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return str(self.name) + ' ' + str(self.article)


class Sklad(models.Model):
    product = models.ForeignKey(Product, on_delete = models.PROTECT)
    purchase_price = models.PositiveIntegerField()   # создать отдельную таблицу для закупа
    sale_price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    condition = models.CharField(max_length=50, choices=[
        ('Новое', 'Новое'),
        ('БУ', 'Бывшее в Употреблении'),
        ('В наличии', 'В наличии'),
        ('Требует Ремонта', 'Требует Ремонта'),
        ('Требует Ревизии', 'Требует Ревизии'),
        ('НЕТ в наличии', 'Нет в наличии'),
        ('В пути', 'В пути'),
        ('На списание', 'На списание'),
    ])
    comments = models.TextField(null=True, blank=True)


    def __str__(self):
        return str(self.product) + ' ' + str(self.quantity)

    @property
    def expected_profit(self):
        return (self.sale_price - self.purchase_price) * self.quantity


class Sales(models.Model):
    positions = models.ManyToManyField("SalePosition")
    customer = models.ForeignKey('Customers', on_delete = models.SET_NULL, null=True)
    datetime = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey("Seller", on_delete=models.PROTECT, null=True, blank=True)
    discount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    discount_type = models.CharField(max_length=20, choices=[('процент', 'процент'), ('общая скидка', 'общая скидка')], default='общая скидка')

    def __str__(self):
        return str(self.positions)

class SalePosition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    sale_price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    units_of_measurement = models.ForeignKey("UnitsofMeasurement", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return str(self.product)

class UnitsofMeasurement(models.Model):
    units = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return str(self.units)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Customers(models.Model):
    name = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    bin = models.CharField(max_length=16, null=True, blank=True)


    def __str__(self):
        return str(self.name) + ' ' + str(self.telephone)


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    bin = models.CharField(max_length=16, null=True, blank=True)
    fact_address = models.CharField(max_length=255)
    ur_address = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)

    def __str__(self):
        return str(self.company_name)


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.PROTECT)
    telephone = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user)


