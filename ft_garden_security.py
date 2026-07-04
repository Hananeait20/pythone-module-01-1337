class Plant:
    def __init__(self, name, height, age):
        self.name = name
        if height >=0:
            self._height = height
        else:
            print(self.name, ": Error, height can't be negative")
            self._height = 0
        if age >=0:
           self._age = age
        else:
            print(self.name, ": Error, age can't be negative")
            self._age = 0
    def show(self):
        print(self.name, ":", self._height,'cm', self._age, "days old")
    
    def get_height(self):
        return self._height
    def get_age(self):
        return self._age
    def set_height(self,height):
        if height >= 0:
            self._height = height
            print("Height updated: ", height,"cm")      
        else:
            print(self.name, ": Error, height can't be negative")
            print("Height update rejected")
    def set_age(self,age):
        if age >= 0:
            self._age = age
            print("Age updated: ", age, "days")
        else:
            print(self.name,": Error, age can't be negative")
            print("Age update rejected")
print("=== Garden Security System ===")
rose = Plant("rose", -2, 30)
#jasmin = Plant("jasmin", 25, 30)
#flow = Plant("flow", 25, 30)
print("Plant created:", end=" ")
rose.show()

rose.set_height(25)
rose.set_age(30)
print("Current state:", end=" ")
rose.show()
#jasmin.show()
#flow.show()