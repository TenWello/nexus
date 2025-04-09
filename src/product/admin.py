from django.contrib import admin
from .models import Product, ProductImage, ProductView
from django.utils.html import mark_safe

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px;"/>')
        return "No Image"
    image_preview.short_description = 'Preview'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'status', 'user')  # 'name' o'rniga 'title' ishlating
    list_filter = ('status', 'condition', 'category')
    ist_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    inlines = [ProductImageInline]

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'is_main', 'image_preview')
    list_editable = ('is_main',)
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px;"/>')
        return "No Image"
    image_preview.short_description = 'Preview'

    def save_model(self, request, obj, form, change):
        if obj.is_main:
            ProductImage.objects.filter(
                product=obj.product,
                is_main=True
            ).exclude(id=obj.id).update(is_main=False)
        super().save_model(request, obj, form, change)

@admin.register(ProductView)
class ProductViewAdmin(admin.ModelAdmin):
    list_display = ('product', 'view_count')