def check_fermet(a, b , c, n):
	if n>2 and (pow(a,n) + pow(b,n) == pow(c,n)):
		print("Holy smokes, Fermant was wrong!")
	else:
		print("NO, that doesn't work.")




def is_triangle(a , b ,c):
	if (c > a+b) or (a > b+c) or (b > a +c):
		print("No")
	else:
		print("Yes")
"""a = int(input("Enter 3 integers as sides of triangle to check if a triangle can be made from them\n"))
b = int(input())
c = int(input())

is_triangle(a,b,c)
"""

def ack(m,n):
	if m ==0:
		return n+1
	elif m>0 and n==0:
		return ack(m-1,1)
	elif m>0 and n>0:
		return ack(m-1, ack(m,n-1))
def first(word):
return word[0]
def last(word):
return word[-1]
def middle(word):
return word[1:-1]

