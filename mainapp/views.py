import datetime
from django.shortcuts import render


def main(request):
    title = 'Главная'
    products = [
        {
            'name': 'Отлинчый стул',
            'desc': 'Расположитесь комфортно',
            'image_src': 'product-1.jpg',
            'image_href': '/product/1/',
            'alt': 'продукт 1'
        },
        {
            'name': 'Стул повышенного качества',
            'desc': 'Не оторваться',
            'image_src': 'product-2.jpg',
            'image_href': '/product/2/',
            'alt': 'продукт 2'
        },
    ]
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)


def products(request):
    title = 'продукты'
    links_menu = [

        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},

    ]
    same_products = [
        {'name': 'Отличный стул', 'desc': 'не оторваться',
            'image_src': 'product-11.jpg', 'alt': 'продукт 11'},
        {'name': 'Стул повышенного качества', 'desc': 'комфортно',
            'image_src': 'product-21.jpg', 'alt': 'продукт 21'},
        {'name': 'Стул премиального качества', 'desc': 'Просто попробуйте',
            'image_src': 'product-31.jpg', 'alt': 'продукт 31'},
    ]
    content = {'title': title, 'links_menu': links_menu,
               'same_products': same_products}
    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = 'контакты'
    vizit_date = datetime.datetime.now()
    locations = [
        {'city': 'Москва', 'phone': '+7-777-777-77-77',
            'email': 'info@geekshop.ru', 'address': 'В пределах МКАД'},
        {'city': 'Ектаеринбург', 'phone': '+8-888-888-88-88',
            'email': 'info_yekaterinburg@geekshop.ru', 'address': 'Близко к центру'},
        {'city': 'Владивосток', 'phone': '+9-999-999-99-99',
            'email': 'info_vladivostok@geekshop.ru', 'address': 'Близко к океану'},
    ]
    content = {'title': title, 'vizit_date': vizit_date,
               'locations': locations}
    return render(request, 'mainapp/contact.html', content)
