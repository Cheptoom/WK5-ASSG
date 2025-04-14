# Object-Oriented Programming (OOP) Example: Smartphone and Gaming Smartphone
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.powered_on = False

    def power_on(self):
        self.powered_on = True
        return f"{self.brand} {self.model} is now ON."

    def power_off(self):
        self.powered_on = False
        return f"{self.brand} {self.model} is now OFF."

    def make_call(self, number):
        if self.powered_on:
            return f"Calling {number} from {self.brand} {self.model}"
        else:
            return "Phone is off. Please power on first."

    def __str__(self):
        return f"{self.brand} {self.model} {self.storage}GB"
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage,cooling_system):
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system  

    def launch_game_mode(self):
        if self.powered_on:
            return f"Game Mode activated on {self.brand} {self.model} with {self.cooling_system} cooling."
        else:
            return "Phone is off. Cannot launch Game Mode."
# Polymorphism
    def make_call(self, number):
        if self.powered_on:
            return f"[Gaming Phone] Connecting to {number} with voice optimization"
        else:
            return "Phone is off. Please power on first."

    def __str__(self):
        return super().__str__() + f" Cooling: {self.cooling_system}"

if __name__ == "__main__":
    phone1 = Smartphone("Apple", "iPhone 14", 256)
    phone2 = GamingSmartphone("Samsung", "Galaxy S23", 512,"liquid")

    print(phone1)
    print(phone1.power_on())
    print(phone1.make_call("123-456-7890"))
    
    print()

    print(phone2)
    print(phone2.power_on())
    print(phone2.launch_game_mode())
    print(phone2.make_call("987-654-3210"))
#Activity 2
class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water.")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling along the road.")

my_car = Car()
my_plane = Plane()
my_boat = Boat()
my_bicycle = Bicycle()
vehicles = [my_car, my_plane, my_boat, my_bicycle]
print("--- Vehicles in Action ---")
for vehicle in vehicles:
    vehicle.move()
def travel(vehicle):
    print(vehicle.move())