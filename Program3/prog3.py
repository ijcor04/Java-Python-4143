# Isaiah Corrales
# Program 3 CMPS-4143-102
# This program will ask the user to enter decimal numbers they would like converted to binary,
# the solutuion is found reucrsively, it will continue to loop until the sentinel value (-1) is entered.

# defining the function "binary" which is a recursive function
def binary(decimal):
   if decimal == 0:
      return 0
   else:
      # arithmetic to find out the binary makeup of a decimal number
      return (decimal % 2 + 10 * binary(int(decimal // 2)))

# while loop that only breaks when -1 is entered
decimal = int(input("Please enter an integer (enter -1 to exit) "))

while (decimal != -1):
    print(binary(decimal))
    decimal = int(input("Please enter an integer (enter -1 to exit) "))
    
