str_lst = input("Enter a list of string:-").split()
#t = len(str_lst)
if len(str_lst)>0:
    t=0
    for i in str_lst:
        if len(i)>t:
            t = len(i)
print("The length of the largest string is:-",t)
