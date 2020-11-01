l = ['R','A','S','H','I', 'Raman','Pranav','bhavika','Rijul',1,3,4]
l2 = ['Moonal', 'Pranjal']
l1 = len(l)
for c in range(l1):
    print("At index", c, "and", (c-l1), "element :-", l[c])
print(l[6][2])

s = l[0:10:3]
print(s)

l.append('Abhay')
l.extend(l2)
l.insert(6,'Devansh')
print(l)
r = []
r.append('rajesh')
r.insert(1,'Ansh')
r.extend(l)
print(r)



l = [5, 15, 35, 8, 98,5]
print("Index", "    ", "Elements")
for x in l:
    #print("Index", "Elements")
    print(l.index(x),"         ", x)
print(l.count(5))





























