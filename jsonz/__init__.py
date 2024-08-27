from abc import ABC, abstractmethod
import os, sys, json

"""
https://github.com/python/cpython/blob/main/Lib/json/__init__.py
"""

class core_json(ABC):
    def __load_file(self, fp):
        if not os.path.exists(fp):
            return None
        with open(fp, 'r') as reader:
            return reader.readlines()
    @property
    @abstractmethod
    def load(fp):
        pass

class jsonc(object):
    @property
    def load(fp):
        return json.loads([
            x
            for x in self.__load_file(fp)
            if not x.startswith("//")
        ])
class jsonl(object):
    @property
    def load(fp):
        output = []
        for content_line in self.__load_file(fp):
            try:
                output += [
                    json.loads(content_line)
                ]
            except Exception as e:
                print(e)
        return output

def load_json(file:str):
    if not os.path.exists(file):
        return None
    if file.endswith(".jsonc"):
        return jsonc.load(file)
    elif file.endswith(".jsonl"):
        return jsonl.load(file)
    if file.endswith(".json"):
        with open(file, "r") as reader:
            return json.load(reader)
    return None