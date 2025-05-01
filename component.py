# class Component:
#     def __init__(self, name, volume, material, index):
#         self.name = name
#         self.volume = volume
#         self.material = material
#         self.index = index
# In component.py
class Component:
    def __init__(self, name, volume, width, height, material, index = None):
        self.name = name
        self.volume = volume
        self.width = width
        self.height = height
        self.material = material
        self.index = index


    def __repr__(self):
        return f"Component({self.name}, Vol: {self.volume}, Mat: {self.material})"
