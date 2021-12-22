from django.test import TestCase
from accountapp.models import AccountType, Account


class AccountTypeTestCase(TestCase):
    def setUp(self) -> None:
        AccountType.objects.create(title='Cash')
        Account.objects.create(account_type=AccountType.objects.get(title='Cash'), title='Наличка', summ=20)
        Account.objects.create(account_type=AccountType.objects.get(title='Cash'), title='Подушка', summ=80)

    def test_accounttype_get_full_summ(self):
        account_type = AccountType.objects.get(title='Cash')
        self.assertEqual(account_type.get_full_summ(), 100)
        self.assertNotEqual(account_type.get_full_summ(), 10)
