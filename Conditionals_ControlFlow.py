#COMPARATORS

"""
== igual a 
!= no igual a
< menor que
<= menor o igual que
> mayor que
>= mayor o igual que 
"""

bool_one = 3 < 5 
bool_two =  3 == 5
bool_three = 5 != 3
bool_four = 3 > 5
bool_five = 3 <= 3

#BOOLEAN OPERATORS (and(second), or(last), not(first) )

bool_one = False and False
bool_two = True or False
bool_three = not True

#IF/ELSIF/ELSE STATEMENT

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print (greater_less_equal_5(4))
print (greater_less_equal_5(5))
print (greater_less_equal_5(6))

#CLINIC
def clinic():
    print ("You've just entered the clinic!")
    print ("Do you take the door on the left or the right?")
    answer = input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print ("This is the Verbal Abuse Room, you heap of parrot droppings!")
    elif answer == "right" or answer == "r":
        print ("Of course this is the Argument Room, I've told you that already!")
    else:
        print ("You didn't pick left or right! Try again.")
        clinic()

clinic()

#PYGLATIN TRANSLATOR

pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():#.isalpha() verifies if it's only characters
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print (new_word)
else:
  print ('empty')


