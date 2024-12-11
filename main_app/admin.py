from django.contrib import admin
from .models import *

# from .models -> Джанго будет искать в этой же папке файлик models.py
# from models -> Джанго будет искать библиотеку models
# from .models import * -> Импортируем все из файла models.py


admin.site.register(Product)  # Регистрируем модель Product в админке
admin.site.register(Customers)
admin.site.register(Sklad)
admin.site.register(Category)
admin.site.register(Sales)
admin.site.register(SalePosition)
admin.site.register(Seller)
admin.site.register(Owner)
admin.site.register(UnitsofMeasurement)
