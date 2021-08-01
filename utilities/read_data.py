import json
import os
def JSON_Reader(path,key=""):
    with open(path) as data_file:
        data = json.load(data_file)
        test_data = (data[key])
        return test_data


