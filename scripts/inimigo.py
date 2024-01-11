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
        self.character = bge.constraints.getCharacter(self.object)
        self.scene = bge.logic.getCurrentScene()
        
        for n in self.object.children: 
            if "armadura" in n.name:
                self.armadura = n

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
            # se ele chegar perto do player       
            # se ele avistar o player
            if self.object.getDistanceTo(player) < self.distance and not self.object.getDistanceTo(player) < self.minDistance:
                vetor = mathutils.Vector(player.worldPosition - self.object.worldPosition)
                self.character.walkDirection = vetor.normalized() * self.speed
                self.armadura["Andar"] = True
            
            elif self.object.getDistanceTo(player) < self.minDistance:
                self.character.walkDirection = mathutils.Vector([0,0,0])
                self.armadura["Andar"] = False; self.armadura["direcao"] = 0
                escolha = self.object["escolha"]
                
                if escolha == 0:
                    self.character.walkDirection = mathutils.Vector([0,0,0])
                    self.armadura["Andar"] = False; self.armadura["direcao"] = 0
                if self.Ray.hitObject == None:
                    if escolha == 1:
                        self.object.applyMovement([self.speed, 0, 0], True)
                        self.armadura["Andar"] = True; self.armadura["direcao"] = 1
                        
                    if escolha == 2:
                        self.object.applyMovement([-self.speed, 0, 0], True)
                        self.armadura["Andar"] = True; self.armadura["direcao"] = -1
                else:
                    escolha = 0
            # se ele não ver ou perder o player
            else:
                self.character.walkDirection = mathutils.Vector([0,0,0])
                self.armadura["Andar"] = False
                return
        
        
    def update(self):
        self.seguir()
