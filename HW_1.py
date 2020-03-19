#1
a = int (5)
b = int (3)
if b > a:
  print ( "b is greater than a")
else:
  print("b is not greater than a")

#2
c = int(7)
d = str ("We")
print (bool(c))
print (bool(d))

#3
f = bool (7)
g = bool("Hello")
h = bool(["I", "You" ,"We"])
print (f)
print (g)
print (h)
print (bool(()))
print (bool(""))
print (bool([]))


#4
j = int(5)
if j >3 and j<10:
  print ("True")
else:
  print ("False")


#5
k = int(5)
if k >3 or k<=4:
  print ("True")
else:
  print ("False")

#6
l = int(5)
if l > 3 and not l < 10:
  print ("True")
else:
  print ("False")

#7
mylist = ["run", "walk","stop"]
print (bool (mylist))
print (bool())

#8
mylist1 = ["run", "walk","stop"]
print (mylist1)
print (mylist1[1])
print (mylist1[2])

#9
mylist2 = ["run","walk","stop","sleep","want","dream","eat"]
print (mylist2[2:5])
print (mylist2[-4:-1])
mylist2 [1]= "jump"
print (mylist2)

#10
mylist3 = ["run","walk","stop","sleep","want"]
for x in mylist3:
  print (x)
  print (len(mylist3))
  mylist3.append("dream")
  print (mylist3)
  mylist3.insert(1,"eat")
  print(mylist3)
  mylist3.remove("eat")
  print(mylist3)
  mylist3.pop()
  print(mylist3)
  mylist3.pop(1)
  print(mylist3)
 # del mylist3[0]
 # print(mylist3)
 # mylist3.clear()
 # print(mylist3)
 # del mylist3
 # print(mylist3)

#11
mylist4 = ["run", "walk", "stop", "sleep", "want"]
youlist4 = mylist4.copy()
print(youlist4)
youlist = list(mylist4)
print(youlist)

# 12

mylist5 = ["run", "walk", "sleep"]
mylist6 = ["want", "dream", "eat"]
mylist7 = mylist5 + mylist6
print(mylist7)

# 13
mylist8 = ["run", "walk", "sleep"]
mylist9 = ["want", "dream", "eat"]
for x in mylist9:
  mylist8.append(x)
print(mylist8)

#14
mylist8 = ["run","walk","sleep"]
mylist9 = ["want","dream","eat"]
mylist8.extend(mylist9)
print(mylist8)

#15
mylist8 = list (("run","walk","sleep"))
print(mylist8)

#16

mylist = list(("want","dream","eat","jump","rain","rain","rain","rain"))
x = mylist.count("rain")
print (x)

#17

mylist = [1,2,3]
mylist.reverse()
print (mylist)

#18

a = ("run","walk","sleep")
print(a)
print (a[1])
print (a[2])
print (a[-2])

#19

b = (1,2,3,4,5,6,7)
c= b[2:5]
print(c)
c= b[-4:-1]
print (c)

#20

aa = (1,2,3)
bb = list(aa)
bb [2]= ("Go")
cc = tuple(bb)
print (cc)

#21

aaa = (1,2,3,4,5)
for x in (aaa):
  print (x)

#22

bbb = ("run","walk","stop","sleep", "gold")
if "gold" in bbb:
  print ("gold")


#23

ccc = (1,2,3,4,5)
print (len(ccc))


#25
gg = ("go")
print (type(gg))


#27

a_a = (1,2,3)
b_b = (4,5,6)
c_c = a_a + b_b
print (c_c)

#28

ad = (1,2,3,3,4)
print (ad)
x = ad.count(3)
print (x)

#29
z = (1,2,3,4,5)
x = z.index(3)
print (x)

#30

set1 = {1,3,6}
print (set1)
for x in set1:
  print (x)
print ("3" in set1)

#31

k = {"run", "walk","stop"}
l = {1,2,3}
newSet = k.union(l)
print (newSet)
m = {6,7,8}
newSet.update (m)
print (newSet)

#32

oo = {"run", "walk","stop"}
pp = oo.copy()
print (pp)

#33

kk = {"run", "walk","stop","dream", "dream"}
ll = {1,2,3,4,4}
mm = ll.difference(kk)
print (mm)
kk.difference_update(ll)
print (kk)

#34

a1 = {
"hair":"brown", "eyes": "blue","height": 170
}
x= a1["hair"]
print (x)
y = a1.get ("eyes")
print (y)
a1 ["hair"] = "blond"
print (a1)
for x in a1:
  print (x)
  print (a1[x])
for x in a1.values():
  print(x)
for x, y in a1.items():
  print(x, y)


 #36

  b1 = {
"hair":"brown", "eyes": "blue","height": 170, "head": 1 , "fingers": "ten"
}
print (b1)
if "hair" in b1:
  print ("Yes")
print (len(b1))
b1[ "leg"]= "two"
print (b1)
b1.pop("head")
print(b1)
b1.popitem ()
print(b1)
#del b1 ["hair"]
#print (b1)
#b1.clear()
#print (b1)
#del b1
#print (b1)



#37
c1 = {
"hair":"brown", "eyes": "blue","height": 170
}
d1 = c1.copy()
print (d1)
f1 = dict(c1)
print (f1)

#38

g1 = {
  "house1" : {
    "floor" : "one",
    "stair" : 2
  },
  "house2" : {
    "floor" : "two",
    "stair" : 3
  },
  "house3" : {
    "floor" : "three",
    "stair" : 3
  }
}
print (g1)

#39

house1 = {
    "floor" : "one",
    "stair" : 2
  },
house2 = {
    "floor" : "two",
    "stair" : 3
  },
house3 = {
    "floor" : "three",
    "stair" : 3
  }
myhouse = {
  "house1": house1,
  "house2": house2,
  "house3": house3
  }
print (myhouse)

#40

myhouse = dict (house="house1",floor= "one", stair=1)
print (myhouse)

#41

t = 3
r = 7
if r > t:
   print("r is greater than t")

 #42

tt = 3
rr = 7
if rr > tt:
  print("rr is greater than tt")
elif  rr==tt:
  print ("rr and tt are equal")
else:
  print ("rr is greater than tt")
if  rr > tt:
  print("rr is greater than tt")
else:
  print ("tt is not greater than rr")

  #43

r = 3
t = 4
if r < t: print("t is greater than r")


#44

a = 3
d = 4
print("Yes") if a < d else print ("No")

#45
a = 5
b = 10
c = 15
if b > a and c > b:
  print ("Both conditions are True")

  #46

a = 6
b = 11
c = 16
if b > a or c < b:
  print ("True")

  #47

a = 7
b = 9
c = 14
if b > a :
  print ("Yes")
  if c > a :
    print ("True")
  else:
    print ("No")










