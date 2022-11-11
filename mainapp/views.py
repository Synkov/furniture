import datetime

from django.conf import settings
from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def main(request):
    title = "Главная"
    products = Product.objects.all()
    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL}
    return render(request, "mainapp/index.html", content)


def products(request, pk=None):
    title = "продукты"
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()
    content = {
        "title": title,
        "links_menu": links_menu,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,
    }
    if pk:
        print(f"User select category: {pk}")
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "контакты"
    vizit_date = datetime.datetime.now()
    locations = [
        {"city": "Москва", "phone": "+7-777-777-77-77", "email": "info@geekshop.ru", "address": "В пределах МКАД"},
        {
            "city": "Ектаеринбург",
            "phone": "+8-888-888-88-88",
            "email": "info_yekaterinburg@geekshop.ru",
            "address": "Близко к центру",
        },
        {
            "city": "Владивосток",
            "phone": "+9-999-999-99-99",
            "email": "info_vladivostok@geekshop.ru",
            "address": "Близко к океану",
        },
    ]
    content = {"title": title, "vizit_date": vizit_date, "locations": locations}
    return render(request, "mainapp/contact.html", content)
