import json
import os

def loadJsonData(file_path):
    blank_json = {}
    if os.path.exists(file_path):
        try:
            f = open(file_path, "r")
            data = json.load(f)
            f.close()
            return data
        except ValueError: 
            print("Decode error")
            return blank_json
    else:
     return blank_json    

def saveJsonData(file_path, data):
    blank_json = {}
    stringified_json_data = json.dumps(data)
    f = open(file_path, "w")
    f.write(stringified_json_data)
    f.close() 
    return True