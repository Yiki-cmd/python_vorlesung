"""
A function is 
 a piece of code that carry out a repearable specified 
 or set of repeatable specified code instruction 
   1. returnable 
   2. none returnable

   --> single arrow - python
   ==> fat arrow - javascript
   or = logical operator
   | = delarative or (name type    )
"""
# 
def add(a:int | float, b: int | float) -> int|float:
    return a + b

c= add(a=1,b=2)
print(c)

num_1=4
num_2=6

num_3= add(num_1,num_2)
print(num_3)


def sayHi(name:str):
    print(f"Hi {name}")

sayHi("Awet")
sayHi("Dani")
sayHi("Malie")

"""
 arguments are divided in to two
  1. named references
  2. unnamed references


  1.supplied value
  2.defaulted value

defaulted value must be after supplied
"""

print("------111111-------")
def greet(name: str, greeting: str ="alles gut",):
  print(f"{name} {greeting}")

greet("Awet") 

greet(name="Awet" "Hallo")

greet("Awate")


"""
what is a factorial

5!
n*n-1*n-2* until n*n-1
or 

"""

def factorial(n: int) -> int:
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
five_factorial=factorial(5) # or print(factiorial(5))
print(five_factorial)
#first expand it all of it then muliply it at last
"""
lambda: a syntactic sugar of single line function

parametes: operation
lambda parameters: operation
python --> recursion 
"""
print("-----------2222222--------")
add_numbers = lambda x, y:x+y 
print(add_numbers(3,5)) 

sqr = lambda x: x**2 # x*x

print(sqr(9))

numbers = [2,8,3,4]

sqr_numbers = map(lambda x:x**2, numbers)

print(list(sqr_numbers))

print("-----3333333333-----")

def sqr_func(x:int)-> int:
    return x **2    
x=[2,8,3,4]

print(list(x))
 
"""
map take two parametrs
   1.reduce/operator [function,lambda]
   2. collection[list, dict,tuple,set]


"""

""""
1. it constructs an empty list
2. it converts the set to a list
number_{} = [] and loops over it
3. in each loop square the element and append it
to the list sqr_numbers
4. convert sqr_numbers to set and return it

"""
print("-----------44444444---------")
numbers=[2,3,8,4]
def map_x(numbers_: set) -> set[int]:
    #construct empty list
    sqr_numbers = []  #[4,]

    for number in list(numbers_):
         sqr_number = number**2
         sqr_numbers.append(sqr_number)
    # {2,3,8,4} = [2,3,8,4] 
    return set(sqr_numbers)

sqr_numbers = map_x(set(numbers))
#sqr_numbers = map(lambda x: x**2, numbers)

print(list(sqr_numbers))
sqr_numbers = map(lambda x: x**2, numbers)

print(sqr_numbers)
 
print("-----------55555555---------")


 def map_x(zahlen_:list[int])->list[int]:
    #construct empty list
    sqr_zahlen=[] 
    #{5,7,3,1} =
    for zahlen in zahlen_:
        sqr_zahlen=zahlen**2
        sqr_zahlens.append(sqr_zahlen)

        return sqr_zahlens

        sqr_zahlens=map_x(zahlen)
        print(sqr_zahlens)
         


