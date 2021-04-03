from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    def test_one_page_status_code(self):
        response = self.client.get('/one_page/')
        self.assertEqual(response.status_code, 200)
    def test_second_page_status_code(self):
        response = self.client.get('/second_page/')
        self.assertEqual(response.status_code, 200)
    def test_three_page_status_code(self):
        response = self.client.get('/three_page/')
        self.assertEqual(response.status_code, 200)
    def test_six_page_status_code(self):
        response = self.client.get('/six_page/')
        self.assertEqual(response.status_code, 200)

