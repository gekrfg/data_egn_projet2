import json
import unittest
import requests
import time
import os


class FlaskTests(unittest.TestCase):
    def setUp(self):
        os.environ['NO_PROXY'] = '0.0.0.0'
        pass

    def tearDown(self):
        pass

    def test_stress(self):
        count = 1000

        params = {
            'sentence': "I'm feeling really good!",
            "form_type": "analysis_sentence"
        }

        kaishi = time.time()

        for i in range(1000):
            responce = requests.post('http://localhost:5000', data=params)
            self.assertEqual(responce.status_code, 200)
        
        jieshu = time.time()

        t = jieshu - kaishi


        print("The {} requests took: {} seconds".format(count, t))


if __name__ == '__main__':
    unittest.main()
