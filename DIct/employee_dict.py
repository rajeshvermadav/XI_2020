num = int(input("Enter the number of employees whose data to be stored: "))
count = 1
emp = dict()                               #create an empty dictionary
while count <= num:
    name = input("Enter the name of the Employee: ")
    salary = int(input("Enter the salary: "))
    emp[name] = salary
    count += 1
print("\n\nEMPLOYEE_NAME\tSALARY")
for k in emp:
    print(k,'\t\t',emp[k])
print(emp)