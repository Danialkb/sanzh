from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "zones"


class Table(models.Model):
    table_number = models.IntegerField()

    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name="tables")

    class Meta:
        db_table = "tables"
