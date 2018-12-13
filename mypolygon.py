import math
from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01


def square(t, length):
	for i in range(4):
		fd(bob, length)
		lt(bob)
def polygon(t, length, n, angle):
	
	for i in range(int(angle/360*n)):
		fd(bob, length)
		lt(bob, 360/n)

def call(bob, length, n):
	polygon(bob,length, n)

def circle(t,r):
	polygon(t, 2*math.pi*r/20, 20) 

def arc(t, r, angle):
	polygon(t, 2*math.pi*r/20, 20, angle)

arc(bob,50,120)



wait_for_user()