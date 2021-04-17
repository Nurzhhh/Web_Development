from django.urls import path

from api.views import company_list, companies_detail, vacancy_list, vacancies_detail, company_vacancies, vacancies_top_ten

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:company_id>/', companies_detail),
    path('companies/<int:company_id>/vacancies', company_vacancies),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancies_detail),
    path('vacancies/top_ten/', vacancies_top_ten)
]