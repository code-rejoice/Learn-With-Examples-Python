#tutorials 3: Lists

#more examples 1- using print function
print(
	"Start of Lists example"
	)

Lists=[1,2,3,4]
print("Lists -->")
print(Lists)

#using indexes in List
print("\nif we want to get a character in a particular\n index we can use the below code ")
print("\nLists[2] --> ")
print(Lists[2])

print("\nif we want to get a character in a reverse range use -ve numbers\n in index, here 4 has an index -1")
print("\nLists[-1] --> ")
print(Lists[-1])

print("if we want to get characters in a range use : , in this case we are\n trying to get characters from -2 position until end, \n hence we dont specify any number after :")
print("\nLists[-2:] --> ")
print(Lists[-2:])

print("if we dont specify starting range and end range\n, entire list will be printed")
print("\nLists[:] --> ")
print(Lists[:])

print("\nif we have to add few more sets of numbers to\n the existing List, it can be done as follows ")
print("\nLists+[5,6,7,8] --> ")
print(Lists+[5,6,7,8])

print("\n assigning the result to a new list")
print("\nLists2=Lists+[5,6,7,8] --> ")
Lists2=Lists+[5,6,7,8]
print(Lists2)

print("\n assign a new value in nth index Lists2[n]= x Lists2[4]=5.5 -> ")
Lists2[4]=5.5


print("\n Lists2, notice the changed value 5.5 --> ")
print(Lists2)

print("\n length of lists--> len(List name) ")
print(Lists)
print (len(Lists))

print("\n clearing a List --> ListName[:]=[] ")
Lists[:]=[]
print(Lists)

print("\n Nested Lists ")
ListA=[1,2,3]
print("\nListA--> ")
print(ListA)

ListB=[4,5,6]
print("\nListB--> ")
print(ListB)

ListAB=[ListA,ListB]
print("\nListAB = ListA, ListB --> ")
print(ListAB)
