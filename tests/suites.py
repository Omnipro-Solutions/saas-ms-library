import unittest

from test_bank_account import TestBankAccount


def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestBankAccount("test_deposit"))
    suite.addTest(TestBankAccount("test_withdraw"))
    suite.addTest(TestBankAccount("test_get_balance"))
    suite.addTest(TestBankAccount("test_transaction_log"))
    suite.addTest(TestBankAccount("test_count_transaction_log"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(bank_account_suite())
