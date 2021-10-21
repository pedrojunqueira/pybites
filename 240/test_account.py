import pytest

from account import Account


@pytest.fixture(scope="function")
def acc():
    ac = Account(owner="Pedro", amount=1000)
    return ac


def test_account_owner_and_amount(acc):
    ac = acc
    assert ac.owner == "Pedro"
    assert ac.amount == 1000


def test_default():
    acc = Account(owner="default")
    assert acc.amount == 0


def test_account_sdtout(capsys, acc):
    print(acc)
    captured = capsys.readouterr()
    assert captured.out == f"Account of Pedro with starting amount: 1000\n"
    print(repr(acc))
    captured = capsys.readouterr()
    assert captured.out == f"Account('Pedro', 1000)\n"


def test_add_transaction(acc):
    acc.add_transaction(100)
    assert acc._transactions == [100]


def test_add_not_int(acc):
    with pytest.raises(ValueError, match="please use int for amount"):
        acc.add_transaction("not an int")


def test_balance_property(acc):
    assert acc.balance == 1000
    acc.add_transaction(100)
    assert acc.balance == 1100


def test_len(acc):
    assert len(acc) == 0
    acc.add_transaction(100)
    assert len(acc) == 1


def test_get_item(acc):
    acc.add_transaction(100)
    acc.add_transaction(200)
    assert acc[0] == 100
    assert acc[1] == 200


def test_equality():
    acc1 = Account(owner="Pedro", amount=1000)
    acc2 = Account(owner="Elena", amount=1000)
    assert acc1 == acc2


def test_lt():
    acc1 = Account(owner="Pedro", amount=1000)
    acc2 = Account(owner="Pedro", amount=1000)
    acc2.add_transaction(100)
    assert acc1 < acc2
    acc1.add_transaction(100)
    assert not acc1 < acc2
    acc1.add_transaction(100)
    assert acc2 < acc1


@pytest.mark.parametrize("owners, amounts", [(["Pedro", "Elena"], [1000, 1000])])
def test_add(capsys, owners, amounts):
    o1, o2 = owners
    a1, a2 = amounts
    acc1 = Account(owner=o1, amount=a1)
    acc2 = Account(owner=o2, amount=a2)
    acc1.add_transaction(100)
    acc2.add_transaction(100)
    acc3 = acc1 + acc2
    assert acc3.balance == acc1.balance + acc2.balance
    print(acc3)
    captured = capsys.readouterr()
    assert captured.out == f"Account of {o1}&{o2} with starting amount: {a1+a2}\n"
    print(repr(acc3))
    captured = capsys.readouterr()
    assert captured.out == f"Account('{o1}&{o2}', {a1+a2})\n"
