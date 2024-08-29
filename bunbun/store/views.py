from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Cart, CartItem


def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    # Простая сортировка по имени или цене (если указан GET-параметр)
    sort_by = request.GET.get('sort')
    if sort_by == 'name':
        products = products.order_by('name')
    elif sort_by == 'price':
        products = products.order_by('price')

    return render(request, 'home.html', {'categories': categories, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product.html', {'product': product})

def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart, created = Cart.objects.get_or_create(user=request.user, defaults={'user': request.user})
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_detail')


def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user, defaults={'user': request.user})
    return render(request, 'cart.html', {'cart': cart})


def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()
    return redirect('cart_detail')
