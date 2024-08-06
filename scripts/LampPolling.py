import bge

class LampPooling(bge.types.KX_PythonComponent):
    args = []

    def start(self, args):
        self.scene = bge.logic.getCurrentScene()
        self.list = []
        self.listLamp = []
        self.initialLampPosition = [0, 0, -60]

    def update(self):
        self.list = [obj for obj in self.scene.objects if obj.name == "inimigo" or obj.name == "inimigo_longaDistancia"]
        self.listLamp = [lamp for lamp in self.scene.objects if "inimigo_lamp" in lamp.name]

        if len(self.listLamp) > len(self.list):
            dif = len(self.listLamp) - len(self.list)
            listSbr = self.listLamp[-dif:]
            for obj in listSbr:
                obj.worldPosition = self.initialLampPosition

        for n, enemy in enumerate(self.list):
            if n < len(self.listLamp):
                if not enemy.invalid:
                    self.listLamp[n].worldPosition = enemy.worldPosition
                else:
                    self.listLamp[n].worldPosition = self.initialLampPosition

