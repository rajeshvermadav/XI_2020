#numbers1 = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple

count_odd = 0
count_even = 0
while True:
    numbers = int(input("Enter a sequence of odd or even number and [99 to Exit]:-"))
    if numbers == 99:
       break
    if numbers % 2 == 0:
        count_even+=1
    else:
        count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

