
#1
i = 34
while i < 67:
  print(i)
  i += 2

#2
i = 0
while i < 100:
  i +=1
  if i ==50:
    continue
  if i ==99:
    continue
  print (i)

#3

a = str (input ())
b = int (input ())
for x in a:
  x *= b
  print (x)


#6

 lis = ["Андрей", "Иван", "Василий", "Петро", "Максим", "Дима"]
a = lis [0]
print (a)
for x in a:
  print (x)
b = lis [1]
print (b)
for x in b:
  print (x)
c = lis [2]
print (c)
for x in c:
  print (x)
d = lis [3]
print (d)
for x in d:
  print (x)
f = lis [4]
print (f)
for x in f:
  print (x)
h = lis [5]
print (h)
for x in h:
  print (x)

  #7

  lis = [1, 34, 8, 0, -5, 7, 32, 74, 59, 92, 41, 10, -2]
x = min(lis)
print (x)
if x < 0:
  lis.remove(x)
  lis.insert(13,x)
  print (lis)
if x >= 0:
  lis.remove(x)
  lis.insert(0,x)
  print (lis)
  
   #9

  def myfunc(a,b):
  print (a)
  print (b)
myfunc(4,2)

#10
def dev (x,y,z =2):
  return ( x / y /z)
print (dev (24,2,3))
print (dev (24,2))

#11
def myfuncSum(*args):
  a = 0
  for x in args:
    a += x
  return a
print (myfuncSum (1,5,5,4,5))
print (myfuncSum (3,4,5))

#12
import datetime
a = datetime.datetime.now()
print(a)


#13

import random
a = random.randint(0, 20)
print (a)

#14
def myfunc(color = "Red"):
  print("Rainbow has  " + color)
myfunc()
myfunc("Orange")
myfunc("Yellow")
myfunc("Green")
myfunc("Light blue")
myfunc("Blue")
myfunc("Purple")


#15
def myfunc(colors):
  for x in colors:
    print(x)
colors = ["red", "orange", "yellow", "green", "blue"]
myfunc(colors)

#16
def myfunc(a):
  return 3 * a
print(myfunc(1))
print(myfunc(2))
print(myfunc(3))
print(myfunc(55))
print(myfunc(333))

#17
def myfunc(**args):
  return args
print (myfunc(x = 3,y = -6))
print (myfunc (x = "Colors"))

#18
def myfunc(*colors):
  print("The rainbow has " + colors[3])
myfunc("red", "yellow", "blue", "green")

#19

def myfunc(**colors):
  print("The rainbow has " + colors ["c"])
myfunc (a = "red", b = "yellow", c = "blue")

#20
x = lambda c: c + 20
print (x(30))

#21

x = lambda c, b: c * b
print (x(3,5))

#22

x = lambda a,b,c: a + b + c
print (x(3,5,7))

#23

def myfunc(x):
  return lambda a : a * x
mynewfunc = myfunc(2)  
print(mynewfunc(32))

#24
try:
  num1 = 4
  num2 = 0
  print (num1/num2)
  print ("we")
except ZeroDivisionError: 
  print ("colors")

#25

#try:
  num1 = 4
  num2 = 2
  print (num1/num2)
  print ("Happy")
except ZeroDivisionError: 
  print ("division by zero")
except TypeError: 
  print ("unsupported operand type(s) for /: 'int' and 'str'")
else:
  print ("We are fine")
finally:

