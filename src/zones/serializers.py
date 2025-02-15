from rest_framework import serializers

from zones.models import Zone, Table


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = "__all__"

    def to_representation(self, instance: Zone):
        representation = super().to_representation(instance)
        representation["tables"] = TableSerializer(instance.tables.all(), many=True).data
        return representation
