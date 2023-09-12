import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from app.banking_app import Banking

class Tdd_Python(unittest.TestCase):
    def setUp(self):
       self.bank = Banking()

    def test_banking_credit_method_return_correct_result(self):
        final_bal = self.bank.credit(1000)
        self.assertEqual(1000, final_bal)

    def test_banking_credit_method_returns_error_if_args_not_numbers(self):
       self.assertRaises(ValueError, self.bank.credit, "two")

    def test_banking_debit_method_returns_correct_result(self):
       final_bal = self.bank.debit(700)
       self.assertEqual(-700, final_bal)

    def test_banking_debit_method_returns_error_if_args_not_numbers(self):
       self.assertRaises(ValueError, self.bank.debit, "two")

if __name__ == '__main__':
 unittest.main()


 