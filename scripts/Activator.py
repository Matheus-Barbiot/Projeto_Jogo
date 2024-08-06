import bge
from collections import OrderedDict

class Activator(bge.types.KX_PythonComponent):
    args = OrderedDict([
        ("Target Object", ""),
        ("Property Name", ""),
        ("Initial Value", False),
        ("Activator Object", ""),
    ])

    def start(self, args):
        self.scene = bge.logic.getCurrentScene()
        self.target_object = self.scene.objects.get(args["Target Object"])
        self.activator_object_name = args["Activator Object"]
        
        self.property_name = args["Property Name"]
        self.initial_value = args["Initial Value"]
        
        self.target_object[self.property_name] = self.initial_value

    def update(self):
        try:
            obj = self.scene.objects[self.activator_object_name]
        except:
            obj = None
        
        if obj:
            if self.target_object in self.scene.objects:
                if self.object.getDistanceTo(obj) < 2:
                    self.target_object[self.property_name] = True
                    obj.endObject()
                    self.object.endObject()
            else:
                return
        pass
        
