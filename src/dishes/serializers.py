from rest_framework import serializers

from departments.models import KitchenDepartment
from departments.serializers import KitchenDepartmentSerializer
from dishes.models import Category, Set, Group, DishCategory, DishSet, DishGroup, Dish


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ["id", "name"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]


class DishCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = DishCategory
        fields = ["category"]


class DishSetSerializer(serializers.ModelSerializer):
    set = SetSerializer()

    class Meta:
        model = DishSet
        fields = ["set"]


class DishGroupSerializer(serializers.ModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = DishGroup
        fields = ["group"]


class DishSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=KitchenDepartment.objects.all())
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    sets = serializers.PrimaryKeyRelatedField(queryset=Set.objects.all(), many=True)
    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True)

    class Meta:
        model = Dish
        fields = [
            "id", "name", "price", "description", "department", "created_at", 
            "categories", "sets", "groups"
        ]

    def create(self, validated_data):
        categories = validated_data.pop("categories", [])
        sets = validated_data.pop("sets", [])
        groups = validated_data.pop("groups", [])

        dish = Dish.objects.create(**validated_data)

        for category in categories:
            DishCategory.objects.create(dish=dish, category=category)

        for set_instance in sets:
            DishSet.objects.create(dish=dish, set=set_instance)

        for group in groups:
            DishGroup.objects.create(dish=dish, group=group)

        return dish
