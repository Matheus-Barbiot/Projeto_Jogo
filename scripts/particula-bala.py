import bge
from collections import OrderedDict

class Particula(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        pass

    def update(self):
        self.object.localScale = [
            self.object['escala'], 
            self.object['escala'], 
            self.object['escala'],
        ]
        
        if self.object["escala"] <= 0:
            self.object.endObject()
        pass
