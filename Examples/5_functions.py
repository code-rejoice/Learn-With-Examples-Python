#tutorials 5: functions

print(
	"-->examples to define functions\n"
	)
x = str(input("enter an alphabet: \n"))
print ("entered alphabet is ",x)


def vowelTest(alphabet):
	vow=['a','e','i','o','u']
	if any(alphabet in s for s in vow) :
		print("TEST PASS: the given alphabet is a vowel")
	else:
		print("TEST FAILED: the given alphabet is NOT a vowel")

print("calling function test(alphabet) \n")
vowelTest(x.lower())		