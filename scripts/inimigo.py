import bge
import mathutils
from random import choice
from collections import OrderedDict

class inimigo(bge.types.KX_PythonComponent):
    args = OrderedDict([
        ("Speed", 0.0),
        ("Distance", 0),
    ])

    def start(self, args):
        self.scene = bge.logic.getCurrentScene()
        self.character = bge.constraints.getCharacter(self.object)
        self.player = self.scene.objects.get("Player")
        
        for n in self.object.children: 
            if "inimigo_armadura" in n.name:
                self.armadura = n
        self.hit = self.scene.objects.get("inimigo_ataqueHit")
        
        self.speed = args["Speed"]
        self.distance = args["Distance"]
        self.minDistance = choice([3,4,5,6])
        
        self.Near = self.object.sensors['Near']
        self.NearMin = self.object.sensors['NearMin']
        
        self.Seguir = self.object.actuators['seguirPlayer']
        self.Seguir.distance = self.minDistance + 0.5
        
        self.Near.distance: self.Near.resetDistance = self.distance
        self.NearMin.distance: self.Near.resetDistance = self.minDistance
        
    def seguir(self):
        escolha = self.object["escolha"]
        
        if escolha == 1:
            if self.object.getDistanceTo(self.player) < self.minDistance + 0.5: 
                self.armadura["Andar"] = True 
                self.armadura["direcao"] = 1
                self.object.applyMovement([self.speed, 0, 0], True)
        elif escolha == 2:
            if self.object.getDistanceTo(self.player) < self.minDistance + 0.5: 
                self.armadura["Andar"] = True
                self.armadura["direcao"] = -1
                self.object.applyMovement([-self.speed, 0, 0], True)
        elif escolha == 3:
            self.armadura["Atacar"] = True
            self.armadura["Andar"] = False
            self.armadura["direcao"] = 0
            if self.object["AtaqueTemp"] >= 0.6:
                if self.hitAtaque:
                    self.hitAtaque["ataque"] = True
                    self.object.applyMovement([0, 0.2, 0], True)
                else:
                    pass
 
        else:
            self.object["avistado"] = False
            self.parar()
        
    def parar(self):
        if self.object["avistado"] == False:
            self.armadura["Andar"] = False
        self.armadura["Atacar"] = False
        self.armadura["direcao"] = 0
        self.object["AtaqueTemp"] = 0.0
        self.object["escolha"] = 0
        if self.hitAtaque:
            self.hitAtaque["ataque"] = False
        self.character.walkDirection = mathutils.Vector([0,0,0])
        
    def update(self):
        for obj in self.object.children["inimigo_armadura"].children:
            if obj.name == "inimigo_espadaHit":
                self.hitAtaque = obj
            elif obj.name == "inimigo_ataqueHit":
                self.hitAtaque = obj
            else:
                pass
            
        if self.player:
            if self.object.getDistanceTo(self.player) < 25:
                self.object["avistado"] = True
                
                if self.object["avistado"] == True:
                    self.armadura['Andar'] = True
                    
                    if self.object.getDistanceTo(self.player) < self.minDistance + 0.5:  
                        self.seguir()
                    else:
                        self.armadura["direcao"] = 0
                        self.object["escolha"] = 0
                
                else:
                    self.parar()
        else:
            return
        
        pass
