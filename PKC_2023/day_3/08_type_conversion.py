
x=100                   # integer
y=100.29                 # float
z="Hello"              # string
print(type(x))
print(type(y))
print(type(z))

# implicit type of conversion
x=x*y                  # float
print(x,"type of x is:", type(x))

# explicit type of conversion
age=input("What is your age? ")
age=int(age)
print(age, type(int(age)))          # int
age=input("What is your age? ")
print(age, type(float(age)))        # float

# name
name=input("what is your name? ")
print(name, type(str(name)))        # str



