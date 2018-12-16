import requests
from datetime import datetime
from weightin.common.constant import data_post_field
import json

class WIClient:
    application_name = 'weightin'

    def __init__(self,host,port):
        self.host, self.port = host, port
        self.app_info = {'application_name': 'weightin'}
    
    def get_url(self, api):
        return "http://{}:{}/{}".format(self.host, self.port, api)

    def request_add_weight(self, obj):
        url = self.get_url('add_data')
        data = dict()
        data.update(**self.app_info)
        data[data_post_field] = json.dumps(obj)
        result = requests.post(url, data=data)
        return result

    def request_get_data(self):
        url = self.get_url('get_data')
        result = requests.post(url, data=self.app_info)
        return result

    def request_delete_data(self, obj):
        url = self.get_url('delete_data')
        result = requests.post(url, data=obj)
        return result

    def get_plot(self, obj):
        url = self.get_url('get_plot')
        result = requests.post(url, data={})
        return result

    def delete_by_date(self, dates):
        url = self.get_url('delete_by_date')
        result = requests.post(url, data={})
        return result
