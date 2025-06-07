import random
import threading
import time


class Car:
    def __init__(self, make, model, year, max_gas=50):
        self.make = make
        self.model = model
        self.year = year
        self.max_gas = max_gas
        self.gas_left = max_gas
        self.speed = 0

        self.distance_traveled = 0
        self.crashed = False
        self.reached_home = False

    def speed_up(self):
        if self.gas_left > 0:
            self.speed += random.randint(5, 15)
            self.gas_left -= 1
            self.distance_traveled += self.speed * 0.1
            print(f"Speeding up! Speed: {self.speed} mph")
        else:
            print("Out of gas")

    def slow_down(self, amount):
        self.speed = max(0, self.speed - amount)
        print(f"Slowing down by {amount} mph. Speed: {self.speed} mph")
