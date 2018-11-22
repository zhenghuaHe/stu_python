
#根据ip或者网段判断基本信息

# from IPy import  IP
#
# ip_s = input('Please input an IP or net-range:')
# ips = IP(ip_s)
#
# if len(ips) > 1:
#     print("net: %s" % ips.net())
#     print("netmask: %s" % ips.netmask())
#     print("broadcast: %s" % ips.broadcast())
#     print("reverse address: %s" % ips.reverseNames()[0])
#     print("subnet: %s" % len(ips))
# else:
#     print("reverse address: %s" % ips.reverseNames()[0])


#根据域名反解析ip

from dns import resolver

a = 1
domain = input("Please input an domain:")
A = resolver.query(domain, "A")
for i in A.response.answer:
    for j in i.items:
        print(j.address)

