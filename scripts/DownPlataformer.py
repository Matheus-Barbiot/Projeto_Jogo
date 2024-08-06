import bge
from Timer import Timer
from collections import OrderedDict

class Plataform(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ("Obj", ""),
    ("Temp", 1.0),
    ])

    def start(self, args):
        self.scene = bge.logic.getCurrentScene()
        self.active = False
        self.objSubs = args["Obj"]
        self.temp = args["Temp"]
        self.timer = Timer()
        pass
    def state2(self):
        self.object.playAction("Plataforma_Acair", 0, 4, play_mode=2)
        if self.timer.get() > self.temp:
            self.newObj = self.scene.addObject(self.objSubs, self.object, 100)
            self.object.endObject()
            
            
    def update(self):
        self.player = self.scene.objects["Player"]
        if self.object.collide(self.player)[0]:
            self.active = True
            
        if self.active == True:
            self.state2()
        else:
            self.timer.reset()
        pass
