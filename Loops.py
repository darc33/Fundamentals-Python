#WHILE LOOP

count = 0
while count <= 9:
  print ("Hello, I am a while and count is", count)
  count += 1
  
#WHILE / ELSE LOOP

import random

print ("Lucky Numbers! 3 numbers will be generated.")
print ("If one of them is a '5', you lose!")

count = 0
while count < 3:
  num = random.randint(1, 6)
  print (num)
  if num == 5:
    print ("Sorry, you lose!")
    break
  count += 1
else:
  print ("You win!")

#ENUMERATE FOR   
choices = ['pizza', 'pasta', 'salad', 'nachos']

print ('Your choices are:')
for index, item in enumerate(choices):#it permits to know the index 
  print (index+1, item)
  
#ZIP FUNCTION (iterate over tow lists at once)

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):#zip stops at the end of the shorter list
  # Add your code here!
  if a > b:
    print (a)
  else:
    print (b)
    
#FOR / ELSE

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print ('You have...')
for f in fruits:
  if f == 'tomato':
    print ('A tomato is not a fruit!') # (It actually is.)
    
  print ('A', f)
else:#executes if for ends normally, not by a break
  print ('A fine selection of fruits!')
  

#IS EVEN
def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False
    
#IS INT
    
def is_int(x):
  if type(x) == int or round(x) == x:
    return True
  else:
    return False
    
#DIGIT_SUM
    
def digit_sum(n):
  sm=0
  ns = str(n)
  for s in ns:
    sm += int(s)
    
  return sm

#FACTORIAL
    
def factorial(x):
  fact = 1
  for n in range(1,x+1):
    fact *= n
    
  return fact

#IS PRIME
    
def is_prime(x):
  
  if x > 1:
      # check for factors
      for i in range(2,x):
          if (x % i) == 0:
              print(x,"is not a prime number")
              print(i,"times",x//i,"is",x)
              break
          else:
              print(x,"is a prime number")
       
  else:
      print(x,"is not a prime number")
      
#REVERSE
    
def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word
    
#ANTI VOWEL

def anti_vowel(text):
    a_text = ""
    l= len(text)
    for x in range(l):
        if text[x].lower() == "a" or text[x].lower() == "e" or text[x].lower() == "i" or text[x].lower() == "o" or text[x].lower() == "u":
            a_text = a_text
        else:
            a_text += text[x]
      
    return a_text
    
#SCRABBLE_SCORE
    
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  word = word.lower()
  total = 0
  for x in word:
    for key in score:
      if x == key:
        total += score[key]
  
  return total
  
#CENSOR (cambia un palabra por asteriscos en una oracion)
  
def censor(text, word):
  repl = ""
  text2= text.split()
  for x in word:
    repl += "*"
  for index, val in enumerate(text2):
    if word == val:
      text2[index] = repl
      
  text = ' '.join(text2)
  return text
  
#COUNT (cuenta cuantas veces esta item en la secuencia)
  
def count(sequence, item):
  times = 0
  
  for x in sequence:
    if x == item:
      times += 1
  
  return times
  
#PURIFY (removes odd numbers in the list)
def purify(numbers):
  pure= []
  
  for x in numbers:
    if x % 2 == 0:
      pure.append(x)
      
  return pure
  
#PRODUCT (return the product of the numbers of a list)
def product(numbers):
  prod = 1
  for x in numbers:
    prod *= x
    
  return prod
  
#REMOVE_DUPLICATES
def remove_duplicates(inputlist):
    if inputlist == []:
        return []
          
    inputlist = sorted(inputlist)
    outputlist = [inputlist[0]]

    for i in inputlist:
        print (outputlist[-1])
        if i > outputlist[-1]:
          outputlist.append(i)
        
    return outputlist 
    
#MEDIAN
def median(input_list):
  median=0.0;
  input_list=sorted(input_list)
  l=len(input_list)
  if l % 2 != 0:
    median = input_list[(l-1)/2]
  else:
    median=(input_list[(l/2)-1]+input_list[l/2])/2.0
    
  return median 
  

