# 1
def aaa(func):
    def out():
        print("Code before function")
        func()
        print("Code after function")

    return (out)


def enter():
    print("X")


enter = aaa(enter)
enter()


# 2
def aaa(func):
    def out():
        print("Code before function")
        func()
        print("Code after function")

    return (out)


def bbb(func2):
    def out1():
        print("This is one more line")
        func2()
        print("This is one more line")

    return (out1)


@aaa
@bbb
def enter():
    print("X")


enter()

# 3
a = int(input("Enter number N: "));
print(a + a * a)

# 4
a = 46
c_int = int("4")
print(a, (c_int * 5))

# 5
c = ','.join(str(1234))
print(c)

# 6
a = str(input("Enter First name: "))
b = str(input("Enter Last name: "))
c = int(input("Enter your age: "))
print(a, b, c)

# 7
a = (input("Enter number: "))
b = len([i for i in a if i == '7'])
print(b)

# 8
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
print(a + b + c)
print(a - b - c)
print(a / b / c)
print(a * b * c)
print(a % b, b % c)

# 9
a = int(input("Enter integer: "))
b = float(input("Enter float: "))
c = str(input("Enter number as string: "))
d = int(c)
print(a * b * d)

# 10
a = float(input("Enter float number: "))
if a > 0:
    print("positive")
elif a < 0:
    print("negative")
else:
    print("zero")

    # 11


def a():
    while True:
        try:
            b = int(input("Enter any sign: "))
        except ValueError:
            print("Not an integer")
            continue
        else:
            return b
            break


a()

# 12
a = int(input("Enter your age: "))
if a > 18:
    print("Вам уже все можно")
elif a == 18:
    print("Ура, Вам 18 лет!")
else:
    print("Вы еще слишком молоды")

    # 13
print("I would like to say: Thanks Google !!!!")
print("_______________________________________")


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")

# 14
exp = int(input("Enter export: "))
imp = int(input("Enter import: "))
if exp > imp:
    print("Positive")
else:
    print("Negative")

    # 15
num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))

    # 16
a = 14
if a > 10 & a != 12 & a <= 15 or a == 18:
    print("True")
else:
    print("False")
