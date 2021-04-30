import re
from pyyaml import load,FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimeter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter,re.MULTILINE)

    @classmethod
    def load(cls,string):
        _,fm,content = __regex.split(string,2)
        metadata = load(fm,Loader = FullLoader)
        return cls(metadata,content)
    def __init__(self,metadata,content):
        self.data = {"content":content}
    @property
    def body():
        return self.data["content"]
    @property
    def type():
        return self.data["type"] if self.data.has_key("type") else None
    @type.setter
    def type(self,type):
        self.data["type"] = type
    def __getitem__(self,key):
        return self.data[key]
    def __iter__(self):
        self.data.__iter__()
    def __len__(self):
        len(self.data)
    def __repr__(self):
        data = {}
        return str(data)
