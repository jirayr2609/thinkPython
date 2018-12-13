def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]


def is_palindrome(word):
	if len(word) <=1:
		return True
	if first(word) != last(word):
		return False
	return is_palindrome(middle(word))

def gcd(a,b):
	if a == b :
		return a
	if a > b:
		bigger = a
		smaller = b
	else:
		bigger = b
		smaller = a
	gcd = 0
	for i in range(1,smaller+1):
		if smaller%i==0 and bigger%i==0:
			gcd = i
	return gcd

print(gcd(12,32)) 

