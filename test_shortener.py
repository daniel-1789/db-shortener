import unittest
from shortener import shorten_url


class ShortenUrl(unittest.TestCase):
    def test_shorten(self):
        shortened_url_1 = shorten_url('https://example.com', 'foo')
        shortened_url_2 = shorten_url('https://example.com', 'bar')

        self.assertEqual(shortened_url_1, shortened_url_2)


        shortened_url_3 = shorten_url('https://starwars.com', 'anakin')

        self.assertNotEqual(shortened_url_1, shortened_url_3)


if __name__ == '__main__':
    unittest.main()
