
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
