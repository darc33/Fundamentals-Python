#FUNCTIONS
def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print ("With tax: %f" % bill)
  return bill

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print ("With tip: %f" % bill)
  return bill
  
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

#IMPORT

from math import * #Import everything from module math
print (sqrt(25))

import math # Imports the math module
everything = dir(math) # Muestra todas las funciones de un modulo
print (everything) # Prints 'em all!

#PLAN YOUR TRIP

def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
  
def rental_car_cost(days):
  rent = 40 * days
  if days >= 7:
    rent -= 50
  elif days >= 3:
    rent -= 20
  return rent

def trip_cost(city, days, spending_money):
	return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print (trip_cost("Los Angeles", 5, 600))