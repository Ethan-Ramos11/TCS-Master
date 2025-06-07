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
            self.speed += random.randint(30, 50)
            self.gas_left -= 1
            self.distance_traveled += self.speed * 0.1
            print(f"Speeding up! Speed: {self.speed} mph")
        else:
            print("Out of gas")

    def slow_down(self, amount):
        self.speed = max(0, self.speed - amount)
        print(f"Slowing down by {amount} mph. Speed: {self.speed} mph")

    def brake_fully(self):
        self.speed = 0
        print("Full stop. speed: 0mph")

    def reverse(self):
        if self.gas_left > 0:
            self.speed = -random.randint(3, 8)
            self.gas_left -= 1
            self.distance_traveled += abs(self.speed) * .05
        else:
            print("Out of gas")

    def gas_up(self, amount):
        old_gas = self.gas_left
        self.gas_left = min(self.max_gas, self.gas_left + amount)
        amount_filled = self.gas_left - old_gas
        print(
            f"Added {amount_filled} gallons of gas. Gas left: {self.gas_left}/{self.max_gas}")

    def display_stats(self):
        print(f"\n{self.year} {self.make} {self.model}")
        print(f"   Speed: {self.speed} mph")
        print(f"   Gas: {self.gas_left}/{self.max_gas} gallons")
        print(f"   Distance: {self.distance_traveled:.2f} miles")


class RandomCarSimulator:
    def __init__(self, car: Car):
        self.car = car
        self.running = False
        self.outcome = None

    def random_action(self):
        actions = [
            self.car.speed_up,
            lambda: self.car.slow_down(random.randint(5, 20)),
            self.car.brake_fully,
            self.car.reverse,
            lambda: self.car.gas_up(random.randint(1, 5))
        ]
        action = random.choice(actions)
        action()

        self.check_for_events()

    def check_for_events(self):
        crash_chance = max(0, (self.car.speed - 20) * 0.02)

        if random.random() < crash_chance:
            self.car.crashed = True
            self.outcome = "CRASH! You were going too fast!"
            self.running = False
            return

        if self.car.distance_traveled > 20 and random.random() < 0.6:
            self.car.reached_home = True
            self.outcome = "Made it home safely"
            self.running = False
            return

        if self.car.gas_left == 0 and self.car.speed == 0:
            self.outcome = "Ran out of gas and am stuck"
            self.running = False
            return

    def run_simulation(self, duration=15):
        print(f"\nStarting {duration}-second random car simulation")
        print("=" * 50)

        self.running = True
        start_time = time.time()

        while self.running and (time.time() - start_time) < duration:
            self.random_action()
            self.car.display_stats()

            if not self.running:
                break

            time.sleep(1)
        if self.running:
            self.outcome = "Time's up! Nothing interesting happened"

        print("\n" + "=" * 50)
        print(f"Simulation ended: {self.outcome}")
        print("=" * 50)


def main():
    print("Welcome to the random car simulator")
    print("=" * 50)

    cars = [
        ("Toyota", "Camry"),
        ("Toyota", "Corolla"),
        ("Honda", "Civic"),
        ("BMW", "M3"),
        ("Porsche", "GT3RS"),
        ("Ford", "Mustang")
    ]
    make, model = random.choice(cars)
    year = random.randint(2015, 2024)
    max_gas = random.randint(12, 20)

    car = Car(make, model, year, max_gas)
    car.display_stats()

    simulator = RandomCarSimulator(car)

    input("\nPress enter to start the random simulation...")

    simulator.run_simulation()

    print("\nFinal car status:")
    car.display_stats()


if __name__ == "__main__":
    main()
