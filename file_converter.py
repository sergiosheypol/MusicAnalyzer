import os
import json
from pathlib import Path

class FileConverter():
    def __init__(self, folder_path):
        # Where to find the mp3 files
        self.path = Path(folder_path)

    # Method: converts the python dictionary 'py_list' into a json file named 'file_name'
    def py_to_json(self, py_list, file_name):

        # Where to create the json file
        output_path = self.path / file_name

        # Takes the python dictionary and produces a string
        json_string = json.dumps(py_list)

        # If the path does not exist, create it
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        # Converts the string into a json file
        with open(output_path, 'w') as outfile:
            json.dump(json_string, outfile)

    # Method: Converts an EXISTING json file named 'file_name into a python dictionary
    def json_to_py(self, file_name):

        # Where to find the json file
        output = self.path / file_name

        # If the path exist, converts the json file into a python dictionary and returns it
        if os.path.exists(self.path):
            with open(output) as data_file:
                py_string = json.load(data_file)  # json to

            py_List = json.loads(py_string)  # String to Python dictionary
            return py_List

        # Otherwise do not return anything
        return None

# # Method trials
# a = FileConverter('output')
# libpy = {
#     'LUFS': -13,
#     'TP': 2
# }
# a.py_to_json(libpy, 'bbb.json')
# b = FileConverter('output')
# x = b.json_to_py('bbb.json')
# print(x)
