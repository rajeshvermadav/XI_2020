# To take input from the user
num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        #print(num)
        print(i)
        if (num % i) == 0:
            print(num, "is not a prime number")
            #print(i, "times", num // i, "is", num)
            break
        else:
            print(num, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")

a = int(input("Input an integer : "))
n1 = int(a)
n2 = int(a+a)
n3 = int(a+a+a)
print(n1 + n2 + n3)