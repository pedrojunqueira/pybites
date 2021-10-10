from collections import Counter

import bs4
import requests

COMMON_DOMAINS = "https://bites-data.s3.us-east-2.amazonaws.com/" "common-domains.html"
TARGET_DIV = {"class": "middle_info_noborder"}


def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    common_domains_el = soup.find("div", TARGET_DIV)
    return [row.find_all("td")[2].text for row in common_domains_el.find_all("tr")]


def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
    ignoring the list (or set) of common_domains"""
    c = Counter()
    if common_domains is None:
        common_domains = get_common_domains()
    for email in emails:
        domain = email.split("@")[-1]
        if domain not in common_domains:
            c[domain] += 1
    return sorted([(k, v) for k, v in c.items()], key=lambda x: x[1], reverse=True)


get_most_common_domains(["pedrocj@gmail.com"])
