from datetime import date
from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from .models import Product
from django.shortcuts import get_object_or_404


def product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 2)  # Show 25 contacts per page.

   

    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)

    context = {'product_list': product_list}
    return render(request, 'Product/product_list.html', context)


def product_detail(request, slug):
    #   product_detail = Product.objects.get(PRDSLug=slug)
    product_detail = get_object_or_404(Product, PRDSLug=slug)

    context = {'product_detail': product_detail , 'product_detailPRDName' :  product_detail.PRDName  }
    return render(request, 'Product/product_detail.html', context)





        
