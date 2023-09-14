#!/usr/bin/env python3
import re
from collections import Counter
from json import dumps
from ipaddress import IPv4Address, IPv6Address, AddressValueError
from typing import Union

ACTION_PAT = re.compile(r'["]action["]:["]([A-Z]+)["]')
SRC_IP_PAT = re.compile(r'["]src_ip["]:["](.+?)["]')
DST_IP_PAT = re.compile(r'["]dest_ip["]:["](.+?)["]')
#SRC_IPV4_PAT = re.compile(r'["]src_ip["]:["]((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)["]')
#SRC_IPV6_PAT = re.compile(r'["]src_ip["]:["]["]')

def verify_ip(ip: str, version_int: int) -> str:
    if version_int == 4:
        try:
            IPv4Address(ip)
            return ip
        except AddressValueError:
            return None
    elif version_int == 6:
        try:
            IPv6Address(ip)
            return ip
        except AddressValueError:
            return None

def main():
    data = None
    with open("data.json", "r") as data_file:
        data = data_file.read()
    actions_match = ACTION_PAT.findall(data)
    action_count_dict = Counter(actions_match)
    print(f"1. There are {len(action_count_dict.keys())} unique actions.")
    print(f"2. The counts of unique actions are {dumps(action_count_dict, indent=2)}.")
    src_ips = SRC_IP_PAT.findall(data)
    ipv4_verified = Counter([verify_ip(ip, 4) for ip in src_ips if not None])
    extra_ipv4 = 0
    if None in ipv4_verified.keys():
        extra_ipv4 = 1
    ipv6_verified = Counter([verify_ip(ip, 6) for ip in src_ips if not None])
    extra_ipv4 = 0
    if None in ipv6_verified.keys():
        extra_ipv6 = 1
    print(f"3. There are {sum(ipv4_verified.values())-ipv4_verified.get(None, 0)} IPV4 Addresses ({len(ipv4_verified.keys()) - extra_ipv4} unique matches)")    
    print(f"   There are {sum(ipv6_verified.values())-ipv6_verified.get(None, 0)} IPV6 Addresses ({len(ipv6_verified.keys()) - extra_ipv6} unique matches)")
    dst_ips = DST_IP_PAT.findall(data)
    dst_ipv4_verified = Counter([verify_ip(ip, 4) for ip in dst_ips if not None and ip.startswith("224")])
    dst_extra_ipv4 = 0
    if None in dst_ipv4_verified.keys():
        dst_extra_ipv4 = 1
    print(f"4. There are {sum(dst_ipv4_verified.values())-dst_ipv4_verified.get(None, 0)} number of records containing ips in 224.0.0.0/8 subnet")
    print(f"   (There are {len(dst_ipv4_verified.keys()) - dst_extra_ipv4} unique ips within those records)")

if __name__ == "__main__":
    main()