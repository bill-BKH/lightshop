from django.contrib import admin
from .models import Product , ProductCategory,ProductComment,ProductVisit,ProductGallery
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductComment)
admin.site.register(ProductVisit)
admin.site.register(ProductGallery)