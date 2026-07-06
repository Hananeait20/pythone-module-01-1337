from ft_garden_security import Plant
class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False
    
    def show(self):
        super().show()
        print("color: ",self.color)
        if self.bloomed:
            print(self.name, "is blooming beautifully!")
        else:
            print(self.name, "has not bloomed yet")

    def bloom(self):
        self.bloomed = True
        
class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.get_height()}cm long and "
            f"{self.trunk_diameter}cm wide."
        )

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")
        
class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.value = 0

    def grow(self):
        super().grow()
        self.value += 10

    def age(self, days):
        super().age(days)
        self.value += 10

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.value}")

print("=== Garden Plant Types ===")
#---------------------------------
print("=== Flower")
rose = Flower("Rose",15, 10,"red")
rose.show()
rose.bloom()
print("[asking the rose to bloom]")
rose.show()
#----------------------------------------
print("\n=== Tree ===")
oak = Tree("Oak", 200.0, 365, 5.0)
oak.show()

print("[asking the oak to produce shade]")
oak.produce_shade()
#-------------------------------------------
print("\n=== Vegetable ===")
tomato = Vegetable("Tomato", 5.0, 10, "April")
tomato.show()

print("[make tomato grow and age for 20 days]")
tomato.grow()
tomato.age(20)
tomato.show()