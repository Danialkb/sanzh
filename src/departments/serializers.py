from rest_framework.serializers import ModelSerializer

from departments.models import KitchenDepartment


class KitchenDepartmentSerializer(ModelSerializer):
    class Meta:
        model = KitchenDepartment
        fields = ["id", "name"]
