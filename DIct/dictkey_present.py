d1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dict = int(input("Enter a key in number"))
for x in d1:
    if x in dict:
      print('Key is present in the dictionary')
    else:
      print('Key is not present in the dictionary')
