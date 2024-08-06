import bge
from Timer import Timer
from collections import OrderedDict
from mathutils import Matrix, Quaternion

class ToBalance(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        self.scene = bge.logic.getCurrentScene()
        self.gangorra = self.object.children[0]
        self.time = Timer()
        self.initialOrientation = self.object.localOrientation.copy()
        pass

    def update(self):
        player = self.scene.objects.get("Player")
        if player:
            if self.gangorra.collide(player):
                distance = self.object.getDistanceTo(player) / 1500
                time = self.time.get()
                force = distance * time

                if self.object["Esquerda"]:
                    self.object.applyRotation([-force, 0, 0], True)
                elif self.object["Direita"]:
                    self.object.applyRotation([force, 0, 0], True)
                else:
                    self.time.reset()
                    self.smooth_return_to_initial()

        else:
            print("Player não encontrado")
        pass

    def smooth_return_to_initial(self):
        currentOrientation = self.object.localOrientation
        initialOrientation = self.initialOrientation

        currentQuat = currentOrientation.to_quaternion()
        initialQuat = initialOrientation.to_quaternion()

        interpolation = 0.01

        newOrientation = currentQuat.slerp(initialQuat, interpolation)

        self.object.localOrientation = newOrientation.to_matrix().to_3x3()
