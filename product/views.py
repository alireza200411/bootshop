from django.shortcuts import render

def detail(request):
    return render(request, 'product/product_details.html', context={})
