import bge
import mathutils
from collections import OrderedDict

class Player(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ("Speed", 0.0)
    ])

    def start(self, args):
        self.character = bge.constraints.getCharacter(self.object)
        self.keyboard = bge.logic.keyboard.inputs
        self.scene = bge.logic.getCurrentScene()
        
        self.speed = args["Speed"]
        pass
    
    def _teclas(self):
        self.WKEY = self.keyboard[bge.events.WKEY].active
        self.SKEY = self.keyboard[bge.events.SKEY].active
        self.AKEY = self.keyboard[bge.events.AKEY].active
        self.DKEY = self.keyboard[bge.events.DKEY].active
        self.SPACE = self.keyboard[bge.events.SPACEKEY].activated
        pass
    
    
    def movimento(self):
        self._teclas()
        y = self.WKEY - self.SKEY
        x = self.DKEY - self.AKEY
        vetor = [x, y, 0]
        self.character.walkDirection = mathutils.Vector(vetor).normalized() * self.speed
        if self.SPACE: self.character.jump()
        
        
    def vida(self):
        bge.logic.globalDict["PlayerLife"] = self.object["vida"]
    def update(self):
        self.movimento()
        self.vida()
        pass
