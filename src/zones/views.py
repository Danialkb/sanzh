from rest_framework.viewsets import ModelViewSet

from zones.models import Zone, Table
from zones.serializers import ZoneSerializer, TableSerializer


class TableViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class ZoneViewSet(ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
