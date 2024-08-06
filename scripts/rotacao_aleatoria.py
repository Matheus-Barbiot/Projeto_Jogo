import bge
from collections import OrderedDict

class Rotacao(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        pass

    def update(self):
        self.object.worldOrientation = [
        self.object['rotationX'],
        self.object['rotationY'],
        self.object['rotationZ'],
        ]
        
        self.object.localOrientation = [
        self.object['rotationX'] * 1.5,
        self.object['rotationY'] * 1.5,
        self.object['rotationZ'] * 1.5,
        ]
        pass
        pass
