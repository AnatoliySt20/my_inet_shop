from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http.response import Http404
from django.conf import settings

def products_all(request):
    try:
        products = Paginator(
            Product.objects.order_by('name').all(),
            settings.ITEMS_ON_PAGE
        ).page(
            request.GET.get('p', 1)
        )
    except (EmptyPage, PageNotAnInteger):
        raise Http404
    return render(request, 'products.html', {'products': products})