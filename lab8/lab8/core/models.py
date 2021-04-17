from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def to_json(self):
        return{
            'id' : self.id,
            'name': self.name
        }
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('id',)

    def __str__(self):
        return f'{self.id}: {self.name}'

        
class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    description = models.TextField(max_length=255, default='')
    count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='products')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('id',)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'is_active': self.is_active
        }

    def __str__(self):
        return f'{self.id}: {self.name} | {self.price}'
