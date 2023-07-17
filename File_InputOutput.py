#MODES 
"""
write-only mode ("w")
read-only mode ("r")
read and write mode ("r+")
append mode ("a"), which adds any new data you write to the file 
                    to the end of the file.
"""
my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

#Write
write_file = open("output.txt", "w")

for item in my_list:
  write_file.write(str(item) + "\n")#Escribe en el documento

write_file.close()

#Read
read_file = open("output.txt","r")

print ("Todo:")
print (read_file.read())#Lee todo el documento
read_file.close()

read_file = open("output.txt", "r")

print ("Linea:")
print (read_file.readline())#Lee solo una linea
read_file.close()

#Automatic close:

with open("output.txt", "a") as textfile:#using with...as....
  textfile.write("Success!")

if textfile.closed == False:
  textfile.close()
  
print (textfile.closed)