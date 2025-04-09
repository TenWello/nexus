from django.db.models import Prefetch
from django.shortcuts import render, redirect
from category.models import Category
from product.models import Product, ProductImage
from .forms import EmailForm
from django.core.mail import send_mail
from category.models import Region
from nexus import settings


def main(request):
    categories = Category.objects.filter(is_main=True)
    locations = Region.objects.all()
    products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images'))
    print(products)
    ctx = {
        "categories": categories,
        "products": products,
        "locations": locations,
        "a" : 1234567890
    }
    return render(request, 'index.html', ctx)


def contact(request):
    form = EmailForm()
    name = form.cleaned_data['name']
    user_email = form.cleaned_data['email']
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message']
    print("START...")
    send_mail(
        subject,
        message,
        user_email,
        ['nexusfayziev@gmail.com'],

        fail_silently=False,
    )
    print('END.....')
    ctx = {
        "form": form
    }
    return render(request, 'contact.html', ctx)

