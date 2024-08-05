import math
def add(x,y):
  return x+y
def sub(x,y):
  return x-y
def mul(x,y):
  return x*y
def div(x,y):
  if y==0:
    return "error:cannot divide by zero"
  else:
    return x/y
def square_root(x):
  return math.sqrt(x)
def power(x,y):
  return x**y
x=int(input('enter a number:'))
y=int(input('enter a number:'))
print(f"the addition of{x}and{y}is:{add(x,y)}")
print(f"the subtraction of{x}and{y}is:{sub(x,y)}")
print(f"the multiplication of{x}and{y}is:{mul(x,y)}")
print(f"the division of{x}and{y}is:{div(x,y)}")
print(f"the square root of{x}is:{square_root(x)}")
print(f"the power of{x}and{y}is:{power(x,y)}")

  
