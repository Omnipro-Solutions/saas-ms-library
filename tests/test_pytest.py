import pytest
from src.bank_account import BankAccount


def test_suma():
    a = 4
    b = 10
    assert sum([a, b]) == 14


@pytest.mark.parametrize(
    "amount, expected",
    [
        (10, 110),
        (20, 120),
        (30, 130),
    ],
)
def test_deposit_multiple_amounts(amount, expected):
    account = BankAccount(100, "test.log")
    new_balance = account.deposit(amount)
    assert new_balance == expected
