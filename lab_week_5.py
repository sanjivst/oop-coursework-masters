
class Vehicle:
    def __init__(self, colour, weight, max_speed, max_range=None, seats=None):
        self.colour = colour
        self.weight = weight
        self.max_speed = max_speed
        self.max_range = max_range
        self.seats = seats

    def move(self, speed):
        """Moves the vehicle at a specified speed."""
        print(f"The vehicle is moving at {speed} km/h")

class Car(Vehicle):
    def __init__(self, colour, weight, max_speed, form_factor, **kwargs):
        super().__init__(colour, weight, max_speed, **kwargs)
        self.form_factor = form_factor

    def move(self, speed):
        """Overrides the move method to specify car speed."""
        print(f"The car is driving at {speed} km/h")        

class Electric(Car):
    def __init__(self, colour, weight, max_speed, form_factor, battery_capacity, **kwargs):
        super().__init__(colour, weight, max_speed, form_factor, **kwargs)
        self.battery_capacity = battery_capacity

    def move(self, speed):
        """Overrides the move method to specify electric car speed."""
        print(f"The electric car is driving silently at {speed} km/h with a battery capacity of {self.battery_capacity} kWh and a maximum range of {self.max_range} km")

class Petrol(Car):
    def __init__(self, colour, weight, max_speed, form_factor, fuel_capacity, **kwargs):
        super().__init__(colour, weight, max_speed, form_factor, **kwargs)
        self.fuel_capacity = fuel_capacity

    def move(self, speed):
        """Overrides the move method to specify petrol car speed."""
        print(f"The petrol car is roaring at {speed} km/h with a fuel capacity of {self.fuel_capacity} liters and a maximum range of {self.max_range} km")

class Plane(Vehicle):
    def __init__(self, colour, weight, max_speed, wingspan, **kwargs):
        super().__init__(colour, weight, max_speed, **kwargs)
        self.wingspan = wingspan

    def move(self, speed):
        """Overrides the move method to specify plane speed."""
        print(f"The plane is flying at {speed} km/h with a wingspan of {self.wingspan} meters")

class Propeller(Plane):
    def __init__(self, colour, weight, max_speed, wingspan, propeller_diameter, **kwargs):
        super().__init__(colour, weight, max_speed, wingspan, **kwargs)
        self.propeller_diameter = propeller_diameter

    def move(self, speed):
        """Overrides the move method to specify propeller plane speed."""
        print(f"The propeller plane is flying at {speed} km/h with a propeller diameter of {self.propeller_diameter} inches")

class Jet(Plane):
    def __init__(self, colour, weight, max_speed, wingspan, engine_thrust, **kwargs):
        super().__init__(colour, weight, max_speed, wingspan, **kwargs)
        self.engine_thrust = engine_thrust

    def move(self, speed):
        """Overrides the move method to specify jet speed."""
        print(f"The jet is soaring at {speed} km/h with a {self.engine_thrust} engine")

class FlyingCar(Car, Plane):
    def __init__(self, colour, weight, max_speed, form_factor, wingspan, **kwargs):
        super().__init__(colour, weight, max_speed, form_factor=form_factor, wingspan=wingspan, **kwargs)

    def move(self, speed):
        """Overrides the move method to specify flying car speed."""
        print(f"The flying car is flying or moving at {speed} km/h")


generic_vehicle = Vehicle("red", 1000, 200)
generic_vehicle.move(100)

electric_car = Electric("green", 1200, 200, "Hatchback", 100, max_range=500, seats=5)
electric_car.move(100)
print(electric_car.seats)
petrol_car = Petrol("red", 1500, 250, "SUV", 50)
petrol_car.move(150)

generic_flying_car = FlyingCar("red", 1000, 200, "SUV", 30, seats=5)
generic_flying_car.move(100)
print(generic_flying_car.seats, generic_flying_car.wingspan,
generic_flying_car.form_factor)

generic_flying_car_2 = FlyingCar(colour="red", weight=1000, max_speed=200, form_factor="SUV", wingspan=30, seats=5)
generic_flying_car_2.move(100)

# car = Car("blue", 1500, 250, "SUV")
# car.move(150)