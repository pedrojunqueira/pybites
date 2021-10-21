from urllib.request import urlretrieve
import os
from pathlib import Path

import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup
from collections import Counter

TMP = Path(os.getenv("TMP", "/tmp"))
PYCON_HTML = TMP / "pycon2019.html"
PYCON_PAGE = "https://bites-data.s3.us-east-2.amazonaws.com/" "pycon2019.html"

if not PYCON_HTML.exists():
    urlretrieve(PYCON_PAGE, PYCON_HTML)


def _get_soup(html=PYCON_HTML):
    return Soup(html.read_text(encoding="utf-8"), "html.parser")


def get_pycon_speaker_first_names(soup=None):
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
    speakers (class "speaker"). Note that some items contain
    multiple speakers so you need to extract them.
    Return a list of first names
    """
    soup = _get_soup()
    speaker_elements = soup.find_all(class_="speaker")
    speakers = [
        session.text.strip()
        for session in speaker_elements
        if ("," not in session.text) and ("/" not in session.text)
    ]
    sessions_with_pairs = [
        session.text.strip()
        for session in speaker_elements
        if ("," in session.text) or ("/" in session.text)
    ]
    for speaker in sessions_with_pairs:
        if "," in speaker:
            speakers.extend(speaker.split(","))
        if "/" in speaker:
            speakers.extend(speaker.split("/"))

    return [full_name.split()[0] for full_name in speakers]


def get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
    of female speakers (female and mostly_female),
    rounded to 2 decimal places."""
    females = 0
    for name in first_names:
        detector = gender.Detector()
        g = detector.get_gender(name)
        if "female" in g:
            females += 1

    return round(females / len(first_names) * 100, 2)
