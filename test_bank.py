import unittest
from concurrent.futures import ThreadPoolExecutor
from bank import Account
from config import DEFAULT_BALANCE

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account("TestUser")

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), DEFAULT_BALANCE)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), DEFAULT_BALANCE + 500)

    def test_withdrawal(self):
        self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), DEFAULT_BALANCE - 100)

    def test_withdrawal_limit_exceeded(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1000)

    def test_insufficient_funds(self):
        acc = Account("PoorGuy", 100)
        with self.assertRaises(ValueError):
            acc.withdraw(150)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_negative_withdrawal(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

def run_single_test(test):
    test_name = test._testMethodName
    print(f"\nRunning test: {test_name}")
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test)
    return result

if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromTestCase(TestAccount)

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(run_single_test, test) for test in tests]
        for future in futures:
            future.result()
