from django.contrib import admin

from dishes.models import Category, Set, Group, Dish, DishCategory, DishSet, DishGroup

admin.site.register(Category)
admin.site.register(Set)
admin.site.register(Group)
admin.site.register(Dish)
admin.site.register(DishCategory)
admin.site.register(DishSet)
admin.site.register(DishGroup)

