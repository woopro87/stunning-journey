import unittest

from vending_machine import VendingMachine


class TestVendingMachine(unittest.TestCase):
    def test_insert_coin_increases_balance(self):
        machine = VendingMachine()
        machine.insert_coin(500)
        self.assertEqual(machine.balance, 500)

    def test_insert_invalid_coin_raises_error(self):
        machine = VendingMachine()
        with self.assertRaises(ValueError):
            machine.insert_coin(50)

    def test_purchase_reduces_balance_and_stock(self):
        machine = VendingMachine()
        machine.insert_coin(1000)
        drink_name = machine.purchase("1")

        self.assertEqual(drink_name, "콜라")
        self.assertEqual(machine.balance, 300)
        self.assertEqual(machine.drinks["1"]["stock"], 4)

    def test_purchase_with_insufficient_balance_raises_error(self):
        machine = VendingMachine()
        machine.insert_coin(100)
        with self.assertRaises(ValueError):
            machine.purchase("1")

    def test_purchase_with_invalid_drink_code_raises_error(self):
        machine = VendingMachine()
        machine.insert_coin(1000)
        with self.assertRaises(ValueError):
            machine.purchase("999")

    def test_purchase_with_no_stock_raises_error(self):
        machine = VendingMachine()
        machine.drinks["1"]["stock"] = 0
        machine.insert_coin(1000)
        with self.assertRaises(ValueError):
            machine.purchase("1")

    def test_refund_resets_balance(self):
        machine = VendingMachine()
        machine.insert_coin(1000)
        refunded = machine.refund()

        self.assertEqual(refunded, 1000)
        self.assertEqual(machine.balance, 0)


if __name__ == "__main__":
    unittest.main()
