from webapp import string_similar, get_similar_tweets
import unittest
import os
import requests


class FlaskTests(unittest.TestCase):

    def setUp(self):
        os.environ['NO_PROXY'] = '0.0.0.0'
        self.text = {
            'sentence': "I love you!",
        }
        pass

    def tearDown(self):
        pass

    def test_a_webpage(self):
        response = requests.get('http://localhost:5000')
        self.assertEqual(response.status_code, 200)

    def test_b_send(self):
        params = {
            'sentence': self.text['sentence'],
            "form_type": "analysis_sentence"
        }
        response = requests.post('http://localhost:5000', data=params)
        self.assertEqual(response.status_code, 200)

    def test_c_send(self):
        params = {
            'sentence': self.text['sentence'],
            "form_type": "analysis_sentence"
        }
        response = requests.post('http://localhost:5000', data=params)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
