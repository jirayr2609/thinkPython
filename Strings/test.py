def backword(s):
	i = len(s)-1
	while(i>0 or i==0):
		print(s[i])
		i-=1
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
	if letter == "O" or letter == "Q":
		print(letter + "u" + suffix)
	else:
		print(letter + suffix)
def count(st, letter):
	count = 0
	for i in st:
		if i==letter:
			count = count + 1
	print(count)
"""
s = "baab"
print(s[:len(s)//2:1])
print(s[(len(s)-1):(len(s)//2):-1])
"""

def is_palindrome(s):

	if s == s[::-1]:
		print("is palindrome")
is_palindrome("baab")