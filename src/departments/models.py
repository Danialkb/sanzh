from django.db import models


class KitchenDepartment(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "kitchen_departments"
