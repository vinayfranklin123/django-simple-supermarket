from django.shortcuts import render, redirect
from django.db.models import Q
from storage.models import Items, Orders, Brand, Category, Product, StockIn, StockOut


def search_view(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        submitbutton= request.GET.get('submit')
        if query is not None:
            results = Items.objects.filter(
                Q(item_name__icontains=query))
            context = {'results':results,
                       'submitbutton':submitbutton}
            return render(request, 'search.html', context)
        else:
            return render(request, 'search.html')
    elif request.method == 'POST':
        itemname = request.POST['item_name']
        quantity = request.POST['quantity']
        item = Items.objects.get(item_name=itemname)
        if item.item_quantity >= float(quantity):
            item.item_quantity = item.item_quantity - float(quantity)
            order = Orders(or_item_name=itemname, or_item_quantity=quantity, or_total_price=item.item_price*float(quantity))
            order.save()
            item.save()
        return redirect('index')
    else:
        return render(request, 'search.html')


def dashboard_view(request):
    return render(request, 'dashboard.html')


def brand_view(request):
    brands = Brand.objects.all()
    return render(request, 'brand.html', {'brand':brands})


def category_view(request):
    category = Category.objects.all()
    return render(request, 'category.html', {'category':category})


def product_view(request):
    product = Product.objects.all()
    return render(request, 'product.html', {'product':product})


def stockin_view(request):
    stockin = StockIn.objects.all()
    return render(request, 'stockin.html', {'stockin':stockin})


def stockout_view(request):
    stockout = StockOut.objects.all()
    return render(request, 'stockout.html', {'stockout':stockout})


def brand_add_view(request):
    if request.method == 'POST':
        brandname = request.POST['brandname']
        brand = Brand(brand_name=brandname)
        brand.save()
        return redirect('dashboard')
    return render(request, 'brand_add.html')


def category_add_view(request):
    if request.method == 'POST':
        categoryname = request.POST['categoryname']
        category = Category(category_name=categoryname)
        category.save()
        return redirect('dashboard')
    return render(request, 'category_add.html')
