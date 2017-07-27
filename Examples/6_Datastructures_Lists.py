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

#TO BE CONTINUED
