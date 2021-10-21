import os
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve
import json

import pytest

from ips import ServiceIPRange, parse_ipv4_service_ranges, get_aws_service_range

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network("192.0.2.8/29")


def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


source = json_file()

data = json.loads(source.read_text())

ip_services = parse_ipv4_service_ranges(source)

# print(ip_services)

# print(len(ip_services))

try:
    ip_range = get_aws_service_range(IP, ip_services)
except Exception as e:
    print(e.__dict__)

# print(ip_range)

# sipr = ServiceIPRange(service='WORKSPACES_GATEWAYS', region='eu-central-1',cidr=IP)

# print(sipr)
