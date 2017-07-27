#tutorials 5: functions

print(
	"\n-->examples to define datastructures using Lists\n"
	)
#List methods
print("--> usage for list.append(x)\n")
numbers=["one","two","three","four","one","two"]
print("\nthe contents of numbers list is -->",numbers)
print("\nadd \"five\" to the list")
print("numbers.append(\"five\")\n")
numbers.append("five")
print("--> usage for list.extend(iterable)\n")
print("\nthe contents of numbers list after appending, is -->",numbers)
print("numbers.extend(\"six\")\n")
numbers.extend("six")
print("\nthe contents of numbers list after extending, is -->",numbers,
"String is iterable\n")
print("numbers.extend([\"seven\",\"eight\"])")
numbers.extend(["seven","eight"])
print("\nthe contents of numbers list after extending, is -->",numbers)
print("--> usage for list.insert(i, x)\n")
numbers.insert(0,"zero")
print("numbers.insert(0,\"zero\")")
print("\nthe contents of numbers list after inserting, is -->\n",numbers)
numbers.remove('s')
numbers.remove('i')
numbers.remove('x')
print("\nnumbers.remove('s')\n"
"numbers.remove('i')\n"
"numbers.remove('x')\n")
print("\nthe contents of numbers list after removing, is -->",numbers)

#usage of list.pop()

print("\nnumbers.pop()\n")
numbers.pop()
print("\nthe contents of numbers list after popping the last item is -->",numbers)
print("notice that 'eight' is removed ")

print("\nnumbers.pop(0)\n")
numbers.pop(0)
print("\nthe contents of numbers list after popping the last item is -->",numbers)
print("notice that 'zero' is removed")

#usage of list.index(x,start_index, end_index)
print("\nnumbers.index('one',0)\n")
print(numbers.index('one',0))
print("\nwe searched for the index of 'one' from the zeroth index and "
"we see the response as 0")

print("\nnumbers.index('one',2,7)\n")
print(numbers.index('one',2,7))
print("\nwe searched for the index of 'one' between index 2 and 7 "
"we see the response as 4")

#usage of list.count(x)
print("numbers.count('one')\n")
print(numbers.count('one'))
print("we see the ocurrence of 'one' twice\n")

#usage of list.count(x)
print("numbers.sort()\n")
numbers.sort()
print(numbers)


#usage of list.reverse()
print("numbers.reverse()\n")
numbers.reverse()
print(numbers)

#usage of list.copy()
numCopy=numbers.copy()
print("\nnumCopy contents =",numCopy)