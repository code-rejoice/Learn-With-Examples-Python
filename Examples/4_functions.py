#tutorials 4: functions

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

# second method to call a function

print("\n--> second method to call a function-->")
y = str(input("\nenter second alphabet: \n"))
print ("entered alphabet is ",y)
vowelTestSecond=vowelTest(y.lower())
vowelTestSecond

#third method to cal a function
def vowelTestThird(alphabet,PASS="TEST PASS: the given alphabet is a vowel",
FAIL="TEST FAILED: the given alphabet is NOT a vowel"):
	vow=['a','e','i','o','u']
	if any(alphabet in s for s in vow) :
		print(PASS)
	else:
		print(FAIL)
		
print("\n--> third method to call a function-->")
z = str(input("\nenter third alphabet: \n"))
print ("entered alphabet is ",z)
vowelTestThird(z.lower())
vowelTestThird(z.lower(),"\nfunction with optional param called: " 
"RESULT PASS: try with 25 other alphabets!",
"\nfunction with optional param called: "
"FAIL: dont worry! you have 25 more alphabets to test!")

#TO BE CONTINUED
