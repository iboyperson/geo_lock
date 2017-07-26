from IPy import IP

def ip_version(ip):
    iptype = IP(ip).version()
    if iptype == 4:
        return "ipv4"
    elif iptype == 6:
        return "ipv6"
