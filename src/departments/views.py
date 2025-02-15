from rest_framework.viewsets import ModelViewSet

from departments.models import KitchenDepartment
from departments.serializers import KitchenDepartmentSerializer


class KitchenDepartmentViewSet(ModelViewSet):
    queryset = KitchenDepartment.objects.all()
    serializer_class = KitchenDepartmentSerializer
