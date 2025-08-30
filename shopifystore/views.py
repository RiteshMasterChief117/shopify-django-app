from django.conf import settings
import shopify
from django.http import JsonResponse
from django.shortcuts import render
from myshopifyapp.shopify_utils import get_shopify_session

# def product_list(request):
#     #products = request.shopify.Products().get()
#     get_shopify_session()
#     products = shopify.Product.find(limit=10)
#     data = [{"id": p.id, "title": p.title,"image":p.images} for p in products]
#     shopify.ShopifyResource.clear_session()
#    # return JsonResponse(data, safe=False)
#
#     return render(request, "myshopifyapp/productlist.html", {"products": products})



def product_list(request):
    data = []
    get_shopify_session()
    products = shopify.Product.find(limit=10)
    for p in products:
        images = [img.src for img in p.images] if p.images else []
        data.append({
        "id": p.id,
        "title": p.title,
        "images": images
        })
        shopify.ShopifyResource.clear_session()


    return render(request, "shopifystore/base.html", {"products": products})