from django.shortcuts import render, redirect
from .models import Wishlist, Product
from django.contrib.auth.decorators import login_required

@login_required
def wishlist_view(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'wishlist/wishlist_view.html', {'wishlist': wishlist})

@login_required
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        url = request.POST.get('url')

        product = Product.objects.create(name=name, description=description, price=price, url=url)
        wishlist = Wishlist.objects.get(user=request.user)
        wishlist.products.add(product)

        return redirect('wishlist_view')

    return render(request, 'wishlist/add_product.html')