import unittest
from tests.helper import WIClient
from datetime import datetime, timedelta
import random

class WeightInTest(unittest.TestCase):

    def setUp(self):
        self.wi_client = WIClient('localhost',5000) 

    def test_add_weight(self):
        results = list()
        for i in range(1,20):
            obj = {'date' : datetime(2019,1,1) + timedelta(days=i),
                   'weight' : 80 + random.random() * 4}
            res = self.wi_client.request_add_weight(obj)
            results.append(res)
        print(results)


    def test_get_data(self):
        for i in range(1,20):
            obj = {'date' : datetime(2019,1,1) + timedelta(days=i),
                   'weight' : 80 + random.random() * 4}
            self.wi_client.request_add_weight(obj)
        data = self.wi_client.request_get_data()
        print(data)



