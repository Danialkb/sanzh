from django.db import models

from departments.models import KitchenDepartment


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "categories"


class Set(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "sets"


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "groups"


class Dish(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    department = models.ForeignKey(
        KitchenDepartment,
        on_delete=models.CASCADE,
        related_name="dishes",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    categories = models.ManyToManyField(
        Category, 
        through="DishCategory", 
        related_name="dishes"
    )
    sets = models.ManyToManyField(
        Set, 
        through="DishSet", 
        related_name="dishes"
    )
    groups = models.ManyToManyField(
        Group, 
        through="DishGroup", 
        related_name="dishes"
    )

    class Meta:
        db_table = "dishes"


class DishCategory(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class DishSet(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    set = models.ForeignKey(Set, on_delete=models.CASCADE)


class DishGroup(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
