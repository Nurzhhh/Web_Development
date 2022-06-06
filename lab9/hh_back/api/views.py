from django.http.response import JsonResponse

from api.models import Company, Vacancy


def company_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)


def companies_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)})

    return JsonResponse(company.to_json())

def company_vacancies(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)})

    vacancies = Vacancy.objects.all()
    company_vacancies = []
    for vacancy in vacancies:
        if vacancy.company == company:
            company_vacancies.append(vacancy)
    company_vacancies_to_json = [vacancy.to_json() for vacancy in company_vacancies]
    return JsonResponse(company_vacancies_to_json, safe=False)
    # try:
    #     vacancy = Vacancy.objects.get(company=company)
    # except Vacancy.DoesNotExist as e:
    #     return JsonResponse({'message': str(e)})
    # return JsonResponse(vacancy.to_json)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancies_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': str(e)})

    return JsonResponse(vacancy.to_json())

def vacancies_top_ten(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    vacancies_json = sorted(vacancies_json, key=lambda k : k['salary'], reverse=True)
    vacancies_json = vacancies_json[:11]
    return JsonResponse(vacancies_json, safe=False)