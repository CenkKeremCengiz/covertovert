from scapy.all import *

target_ip = "172.18.0.3"

outgoing_packet = IP(dst = target_ip, ttl = 1) / ICMP()

response = sr1(outgoing_packet, timeout=2)