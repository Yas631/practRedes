from django.shortcuts import render
# Create your views here.
from django.db import models
from monitorSNMP.models import Device
from .forms import DeviceForm
from django.shortcuts import redirect
from monitorSNMP.Agent import agent_snmp


def devices_list(request):
    devicesquery = Device.objects.all()
    if request.method == 'POST':
        device_to_eliminate = request.POST["dev"]
        Device.objects.filter(id=device_to_eliminate).delete()
        return redirect('../devices/')
    return render(request, 'monitorSNMP/VistaAgentes.html', {'devices': devicesquery})


def device_watcher(request, device_id):
    devicequery = Device.objects.get(id=device_id)
    return render(request, 'monitorSNMP/VistaMonitoreo.html', {'device': devicequery})


def add_device(request):
    if request.method == 'POST':
        device_info = DeviceForm(request.POST)
        if device_info.is_valid():
            device = device_info.save(commit=False)
            snmp_query = agent_snmp(device.host_name, device.ip_address, int(device.SNMP_version), device.community, int(device.port))
            if snmp_query.get_system_description():
                device.SO = snmp_query.get_operative_sistem()
                device.interfaces = str(snmp_query.get_interfaces())
                device.author = request.user
                device.name = snmp_query.get_host_name()
                device.save()
            return redirect('../devices/')
    else:
        device_info = DeviceForm()
    return render(request, 'monitorSNMP/VistaAgregarAgentes.html', {'device_info': device_info})
