import os
import random
import string

import pytest

from movies import MovieDb

salt = ''.join(
    random.choice(string.ascii_lowercase) for i in range(20)
)
DB = os.path.join(os.getenv("TMP", "/tmp"), f'movies_{salt}.db')
# https://www.imdb.com/list/ls055592025/
DATA = [
    ("The Godfather", 1972, 9.2),
    ("The Shawshank Redemption", 1994, 9.3),
    ("Schindler's List", 1993, 8.9),
    ("Raging Bull", 1980, 8.2),
    ("Casablanca", 1942, 8.5),
    ("Citizen Kane", 1941, 8.3),
    ("Gone with the Wind", 1939, 8.1),
    ("The Wizard of Oz", 1939, 8),
    ("One Flew Over the Cuckoo's Nest", 1975, 8.7),
    ("Lawrence of Arabia", 1962, 8.3),
]
TABLE = 'movies'


@pytest.fixture
def db():
    Mdb = MovieDb(db=DB, data=DATA, table=TABLE)
    Mdb.init()
    yield Mdb
    Mdb.drop_table()

def test_contructor(db):
    assert db.table == 'movies'

def test_query_all(db):
    q = db.query()
    assert len(q) == 10

def test_query_by_title_exact(db):
    q = db.query(title="The Godfather")
    assert len(q) == 1
    assert q[0][1] == "The Godfather"

def test_query_by_title_anywhere(db):
    q = db.query(title="The")
    assert len(q) == 5

def test_query_by_year(db):
    q = db.query(year=1975)
    assert len(q) == 1
    assert q[0][1] == "One Flew Over the Cuckoo's Nest"

def test_query_score_gt(db):
    q = db.query(score_gt=1)
    assert len(q) == 10
    q = db.query(score_gt=9)
    assert len(q) == 2
    assert " ".join([i[1] for i in q]) == "The Godfather The Shawshank Redemption"

def test_add(db):
    q = db.query()
    assert len(q) == 10
    db.add(title="Aristocats",year=1970,score=7.1)
    q = db.query()
    assert len(q) == 11
    assert q[-1] == (11, 'Aristocats', 1970, 7.1)

def test_delete(db):
    q = db.query()
    assert len(q) == 10
    idx = q[-1][0]
    db.delete(idx)
    q = db.query()
    assert len(q) == 9