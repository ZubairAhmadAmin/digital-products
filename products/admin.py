from django.contrib import admin
from .models import Category, Product


class ProductInlineAdmin(admin.StackedInline):
    model = Product
    fields = ['title', 'description', 'avatar', 'price', 'is_enable']
    extra =0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time']
    search_fields = ['title']
    inlines = [ProductInlineAdmin]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_enable', 'create_time', 'avatar', 'price', 'description']
    list_filter = ['is_enable']
    search_fields = ['title']
    # filter_horizontal = ['categories']
