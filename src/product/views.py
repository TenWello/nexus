from django.shortcuts import render, redirect
from django.db.models import Prefetch, Count
from django.core.paginator import Paginator

from . import models
from .models import Product, ProductImage, ProductView
from .forms import ProductForm
from category.models import Category, Region




def product_list(request):
    page = request.GET.get('page', 1)
    per_page = request.GET.get('order', 6)
    print('PAGE:', page, 'PER PAGE:', per_page)
    locations = Region.objects.all()
    categories = Category.objects.filter(is_main=True).annotate(
        product_count=Count('product'))
    products = Product.objects.prefetch_related(
        Prefetch(
            'images',
            queryset=ProductImage.objects.filter(is_main=True),
            to_attr='main_images'
        )
    )

    item_counts = [4, 6, 8]  # Foydalanuvchi tanlashi uchun variantlar

    paginator = Paginator(products, int(per_page))  # Har sahifada mahsulotlar dinamik
    page_obj = paginator.get_page(page)

    ctx = {
        "products": page_obj,
        "page_obj": page_obj,
        "count": paginator.count,
        "item_counts": item_counts,
        "selected_count": per_page,
        "locations": locations,
        "categories": categories,

    }

    return render(request, 'products.html', ctx)


def product_detail(request, pk):
    # Asosiy mahsulotni olish
    product = Product.objects.prefetch_related(
        Prefetch(
            'images',
            queryset=ProductImage.objects.all(),
            to_attr='all_images'
        )
    ).get(pk=pk)

    # Bir xil sotuvchining boshqa mahsulotlari
    seller_products = Product.objects.filter(user=product.user).exclude(id=product.id).prefetch_related(
        Prefetch(
            'images',
            queryset=ProductImage.objects.filter(is_main=True),
            to_attr='main_images'
        )
    )[:5]  # Eng oxirgi 5 ta product
    # viewlar sonini kopaytirish
    product_view, created = ProductView.objects.get_or_create(product=product)
    product_view.view_count += 1
    product_view.save()

    ctx = {
        "product": product,
        'seller_products': seller_products,
    }
    return render(request, 'detail.html', ctx)


def product_add(request):

    if request.method == "POST":
        form = ProductForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            product = form.save(commit=False)
            print('USER', request.user.profile)
            product.user = request.user.profile
            product.save()
            return redirect('main')
    else:
        form = ProductForm()
    ctx = {
        "form": form
    }

    return render(request, 'product_add.html', ctx)


