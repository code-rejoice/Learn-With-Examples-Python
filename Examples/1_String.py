#tutorials 3: Execute the below instructions in the interpreter

#execute the below command
"Hello World!"

print("Hello World!")

#execute using single quote
'Hello World!'

print('Hello World!')

#use \' to escape single quote
'can\'t'

print('can\'t')

#or use double quotes
"can't"

print("can't")

#more examples 1- using print function
print(
	'" I won\'t," she said.'
	)

#more examples 2
a = 'First Line. \n Second Line'
print(a)

#String concatenation
print("\n-->string concatenation example without using +")
print('Py''thon')

#String concatenation using +
print("\n-->string concatenation: concatenating two literals using +")
print("Hi "+"there!")

#String and variable concatenation using +
print("\n-->string concatenation: concatenating two literals using +")
a="Hello"
print( a +" there!")

#concatenation of two variables
print("\n-->string concatenation: concatenating two String variables using +")
b= " World!"
print(a+b)

# String indexing
print("\n-->string Indexing: Declare a String variable and access the elements using index")
word = "Python"
print("word-->"+word)

print("\n--> word[0]")
print(word[0])
print("\n--> word[5]")
print(word[5])

print("\n--> word[-6]")
print(word[-6])
print("\n -->if you type word[7]], you would get an error as shown below, as it is out of range")
print("  File \"<stdin>\", line 1")
print("     word[7]]")
print("          ^")
print("SyntaxError: invalid syntax")
print("	  \")")

print("-->Notice the index for each of the letters in the word 'PYTHON' both forward and backward")
print("\n  -->  P  Y  T  H  O  N")
print("  -->  0  1  2  3  4  5")
print("  --> -6 -5 -4 -3 -2 -1")


print("--> word[0:4]")
print(word[0:4])

print("--> word[:2]")
print(word[:2])


print("--> word[4:]")
print(word[4:])

print("--> word[-4]")
print(word[-4])

print("--> word[2]='N' --> String is immutable and hence cannot be changed.\nif we try to, we would get the below error.But we can always create a new String")
print("\nTraceback (most recent call last):")
print("  File \"<stdin>\", line 1, in <module>")
print("TypeError: 'str' object does not support item assignment")

print("\ncreation of a new String")
print("\nrun the  command--> word[:2]+'new'")
print (word[:2]+'new')

print("\nprinting word")
print (word)

print("\nlength of word is")
print (len(word))
