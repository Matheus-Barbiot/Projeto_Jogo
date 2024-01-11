import bge
from random import choice
from collections import OrderedDict

class armadura(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        self.tipo = choice(['tipo 1', 'tipo 2', 'tipo 3'])
        self.walk = self.object.actuators["walk"]
        self.idle = self.object.actuators["idle"]
        
        #Chapeu aleatorio:
        escolha = choice([True, False])
        for obj in self.object.children:
            if "chapeu" in obj.name:
                if escolha == True:
                    obj.endObject()
        
        if self.tipo == "tipo 1":
            self.walk.action = "inimigo_andar1"
            self.idle.action = "inimigo_andar1"
            
        elif self.tipo == "tipo 2":
            self.walk.action = "inimigo_andar2"
            self.idle.action = "inimigo_andar2"
            
        else:
            self.walk.action = "inimigo_andar3"
            self.idle.action = "inimigo_andar3"
        pass

    def update(self):
        pass

