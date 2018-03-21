from django import forms

from .models import Device


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('name', 'SO', 'SNMP_version', 'system_location', 'interfaces', 'community', 'ip_address',
                  'host_name', 'port')
