#to be updated

print("Dictionaries examples-->\n")
print("An unordered set of key: value pairs where keys are unique\n")

print("dict1={'one':1,'two':2,'three':3}  -->")
dict1={'one':1,'two':2,"three":3}
print("dict1 contents -->", dict1)
print("\ndict1['two']")
print(dict1['two'])

#deleting a key value pair
print("deleting a key value pair\n")
print("del dict1['three']-->")
del dict1['three']
print("\n",dict1)

#Listing keys only from a dictionary
print("\nListing keys only from a dictionary\n")
print("dict1.keys()-->\n",dict1.keys())

#sorting keys in dictionary
print("\nsorting keys in dictionary\n")
print("sorted(dict1.keys())-->\n",sorted(dict1.keys()))

#validate existence of the key
print("\nvalidate existence of the key\n")
print("'one' in dict1-->\n",'one' in dict1)
print("\n'nothing' in dict1-->\n",'nothing' in dict1)

#dict() constructor 
print("\ndict() constructor ")
print("builds a dictionary from sequences of key value pairs")
dict2 = dict([('one',1),('two',2),('three',3)])
print("\ndict2-->", dict2)

dict3=dict(nine=9, eight=8, seven=7)
print("\ndict3-->\n",dict3)

#using dict comprehensions
print("\ndict comprehensions-->\n"
"creating dictionaries from arbitrary key and value expressions:\n")
print("{x: x*2 for x in (2, 4, 6)}--> x is the key x*2 is the value\n")
print({x: x*2 for x in (2, 4, 6)})
print("\n{x: x**2 for x in (2, 4, 6)}--> x is the key x square is the value\n")
print("{x: x**2 for x in (2, 4, 6)}\n")
print({x: x**2 for x in (2, 4, 6)})