# #add item in set
# set1={1,2,45}
# set1.add(5)
# print(set1)

# #add the set in set
# set1={1,2,34,0}
# set2={1,2,45}
# set1.update(set2)
# print(set1)

x = ("apple", "banana", "cherry")
y = list(x)
y[3] = "kiwi"
x = tuple(y)

print(x)
