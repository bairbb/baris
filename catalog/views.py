from django.shortcuts import get_object_or_404, render
from .models import Category
from product.models import Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'catalog/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})
