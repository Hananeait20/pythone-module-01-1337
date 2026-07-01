#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.age = age
        self.height = height
    def affiche(self):
        
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
    #that is for exercice ft_plant_growth
    def grow(self):
        self.height += 0.8
    def age_one_day(self):
        self.age += 1
        
if __name__ == "__main__": 
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower",  80, 45)
    plant3 = Plant("Cactus", 15, 120)
    print("===Garden Plant Registry===")
    plant1.affiche()
    plant2.affiche()
    plant3.affiche()