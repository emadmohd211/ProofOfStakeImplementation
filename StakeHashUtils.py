import hashlib
import json


class StakeHashUtils():

    @staticmethod
    def hash(data):
        data_String = json.dumps(data)
        data_Bytes = data_String.encode('utf-8')
        data_Hash = hashlib.sha256(data_Bytes)
        return data_Hash