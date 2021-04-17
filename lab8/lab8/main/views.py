from django.http.response import HttpResponse, JsonResponse


def hello(request):
    return HttpResponse('<h1>hello message</h1>')


def hours_ahead(request, hours):
    return HttpResponse(f'<h1>Hours ahead: {hours}</h1>')


products = [
    {
        'id': i,
        'name': f'Product {i}',
        'price': i * 1000,
        'count': 10,
        'is_active': True
    } for i in range(1, 11)
]


def products_list(request):
    return JsonResponse(products, safe=False)


def product_detail(request, product_id):
    for product in products:
        if product['id'] == product_id:
            return JsonResponse(product)
    return JsonResponse({'message': 'Product with selected ID not found'})


categories = [
    {
        'id': i,
        'name': f'Category {i}'
    } for i in range(1, 6)
]

def categories_list(request):
    return JsonResponse(categories, safe=False)


def categories_detail(request, category_id):
    for category in categories:
        if category['id'] == category_id:
            return JsonResponse(category)
    return JsonResponse({'message': 'Category with selected ID not found'})
