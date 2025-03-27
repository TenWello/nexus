from django.shortcuts import render
from django.db.models import Prefetch
from django.core.paginator import Paginator
from .models import Product, ProductImage

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product, ProductImage
from django.db.models import Prefetch


def product_list(request):
    page = request.GET.get('page', 1)
    per_page = request.GET.get('order', 6)  # Default 6, lekin foydalanuvchi o‘zgartirishi mumkin
    print('PAGE:', page, 'PER PAGE:', per_page)

    products = Product.objects.prefetch_related(
        Prefetch(
            'images',
            queryset=ProductImage.objects.filter(is_main=True),
            to_attr='main_images'
        )
    )

    item_counts = [6, 12, 18]  # Foydalanuvchi tanlashi uchun variantlar

    paginator = Paginator(products, int(per_page))  # Har sahifadagi mahsulot soni dinamik
    page_obj = paginator.get_page(page)

    ctx = {
        "products": page_obj,  # Endi faqatgina `page_obj` yuboriladi
        "page_obj": page_obj,
        "count": paginator.count,
        "item_counts": item_counts,  # Variantlar ham shablonga uzatiladi
        "selected_count": per_page  # Foydalanuvchi tanlagan qiymatni saqlash
    }

    return render(request, 'products.html', ctx)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    ctx = {
        "product": product
    }
    return render(request, 'detail.html', ctx)

