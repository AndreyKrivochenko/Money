from django.test import TestCase, Client


class MainAppMainTemplateTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_context(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['title'], 'Главная')
