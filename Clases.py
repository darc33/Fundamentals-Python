#CREATE A CLASS
class Fruit(object): #Hereda de la clase object
  """A class that makes various tasty fruits."""
  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

  def description(self):
    print ("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))

  def is_edible(self):
    if not self.poisonous:
      print ("Yep! I'm edible.")
    else:
      print ("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()

#MEMEBER AND INSTANCE VARIABLES
class Animal(object):
  """Makes cute animals."""
  is_alive = True #member variable (para todos los objetos de la clase)
  health ="good"
  def __init__(self, name, age):
    self.name = name #instance variable (particular de cada objeto)
    self.age = age #instance variable
  
  def description(self):
    print (self.name)
    print (self.age)

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

hippo = Animal("zehn", "10")
hippo.description()

sloth = Animal("drei", "3")
ocelot = Animal("vier", "4")

print (hippo.health)
print (sloth.health)
print (ocelot.health)

#OVERRIDE AND SUPER
class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00


class PartTimeEmployee(Employee):
  def calculate_wage(self, hours): #Override the method of the superclass
    self.hours = hours
    return hours * 12.00
  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours) #Access the tributes or method of superclass

milton = PartTimeEmployee("milton")
print (milton.full_time_wage(10))
print

#DRIVE A CAR

class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
   
  def display_car(self):
    print ("This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg)))
    
  def drive_car(self):
    self.condition = "used"
    
class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg   = mpg
    self.battery_type = battery_type
    
  def drive_car(self):
    self.condition = "like new"

my_car = Car("DeLorean", "silver", 88)
my_car2 = ElectricCar("Acura", "red", 100, "molten salt")

print (my_car.condition)
my_car.drive_car()
print (my_car.condition)

print (my_car2.condition)
my_car2.drive_car()
print (my_car2.condition)

#3D REPRESENTATION

class Point3D(object):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    
  def __repr__(self): #How to represent an object of the class
    return "(%d, %d, %d)" % (self.x, self.y, self.z)
  
my_point = Point3D(1,2,3)

print (my_point)

