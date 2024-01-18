from django.contrib import admin
from . import models
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active']
    list_editable = ['price', 'is_active']
    # readonly_fields = ['description', 'slug']
    prepopulated_fields = {'slug': ['title']}
    list_filter = ['price', 'is_active']


class ProInfoAdmin(admin.ModelAdmin):
    list_display = ['color', 'texture']
    list_editable = ['texture']


class ProCatAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title']
    list_editable = ['url_title']


class ProTagAdmin(admin.ModelAdmin):
    list_display = ['tag']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory, ProCatAdmin)
admin.site.register(models.ProductInfo, ProInfoAdmin)
admin.site.register(models.ProductTag, ProTagAdmin)
