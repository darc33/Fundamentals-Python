#LISTS
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"];


if len(zoo_animals) > 3:
  print ("The first animal at the zoo is the " + zoo_animals[0])
  print ("The second animal at the zoo is the " + zoo_animals[1])
  print ("The third animal at the zoo is the " + zoo_animals[2])
  print ("The fourth animal at the zoo is the " + zoo_animals[3])
  
zoo_animals.append("lion")
list_length = len(zoo_animals)
tiger_index = zoo_animals.index("tiger")
zoo_animals.insert(2,"duck")
zoo_animals.sort() #Organiza la lista
zoo_animals.remove('sloth') #Quita un elemento de la lista
print
my_list = [1,9,3,8,5,7]

for number in my_list:
  print (2 * number)

print
#DICTIONARY
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print (residents['Puffin'])
print (residents['Sloth'])
print (residents['Burmese Python'])
print

del residents['Sloth'] #Quita un valor del dictionary

residents['Next One'] = 110

inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

inventory['pocket']=['seashell', 'strange berry', 'lint']#adding a key
inventory['backpack'].sort() #Sorting the list under key 'backpack'
inventory['backpack'].remove('dagger') #removing a value of the key 'backpack'
inventory['gold'] += 50 #Adding to the value of the key 'gold'


#SUPERMARKET

prices = {
  "banana" : 4,
  "apple"  : 2,
  "orange" : 1.5,
  "pear"   : 3,
}
stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}

shopping_list = ["banana", "orange", "apple"]

for key in prices:
  print (key)
  print ("price: %s" % prices[key])
  print ("stock: %s" % stock[key])
  print
  
total_sell = 0
for key in prices:
  print ("The total price of %s is: %s" % (key, prices[key] * stock[key]))
  total_sell += (prices[key] * stock[key])
  print
  
print ("The total of sells of supermarket is: %s" % total_sell)
print  

def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
    
  return total

print ("The total of your bill is: %s" % compute_bill(shopping_list))