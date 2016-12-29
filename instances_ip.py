from ovirtsdk.api import API
from ovirtsdk.xml import params
import time

instance_name ="instance_name"
try:
    api = API(url="url_api",
              username="user",
              password="pass",
              insecure="true")
    address = []
    vm_status = api.vms.get(
        name=instance_name).get_status().get_state()
    print('Current Status: {0}'.format(vm_status))
    if vm_status == 'up':
        vm_ip = api.vms.get(
            name=instance_name).get_guest_info().get_ips().get_ip()
        for ip in vm_ip:
            address.append(ip.get_address())
        print('\t IP : %s' % (address[0]))
except Exception as ex:
    print("Unexpected error: %s" % ex)


    api.disconnect()
