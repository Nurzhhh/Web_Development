from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=255, default='')
    city = models.CharField(max_length=256)
    address = models.TextField(max_length=255, default='')
    
    def to_json(self):
        return{
            'id' : self.id,
            'name': self.name,
            'city': self.city,
            'address': self.address
        }
    
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ('id',)

    def __str__(self):
        return f'{self.id}: {self.name}'

        
class Vacancy(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    salary = models.FloatField(default=0)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='Vacancies')

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'
        ordering = ('id',)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,

        }

    def __str__(self):
        return f'{self.id}: Vacancy name - {self.name} | Salary = {self.salary}'
