import re


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:
    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        domain = re.match(r".*\.[a-z]{2,3}$", name)
        if not domain:
            raise DomainException
        self.name = name

    @classmethod
    def parse_email(cls, email):
        domain = re.findall(r"@[\w.]+", email)
        return cls(domain[0].strip("@"))

    @classmethod
    def parse_url(cls, url):
        domain = re.findall(r"(?:^https?:\/\/([^\/]+)(?:[\/,]|$)|^(.*)$)", url)
        return cls(domain[0][0])

    def __str__(self) -> str:
        return f"{self.name}"


d = Domain("www.google.com")

print(type(d))
