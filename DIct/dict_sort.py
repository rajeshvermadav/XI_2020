#Sort (ascending and descending) a dictionary by value
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items())  # In Ascending order
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict(sorted(d.items(), reverse = True))   # In Descending order
print('Dictionary in descending order by value : ',sorted_d)

