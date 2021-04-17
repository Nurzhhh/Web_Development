from django.contrib import admin

from api.models import Company, Vacancy


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'city', 'address',)
    search_fields = ('name',)
    list_filter = ('id',)


# @admin.register(Vacancy)
# class VacancyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'description', 'salary',)
#     search_fields = ('name',)
#     list_filter = ('id',)
    
admin.site.register(Vacancy)