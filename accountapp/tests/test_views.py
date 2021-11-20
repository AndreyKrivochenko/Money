from django.test import TestCase, Client


class AccountAppMainTemplateTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_context_account(self):
        response = self.client.get('/account/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['title'], 'Счета')

    def test_context_services(self):
        response = self.client.get('/account/services/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['title'], 'Услуги')

    def test_context_property(self):
        response = self.client.get('/account/property/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['title'], 'Имущество')
