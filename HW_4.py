# task1
a = int(input())  # integer 5
b = int(input())  # integer 10
c = int(input()) # integer 15
print(a + b + c)
#
#  task 2
h = int (input()) # integer 4
b = int(input())  # integer 5
d = (b*h)*(1/2)
print (d)
#
# task 3
n = int (input()) # students 42
k = int (input()) # apples 5
print (n//k)
print (n % k)
#
#task 4
print ("Hello!")    #Hello!
#
#task 5
st1 = int (input())  #studentsRoom1 = 30
st2 = int (input())  #studentsRoom2 = 23
st3 = int (input())  #studentsRoom3 = 28
print(int((st1+st2+st3)/2))
#
#task 6
z = int (input())  # integer 10
y = int (input())  # integer 15
if z < y:
  print (z)
#
#task 7
x = int(input())
if x > 0:
  x = 1
elif  x < 0:
  x = -1
else:
  x = 0
print(x)
#
#task 8
year = int(input())
if (year%4==0) or (year%400==0) and (not year%100==1):
  print("YES")
else:
  print("NO")
#
#task 9
p = int (input())  #integer2
o = int (input())  #integer3
u = int (input())  #integer4
if p<o and p<u:
    print(p)
elif o<c and o<p:
  print(o)
else:
  print(u)
  #
  #task 10
aa = int (input())  #integer2
bb= int (input())  #integer3
cc = int (input())  #integer4
if aa == bb == cc:
    print(3)
elif aa == bb or aa == cc or bb ==cc:
  print(2)
else:
  print(0)
  #
  #task 11
num = int(input())
if num >= 0:
  print ("положительное")
if num >= 0 and num <= 9:
    print ("однозначное число")
elif num >=10 and num <=99:
    print ("двуxзначное число")
elif num >=100:
  print ("трехзначное или более число")
if  num <= 0:
      print ("отрицательное")
if num <= -1 and num >=-9:
    print ("однозначное число ")
elif num <=-10 and num >=-99:
    print ("двуxзначное число")
elif num <=-100:
  print ("трехзначное или более число")


