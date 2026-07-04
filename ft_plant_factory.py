class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.age = age
        self.height = height
    def show(self):
        
        print(self.name, ":", self.height,'cm', self.age, "days old")
print("=== Plant Factory Output ===")
rose = Plant("rose", 25, 30)
jasmin = Plant("jasmin", 25, 30)
flow = Plant("flow", 25, 30)
rose.show()
jasmin.show()
flow.show()