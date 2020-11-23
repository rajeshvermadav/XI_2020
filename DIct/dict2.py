
ODD = {1:'One',3:'Three',5:'Five',7:'Seven',9:'Nine'}
print("Display the keys:", ODD.keys())
print("Display the Values", ODD.values())
print("Display the items:", ODD.items())
print("length of the dictionary:", len(ODD))
if 7 in ODD:
    print("Seven in dict")
if 2 in ODD:
    print("2 is present")
else:
    print("2 is not present")
print("Retrieve the value corresponding to the key 9:", ODD.get(9))
