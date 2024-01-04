import bge
import mathutils
from collections import OrderedDict

class Player(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        self.character = bge.constraints.getCharacter(self.object)
        self.keyboard = bge.logic.keyboard.inputs
        pass
    
    def _teclas(self):
        self.WKEY = self.keyboard[bge.events.WKEY].active
        self.SKEY = self.keyboard[bge.events.SKEY].active
        self.AKEY = self.keyboard[bge.events.AKEY].active
        self.DKEY = self.keyboard[bge.events.DKEY].active
        pass
    
    
    def movimento(self):
        self._teclas()
        y = self.WKEY - self.SKEY
        x = self.DKEY - self.AKEY
        vetor = [x, y, 0]
        self.character.walkDirection = mathutils.Vector(vetor) * 0.2
        
    def update(self):
        self.movimento()
        pass
