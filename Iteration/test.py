import math
def test_square_root():
	for i in range(1,10,1):
		print(i,newt_square_root(i),math.sqrt(i), abs(newt_square_root(i) - math.sqrt(i)))






def newt_square_root(a):
	x = 4
	iter = 5
	while(iter !=0):
		y = (x + a/x)/2
		x = y
		iter -=1
	return y


"""
def eval_loop():
	myString=input("Enter expression to evaluate the result\n")
	while(myString!="done"):
		print(eval(myString))
		myString=input("Enter expression to evaluate the result\n")
eval_loop()
"""
def fact(a):
	pr = 1
	for i in range(1,a+1,1):
		pr = pr*i
	return pr 

def estimate_pi():
	sumOfterm = 0
	factor = 2*math.sqrt(2)/9801
	k = 0
	while True:
		num = fact(4*k)*(1103 + 26390*k)
		dum = fact(k)**4 * 396**(4*k)
		term = factor*num/dum
		sumOfterm +=term
		if abs(term)<1e-15:
			break
		k+=1
	return 1/sumOfterm

print(estimate_pi())





