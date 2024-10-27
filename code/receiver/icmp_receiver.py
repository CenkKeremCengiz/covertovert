from scapy.all import *

def icmp_packet_callback(packet):
    if packet.haslayer(ICMP):
        print("Received ICMP packet:")
        packet.show()

print("Listening for ICMP packets...")
sniff(filter="icmp", prn=icmp_packet_callback, timeout=10)