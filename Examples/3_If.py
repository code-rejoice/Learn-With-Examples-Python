#tutorials 3: if, if else, if elif else

print(
	"-->if, if else, if else elif examples"
	)
	
#if conditon
print("--> if example"
	"\nAssign x=10 and check using if condition\n"
	"x = 10\n"
	"if x == 10:\n"
	)
x = 10
if x == 10:
		print("result: x is equal to 10\n")
		
#if else condition
print(
	"-->If else example"
	)
print(
	"\nAssign x=10 and check using if condition\n"
	"x = 9\n"
	"if x == 10:\n"
	)
x = 9
if x == 10:
		print("result: x is equal to 10\n")
else:
		print("result: x is NOT EQUAL to 10\n")
		
		
#if elif else condition		
print(
	"-->If elif else example\n"
	"\nTake input from user\n"
	)
x = int(input("enter an integer: \n"))

print(
	"The value of entered number 'x' is",x
	)

if x > 0:
		print("\nresult: x =", x,", is greater than zero \n")
elif x < 0:
		print("\nresult: x =", x,", is less than zero\n")
else: 
	print("\nEntered digit is 0\n")
	
