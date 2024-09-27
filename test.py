import unittest
from unittest.mock import patch
from main import get_random_cat_image  # Замените на имя вашего модуля

class TestCatAPI(unittest.TestCase):

    @patch('requests.get')
    def test_successful_request(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'url': 'http://example.com/cat.jpg'}]

        result = get_random_cat_image()
        self.assertEqual(result, 'http://example.com/cat.jpg')

    @patch('requests.get')
    def test_unsuccessful_request(self, mock_get):
        mock_get.return_value.status_code = 404

        result = get_random_cat_image()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()