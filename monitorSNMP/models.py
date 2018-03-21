from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=200)
    SO = models.CharField(max_length=200)
    SNMP_version = models.CharField(max_length=200)
    system_location = models.CharField(max_length=200)
    interfaces = models.CharField(max_length=200)
    community = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=200)
    host_name = models.CharField(max_length=200)
    port = models.CharField(max_length=200)

    def __str__(self):
        return self.name
