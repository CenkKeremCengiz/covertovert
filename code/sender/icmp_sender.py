from scapy.all import *

# Implement your ICMP sender here

target_ip = "172.18.0.3"

outgoing_packet = IP(dst = target_ip, ttl = 1) / ICMP()

response = sr1(outgoing_packet, timeout=2)

if(response):
    print("Received ICMP reply from", response.src)
    response.show()
else:
    print("No response received.")