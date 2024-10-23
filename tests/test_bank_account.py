import os
import unittest
from unittest.mock import patch

from src.bank_account import BankAccount
from src.exceptions import InsufficientFundsError, WithdrawaTimeRestrictionError


class TestBankAccount(unittest.TestCase):

    TEST_FILE_NAME = "test.log"

    def setUp(self):
        self.account = BankAccount(100, self.TEST_FILE_NAME)

    def tearDown(self):
        if os.path.exists(self.TEST_FILE_NAME):
            os.remove(self.TEST_FILE_NAME)

    def _count_line(self, file_name):
        with open(file_name, "r") as file:
            return len(list(file))

    def test_deposit(self):
        self.assertEqual(self.account.deposit(50), 150)

    @patch("src.bank_account.datetime")
    def test_withdraw(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        self.assertEqual(self.account.withdraw(50), 50)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

    def test_transaction_log(self):
        self.account.deposit(20)
        self.assertTrue(os.path.exists(self.TEST_FILE_NAME))

    def test_count_transaction_log(self):
        self.account.deposit(20)
        self.assertEqual(self._count_line(self.TEST_FILE_NAME), 2)

    @patch("src.bank_account.datetime")
    def test_withdraw_raises_error_when_insufficient_funds(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(500000)

    @patch("src.bank_account.datetime")
    def test_withdraw_raises_error_when_time_is_after_6pm(self, mock_datetime):
        mock_datetime.now.return_value.hour = 18
        with self.assertRaises(WithdrawaTimeRestrictionError):
            self.account.withdraw(50)

    @patch("src.bank_account.datetime")
    def test_withdraw_does_not_raise_error_when_time_is_before_6pm(self, mock_datetime):
        mock_datetime.now().hour = 12
        self.assertEqual(self.account.withdraw(20), 80)

    def test_deposit_multiple_amounts(self):
        test_cases = [
            {"amount": 10, "expected_balance": 110},
            {"amount": 20, "expected_balance": 130},
            {"amount": 30, "expected_balance": 160},
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(self.account.deposit(test_case["amount"]), test_case["expected_balance"])

    def test_deposit_multiples_amounts_with_log(self):
        test_cases = [
            {"amount": 10, "expected_balance": 110},
            {"amount": 20, "expected_balance": 130},
            {"amount": 30, "expected_balance": 160},
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(self.account.deposit(test_case["amount"]), test_case["expected_balance"])
        self.assertEqual(self._count_line(self.TEST_FILE_NAME), 4)

    def test_deposit_multiples_amounts_with_new_account_in_subtest(self):
        test_cases = [
            {"amount": 10, "expected_balance": 110},
            {"amount": 20, "expected_balance": 120},
            {"amount": 30, "expected_balance": 130},
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.account = BankAccount(100, self.TEST_FILE_NAME)
                self.assertEqual(self.account.deposit(test_case["amount"]), test_case["expected_balance"])

        self.assertEqual(self._count_line(self.TEST_FILE_NAME), 7)
