from django import forms

from .models import Device


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('SNMP_version', 'community', 'ip_address',
                  'host_name', 'port')
