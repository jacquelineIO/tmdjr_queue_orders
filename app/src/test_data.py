import os
import json
import jsonpickle
"""
import json
a = [1,2,3]
with open('test.txt', 'w') as f:
    f.write(json.dumps(a))

#Now read the file back into a Python list object
with open('../data/test.txt', 'r') as f:
    a = json.loads(f.read())
"""

def load_test_data():
    data_path = os.path.abspath(os.path.dirname(__file__)) + '/../data'
    file_name = data_path + '/text_jul31.dump' # 21 orders
    #file_name = data_path + '/text_jul25.dump' # 9 orders
    #file_name = data_path + '/text_jul27.dump' # 2 orders
    #file_name = data_path + '/text_jul26.dump' # 17 orders
    with open(file_name, 'r') as f:
        a = json.loads(f.read())
        decoded_data = jsonpickle.decode(a)
        return decoded_data

