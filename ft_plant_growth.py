#!/usr/bin/env python3
from ft_garden_data import Plant
print("=== Garden Plant Growth ===")
#u can initialise the other type of plant
rose = Plant("Rose", 25.0, 30)
rose.affiche()
height_before = rose.height
for day in range(1, 8):
    print(f"=== Day {day} ===")
    rose.grow()
    rose.age_one_day()

    rose.affiche()
growth = rose.height - height_before
print(f"Growth this week: {growth:.2f}cm")