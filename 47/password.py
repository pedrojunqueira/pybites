import string
import re

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set("PassWord@1 PyBit$s9".split())


def validate_password(password):
    criteria = {
        "length": True if len(password) >= 6 and len(password) <= 12 else False,
        "has digit": True if re.search(r"\d+", password) else False,
        "has two lower case": True
        if len(re.findall(r"[a-z]", password)) >= 2
        else False,
        "has one upper case": True if re.findall(r"[A-Z]", password) else False,
        "has one punctuation": True
        if any(c in PUNCTUATION_CHARS for c in password)
        else False,
        "never used": password not in used_passwords,
    }
    used_passwords.add(password)
    return all(checks for checks in criteria.values())