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
        
        for n in self.object.children: 
            if "armadura" in n.name:
                self.armadura = n
        self.hit = self.scene.objects.get("inimigo_ataqueHit")
        
        self.pulo = 0
        self.speed = args["Speed"]
        self.distance = args["Distance"]
        self.minDistance = choice([3,4,5,6])
        
        self.Ray = self.object.sensors['Radar']
        self.Near = self.object.sensors['Near']
        self.NearMin = self.object.sensors['NearMin']
        self.Near.distance: self.Near.resetDistance = self.distance
        self.NearMin.distance: self.Near.resetDistance = self.minDistance
        
    def seguir(self):
        player = self.scene.objects.get("Player")
        if player:
            if self.object.getDistanceTo(player) < self.distance:
                if self.object.getDistanceTo(player) > self.minDistance:
                    vetor = mathutils.Vector(player.worldPosition - self.object.worldPosition)
                    self.character.walkDirection = vetor.normalized() * self.speed
                    self.armadura["Andar"] = True
            
                else:
                    escolha = self.object["escolha"]
                    self.parar()
                    
                    if escolha == 3:
                        self.atacar()
                            
                    elif escolha == 1:
                        self.pulo = 0
                        self.object["ataqueTemp"] = 0.0
                        self.armadura["Andar"] = True 
                        self.armadura["direcao"] = 1
                        self.object.applyMovement([self.speed, 0, 0], True)
                        
                    elif escolha == 2:
                        self.pulo = 0
                        self.object["ataqueTemp"] = 0.0
                        self.armadura["Andar"] = True
                        self.armadura["direcao"] = -1
                        self.object.applyMovement([-self.speed, 0, 0], True)
                  
            else:
                self.parar()
                return
        
    def parar(self):
        self.character.walkDirection = mathutils.Vector([0,0,0])
        self.armadura["Andar"] = False
        self.armadura["direcao"] = 0
    
    def atacar(self):
        self.armadura["Andar"] = False
        self.armadura["direcao"] = 0
        if self.object["ataqueTemp"] > 0.7:
            self.hit["ataque"] = True
            if self.pulo == 0:
                self.object.applyMovement([0, 2, 0], True)
                self.character.jump()
                self.pulo += 1
            return
        
    def update(self):
        if self.NearMin.hitObject == None:
            self.object["escolha"] = 0 
            self.object["ataqueTemp"] = 0.0
        self.seguir()
