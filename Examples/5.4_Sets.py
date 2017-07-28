#5.4 sets examples
print("sets example--> use set() function or {} to create sets \n")
numbers={"one","two","three","four","one","two"}
print("numbers set -->" , numbers,"\n")
print(numbers,"\n")

print("notice that duplicates are removed\n"
"Also notice that everytime we execute, \n"
"the order of the items in the result set change\n")

print("test existence of an item in the set\n")
print("'one' in numbers")
print('one' in numbers,"\n")

print("'nothing' in numbers")
print('nothing' in numbers)

print("find unique letters\n")
a= set('anaesthesia')
b= set('pharmaceutical')

print("print a --> removes duplicates from the set\n")
print(a)

print("print b --> removes duplicates from the set\n")
print(b)

print("\na-b, letters present in a but not in b\n")
print (a-b)

print("\n a | b, letters present in a or b or both\n")
print (a | b)

print("\n a & b, letters present in a and b\n")
print (a & b)

print("\n a ^ b, letters present in a or b, but not both\n")
print (a ^ b)