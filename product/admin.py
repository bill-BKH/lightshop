from django.contrib import admin
from .models import Product , ProductCategory,ProductComment
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductComment)
