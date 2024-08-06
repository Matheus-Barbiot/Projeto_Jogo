import bge
from collections import OrderedDict

class lifebar(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ("Key", ""),
    ("Var", "")
    ])

    def start(self, args):
        self.key = args["Key"]
        self.var = args["Var"]
        pass

    def update(self):
        self.object[self.var] = bge.logic.globalDict[self.key]
        pass
