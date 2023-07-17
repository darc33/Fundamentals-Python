n = [1, 3, 5]
n.pop(1) #Quita el elemento en el indice dado y lo devuelve
print (n)
n.remove(1) #Quita el elemento dado
print (n)
del(n[0]) #lo mismo que pop pero sin devolver el elemento
# Doesn't return anything
print (n)

#LIST OF LISTS
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
  results=[]
  for numbers in lists:
    for number in numbers:
      results.append(number)
  return results


print (flatten(n))
print

#BATTLESHIP(one-player, single ship, 5x5 grid, 10 guesses)

from random import randint #imports random module

board = []
for x in range(5):
  board.append(["O"] * 5)

def print_board(board_in):
  for row in board_in:
    print (" ".join(row))# Uses the string to combine the prints
 
print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print ship_row
#print ship_col

for turn in range(10):
    print ("\nTurn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("Oops, that's not even in the ocean.\n")
        elif(board[guess_row][guess_col] == "X"):
            print ("You guessed that one already.\n")
        else:
            print ("You missed my battleship!\n")
            board[guess_row][guess_col] = "X"
      
        print_board(board)
        
    if turn == 9:
        print ("Game Over")
   
  