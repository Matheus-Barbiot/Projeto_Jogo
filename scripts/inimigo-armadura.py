import bge
from random import choice
from collections import OrderedDict

class armadura(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])
    
    def start(self, args):
        #Itens:
        chapeu = choice([True, False]) # define se o chapéu irá aparecer
        espada = choice([True, False]) # define se a espada irá aparecer
        
        self.tipo = choice(['tipo 1', 'tipo 2', 'tipo 3', 'tipo 4'])
        self.walk = self.object.actuators["walk"]
        self.idle = self.object.actuators["idle"]
        
        for obj in self.object.children:
            if "chapeu" in obj.name:
                if chapeu == False:
                    obj.endObject()
        for item in self.object.children:
            if "Inimigo_espada" == item.name:
                itemEspada = item

            if "inimigo_espadaHit" == item.name:
                hitEspada = item
                
            if "inimigo_ataqueHit" == item.name:
                hitAtaque = item
            
            if "inimigo_escudo" == item.name:
                hitEscudo = item
        
        if self.tipo == "tipo 1":
            self.walk.action = "inimigo_andar1"
            self.idle.action = "inimigo_andar1"
            hitEscudo.endObject()
            if espada == False:
                itemEspada.endObject()
                hitEspada.endObject()
            else:
                hitAtaque.endObject()
            
        elif self.tipo == "tipo 2":
            self.walk.action = "inimigo_andar2"
            self.idle.action = "inimigo_andar2"
            hitEscudo.endObject()
            itemEspada.endObject()
            hitEspada.endObject()
        
        elif self.tipo == "tipo 3":
            self.walk.action = "inimigo_andar3"
            self.idle.action = "inimigo_andar3"
            hitEscudo.endObject()
            itemEspada.endObject()
            hitEspada.endObject()
        elif self.tipo == "tipo 4":
            self.walk.action = "inimigo_andar4"
            self.idle.action = "inimigo_andar4"
            if espada == False:
                itemEspada.endObject()
                hitEspada.endObject()
            else:
                hitAtaque.endObject()
        else:
            return
        
        pass

    def update(self):
        pass

