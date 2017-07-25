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

