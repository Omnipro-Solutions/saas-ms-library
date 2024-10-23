import os
import unittest

from faker import Faker
from src.bank_account import BankAccount
from src.user import User


class UserTest(unittest.TestCase):

    def setUp(self):
        self.fake = Faker(locale="es")
        self.user = User(self.fake.name(), self.fake.email())

    def tearDown(self):
        for x in self.user.accounts:
            if os.path.exists(x.log_file):
                os.remove(x.log_file)

    def test_user_creation(self):
        name = self.fake.name()
        email = self.fake.email()
        user = User(name, email)
        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)

    def test_user_with_multiple_accounts(self):

        for x in range(5):
            account = BankAccount(
                balance=self.fake.random_int(min=100, max=10000, step=100),
                log_file=self.fake.file_name(extension=".txt"),
            )
            account.deposit(100)
            self.user.add_account(account)

        expected_value = self.user.get_total_balance()
        value = sum(account.get_balance() for account in self.user.accounts)
        self.assertEqual(expected_value, value)
