import os
from pathlib import Path
from ipaddress import IPv4Network, IPv4Address
from urllib.request import urlretrieve

import pytest

from ips import ServiceIPRange, parse_ipv4_service_ranges, get_aws_service_range

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network("192.0.2.8/29")


@pytest.fixture(scope="module")
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


def test_ServiceIPRange_instance():
    sipr = ServiceIPRange(service="WORKSPACES_GATEWAYS", region="eu-central-1", cidr=IP)
    assert isinstance(sipr.service, str)
    assert isinstance(sipr.region, str)
    assert isinstance(sipr.cidr, IPv4Network)


def test_ServiceIPRange_str(capsys):
    sipr = ServiceIPRange(service="WORKSPACES_GATEWAYS", region="eu-central-1", cidr=IP)
    print(sipr)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "192.0.2.8/29 is allocated to the WORKSPACES_GATEWAYS service in the eu-central-1 region\n"
    )


def test_parse_ip_range_return_content(json_file):
    result = parse_ipv4_service_ranges(json_file)
    assert isinstance(result, list)
    for item in result:
        assert isinstance(item, ServiceIPRange)


def test_raise_value_err(json_file):
    ip_services = parse_ipv4_service_ranges(json_file)
    with pytest.raises(ValueError, match="Address must be a valid IPv4 address"):
        get_aws_service_range("666.666.666.666", ip_services)


def test_return_valid_service_range(json_file):
    ip_services = parse_ipv4_service_ranges(json_file)
    ip_range = get_aws_service_range("192.0.2.8", ip_services)
    assert isinstance(ip_range, list)
    for item in ip_range:
        assert item.cidr == IPv4Address("192.0.2.8")
