from django.http.response import JsonResponse

from core.models import Product, Category


def products_list(request):
    # select * from core_product;
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    # select * from core_product where id = product_id;
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)})

    return JsonResponse(product.to_json())

def categories_list(request):
    # select * from core_product;
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def categories_detail(request, category_id):
    # select * from core_product where id = product_id;
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)})

    return JsonResponse(category.to_json())