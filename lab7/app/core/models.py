# from django.db import models


# # create table core_product (
# #     id INTEGER,
# #     name VARCHAR (255),
# #     price NUMBER default 0
# # );


# class Product(models.Model):
#     id = models.IntegerField(null=True, blank=True)
#     name = models.CharField(max_length=255, null=True, blank=True)
#     price = models.FloatField(default=0, null=True, blank=True)

#     def to_json(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'price': self.price
#         }