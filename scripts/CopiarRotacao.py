import bge
from collections import OrderedDict

class CopiarRotacao(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ("Object", ""),
    ])

    def start(self, args):
        self.objAlvoName = args["Object"]
        self.scene = bge.logic.getCurrentScene()
        
        if self.objAlvoName in self.scene.objects:
            self.objAlvo = self.scene.objects[self.objAlvoName]
            self.object.worldOrientation = self.objAlvo.worldOrientation
        pass

    def update(self):
        
        pass
