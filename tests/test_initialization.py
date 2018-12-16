import unittest
from tests.helper import WIClient
from datetime import datetime, timedelta
import random
from weightin.apps.weightin import FORMAT_DATE

class WeightInTest(unittest.TestCase):

    def setUp(self):
        self.wi_client = WIClient('localhost',8080) 

    def test_add_weight(self):
        results = list()
        for i in range(1,20):
            obj = {'date' : (datetime(2019,1,1) + timedelta(days=i)).strftime(FORMAT_DATE),
                   'weight' : 80 + random.random() * 4}
            res = self.wi_client.request_add_weight(obj)
            results.append(res)
        print(results)


    def test_get_data(self):
        data = self.wi_client.request_get_data()
        print("{}".format(data))



