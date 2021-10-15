import os
from pathlib import Path
import string
import sys
from typing import DefaultDict
from urllib.request import urlretrieve
from zipfile import ZipFile
from numpy.lib.utils import _split_line

import pandas as pd

TMP = Path(os.getenv("TMP", "/tmp"))
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"


def _setup():
    data_zipfile = '311-data.zip'
    urlretrieve(f'{S3}/{data_zipfile}', TMP / data_zipfile)
    ZipFile(TMP / data_zipfile).extractall(TMP)
    sys.path.append(TMP)

_setup()

from stop_words import stop_words
from tf_idf import TFIDF


def load_data():
    # Load the text and populate a Pandas Dataframe
    # The order of the sample text strings should not be changed
    # Return the Dataframe with the index and 'text' column
    with open(TMP/ "samples.txt", "r") as fp:
        text = fp.read()
    #data = DefaultDict(list)
    data = [line for line in text.splitlines()[1:]]
    columns = ["text"]
    # for line in text.splitlines():
    #     data["text"].append(line)
    df = pd.DataFrame(data=data, columns=columns)
    return df


def strip_url_email(x_df):
    # Strip all URLs (http://...) and Emails (somename@email.address)
    # The 'text' column should be modified to remove
    #   all URls and Emails
    def strip_emails_and_uris(text):
        return [word for word in text.split() if "http://" not in word.lower() and "@" not in word.lower() and "https://" not in word.lower()]
    x_df.text = x_df.text.apply(strip_emails_and_uris)
    x_df.text = x_df.text.str.join(" ")
    return x_df
    


def to_lowercase(x_df):
    # Convert the contents of the 'text' column to lower case
    # Return the Dataframe with the 'text' as lower case
    x_df.text = x_df.text.str.lower()
    return x_df


def strip_stopwords(x_df):
    # Drop all stop words from the 'text' column
    # Return the Dataframe with the 'text' stripped of stop words
    def strip_stops(text):
        return [word for word in text.split() if word.lower() not in stop_words]
    x_df.text = x_df.text.apply(strip_stops)
    x_df.text = x_df.text.str.join(" ")
    return x_df


def strip_non_ascii(x_df):
    # Remove all non-ascii characters from the 'text' column
    # Return the Dataframe with the 'text' column
    #   stripped of non-ascii characters
    def remove_non_ascii(text):
        ascii_letters = [c for c in string.ascii_lowercase]
        ascii_letters.append(" ")
        for char in text:
            if char.lower() not in ascii_letters:
                text = text.replace(char,"")
        return text
    x_df.text = x_df.text.apply(remove_non_ascii)
    return x_df


def strip_digits_punctuation(x_df):
    # Remove all digits and punctuation characters from the 'text' column
    # Return the Dataframe with the 'text' column
    #   stripped of all digit and punctuation characters
    def remove_digits_punctuations(text):
        ascii_digits_punctuation = [c for c in (string.digits + string.punctuation)]
        for char in text:
            if char.lower() in ascii_digits_punctuation:
                text = text.replace(char,"")
        return text
    x_df.text = x_df.text.apply(remove_digits_punctuations)
    return x_df


def calculate_tfidf(x_df):
    # Calculate the 'tf-idf' matrix of the 'text' column
    # Return the 'tf-idf' Dataframe
    tfidf_obj = TFIDF(x_df["text"])
    return tfidf_obj()


def sort_columns(x_df):
    # Depending on how the earlier functions are implemented
    #   it's possible that the order of the columns may be different
    # Sort the 'tf-idf' Dataframe columns
    #   This ensure the tests are compatible
    return x_df.sort_values(by=["text"])


def get_tdidf():
    # Pandas’ pipeline feature allows you to string together
    #   Python functions in order to build a pipeline of data processing.
    # Complete the functions above in order to produce a 'tf-idf' Dataframe
    # Return the 'tf-idf' Dataframe
    df = (
        load_data()
        .pipe(strip_url_email)
        .pipe(to_lowercase)
        .pipe(strip_stopwords)
        .pipe(strip_non_ascii)
        .pipe(strip_digits_punctuation)
        .pipe(calculate_tfidf)
        .pipe(sort_columns)
    )
    return df

df_ = load_data()

#print(df_)

df = strip_url_email(df_)


df = to_lowercase(df_)

df = strip_stopwords(df_)

df = strip_digits_punctuation(df_)


df = strip_non_ascii(df_)

tidf_ = calculate_tfidf(df)

df = sort_columns(df)
print(df)
#print()

print(df.shape)

#print(string.ascii_letters)
#print(df)

