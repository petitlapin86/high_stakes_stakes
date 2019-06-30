from unittest import TestCase
from wallet import Wallet

class WalletTestCase(TestCase):

    def setUp(self):
        self.test_wallet = Wallet(100)

    def test_initialWallet(self):
        current_amount = self.test_wallet.get_wallet()
        self.assertEqual(100, current_amount)
#
    def test_win(self):
        self.test_wallet.win(100)
        self.assertEqual(200, self.test_wallet.get_wallet())

    def test_lose(self):
        self.test_wallet.lose(50)
        self.assertEqual(50, self.test_wallet.get_wallet())
