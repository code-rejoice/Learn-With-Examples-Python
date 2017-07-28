#tuples examples
print("\ntuples examples")

a= 12,13, 'numbers'
print(a)
print("a[0] -->",a[0])

print("nexted tuple\n")
print("b = a, (54,88,'numbers2')\n")
b = a, (54,88,'numbers2')
print("b-->",b)


print("a-->",a)

print("Let's try to change the first value\n")
print("we should see the below error\n"
"TypeError: 'tuple' object does not support item assignment\n"
"tuples are immutable\n")

print("a[0]=6\n")
a[0]=6

