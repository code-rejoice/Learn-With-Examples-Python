#tutorials 4: for, range, break, continue

print(
	"-->for, range, break, continue examples\n"
	)

#example 1
print("-->  example 1\n")
print("--> for loop can iterate through a list or String\n")
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
print("months List-->",months,"\n")

for a in months:
	print(a,",",a.upper())

#example 2
print("\n--> example 2\n")	
numbers = ["one","two","three","four","five"]
print("\nnumbers List-->",numbers,"\n")

for anything in numbers:
	print(anything,"\t",len(anything))
	
#RANGE
print("-->range example\n")
print("range is used to iterate over a sequence of numbers\n "
" -->for i in range(5):\n")
for i in range(5):
	print("the value of i is ",i)

#RANGE WITH INCREMENTS
print("\n specify the starting and end range along with a increment value\n"
	"in this case, the value increments 3 each time until it reaches 9\n")
for i in range(0, 10, 3):
	print("the value of i is ",i)	
	
print("\n"
	"each time -3 is added to the previous negative number which starts from -1\n")	
for i in range(-1, -20, -3):
	print("the value of i is ",i)	
	

#using break in a for loop
print("\n--> break example")
for i in range(-1, -20, -3):
	if i == -7:
		print("the value of i is ",i," loop ends\n")	
		break
	else: 
		print("the value of i is ",i)
	
#using continue in a for loop
print("\n--> continue example")
for i in range(-1, -20, -3):
	if i == -7:
		print("the value of i is ",i," loop continues with else as well\n")	
		continue
	else: 
		print("the value of i is ",i)	