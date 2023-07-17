my_dict = {
  "key1": 1,
  "key2": 2,
  "key3": 3
}

print (my_dict.items())#Extrae los pares de llaves y valores
print (my_dict.keys())#Extrae las llaves
print (my_dict.values())#Extrae los valores

#LIST COMPREHENSION (creates a list according to some logic)
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

even_squares =[x ** 2 for x in range(1, 11) if x % 2 == 0]

print (even_squares)


my_list = range(1, 11) # List of numbers 1 - 10
print (my_list[::2])#Omite el inicio y final de la particion y va de por medio

#ANONYMOUS FUNCTIONS (lambdas)

languages = ["HTML", "JavaScript", "Python", "Ruby"]


print( filter(lambda x: x == "Python", languages))#filter permit to pass only when the condition is true

squares = [x **2 for x in range(1,11)]
print (filter(lambda x: x >=30 and x <= 70, squares))

#BITWISE OPERATIONS (& verifica bits, | enciende bits, ^ invierte bits)
print
print (5 >> 4)  # Right Shift (0b101 >> 4 == 0b00000)
print (5 << 1)  # Left Shift (0b101 << 1 == 0b1010(10) )
print (8 & 5)   # Bitwise AND (0b1000 & 0b0101 == 0b0000)
print (9 | 4)   # Bitwise OR (0b10001 | 0b100 == 0b1101(13) )
print (12 ^ 42) # Bitwise XOR (0b1100 ^ 0b101010 == 0b100110(38) )
print (~88)     # Bitwise NOT (add 1 and make it negative)

print
print (0b1),    #BINARY
print (bin(1))  #Conversion a binario
print (int("11001001",2)) #Conversion a entero