# Assuming this is the content of first_python.py
class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)

# Creating an instance of Vehicle
my_vehicle = Vehicle(max_speed=120, mileage=20000)

# Optionally, assign seating capacity if you want
my_vehicle.assign_seating_capacity(seating_capacity=5)

# Display the properties
my_vehicle.display_properties()
