import pandas as pd
from dataclasses import dataclass
from dataclasses_dict import DataclassDictMixin
from dataclasses_json import DataClassJsonMixin
from datetime import datetime
import pymongo
from weightin.config import DbConfig
from .app import AppBase
import re
import matplotlib.pyplot as plt
import seaborn as sns
import json

from typing import Dict, List

FORMAT_DATE="%Y-%m-%d"
FORMAT_DATEHOUR="%Y-%m-%d %H"
FORMAT_DATETIME="%Y-%m-%d %H:%M:%S"
FORMAT_DATETIME_STANDARD="%Y-%m-%dT%H:%M:%S"

RE_FORMAT_DATE="\d{4}\-\d{2}\-\d{2}"
RE_FORMAT_DATEHOUR="\d{4}\-\d{2}\-\d{2}\b\d{2}"
RE_FORMAT_DATETIME="\d{4}\-\d{2}\-\d{2}\b\d{2}:\d{2}:\d{2}"
RE_FORMAT_DATETIME_STANDARD="\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}"

@dataclass
class WeightIn(DataClassJsonMixin,DataclassDictMixin):
    date: datetime 
    weight: float


class WeightInApp(AppBase):
    db_name = "weightin"
    name = "weightin"
    collections_list = ["weights"]
    weight_collection = "weights"

    @staticmethod
    def from_str_to_date(sdate):
        if isinstance(sdate,datetime):
            return sdate
        if re.match(RE_FORMAT_DATE,sdate):
            return datetime.strptime(sdate,FORMAT_DATE)
        elif re.match(RE_FORMAT_DATEHOUR,sdate):
            return datetime.strptime(sdate,FORMAT_DATEHOUR)
        elif re.match(RE_FORMAT_DATETIME,sdate):
            return datetime.strptime(sdate,FORMAT_DATETIME)
        elif re.match(RE_FORMAT_DATETIME_STANDARD,sdate):
            return datetime.strptime(sdate,FORMAT_DATE_STANDARD)
        else:
            raise Exception("Unkwon date format for {}".format(sdate))

    def __init__(self, dbconfig: DbConfig):
        super().__init__(dbconfig)

    def add_data(self, weightin: WeightIn):
        print(weightin.date)
        if isinstance(weightin.date,str):
            weightin.date = self.from_str_to_date(weightin.date) 
        w = weightin.to_dict()
        res = self.collections[self.weight_collection].insert_one(w)
        return res

    def delete_data(self, weightin: WeightIn):
        self.collections[self.weight_collection].remove(weightin.to_dict())

    def get_plot(self):
        data = pd.DataFrame([obj for obj in self.collections[self.weight_collection].find()])
        fig = sns.plot(x="date",y="weight",data=data)
        return fig

    def get_data(self):
        data = [obj for obj in self.collections[self.weight_collection].find()]
        return data

    def delete_by_date(self, date_list: List[datetime]):
        self.collections[self.weight_collection].remove({
            "date": list(map(self.from_str_date,date_list))
           })

    @staticmethod
    def to_object(dictlike: str):
        return WeightIn.from_dict(json.loads(dictlike))


