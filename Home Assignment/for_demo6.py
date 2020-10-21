numbers1 = (1,2,3,4,5,6,7)
#numbers1 = 0
count_even = 0
count_odd = 0
#numbers1 = int(input("Enter final range"))
for x in numbers1:
    numbers1 = int(input("Enter final range"))
    #if numbers1==99:
        #break

    if x % 2 == 0:
        count_even+=1
    else:
        count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)