# Python Program to Print Natural Numbers from 1 to N, sum of naturaal number and average of natural number

number = int(input("Please Enter any Number: "))
s=0
av=0
print("The List of Natural Numbers from 1 to {0} are".format(number))

for i in range(1, number + 1):

    print(i, end='  ')
    s = s + i
    av = s/number
print("\nThe Sum of Natural Numbers from 1 to {0} are:-".format(number),s)
print("\nThe Average of Natural Numbers from 1 to {0} are:-".format(number),av)

