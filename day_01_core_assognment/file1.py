# - variable declaration
# Data-Types
#primitives
# int
num1 = 42
#float
num2 = 2.3
#  - Booléen 
boolean = True
#string
string = 'Hello World'
#- Composite
#- List
#- initialize 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#- Tuples
#- initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')
#- access value
print(type(fruit))
print(pizza_toppings[1])
#- add value
pizza_toppings.append('Mushrooms')
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])
#- conditional
#  - if
if num1 > 45:
    print("It's greater")
#  - else
else:
    print("It's lower")
#  - if
if len(string) < 5:
    print("It's a short word!")
#  - else if
elif len(string) > 15:
    print("It's a long word!")
#  - else
else:
    print("Just right!")
#- for loop
for x in range(5):
    print(x)

#-         start stop  increment
#              v v 
for x in range(2,5):
    print(x)
#-         start stop increment
#              v  v  v
for x in range(2,10,3):
    print(x)
x = 0
#  -End- for loop
#- while loop
while(x < 5):
    print(x)
    x += 1
#- delete value
pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
#- delete value)
person.pop('eye_color')
print(person)
#  -End- while loop
#- for loop
for topping in pizza_toppings:
#-Conditional
    #-if 
    if topping == 'Pepperoni':
        #-continue
        continue
    print('After 1st if statement')
    #if
    if topping == 'Olives':
        #-Break
        break
#-Function1
# - parameter
def print_hello_ten_times():
    #-For-Loop
    # - parameters
    for num in range(10):
        print('Hello')
        #-End-For-Loop
print_hello_ten_times()
#Function2
#-parameters x
def print_hello_x_times(x):
    #-for-loop throughing 
    for num in range(x):
        print('Hello')
print_hello_x_times(4)
#-End-for-loop
#-Function3
#-Parameters taking x type-var int 10
def print_hello_x_or_ten_times(x = 10):
#-------Start-For-Loop------
#------parameters-taking x-----
    for num in range(x):
        print('Hello')
print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)
#-return 4

"""
Bonus section
"""

print(num3)
#-----Declacaration-of-variables------
#-----Initialize-------------
num3 = 72
#-------List-----------
fruit[0] = 'cranberry'
#--------Acces-Values-------
print(person['favorite_team'])
print(pizza_toppings[7])
print(boolean)
#--------Add-Values-in-List
fruit.append('raspberry')
#--------Delete-Values-in-List
fruit.pop(1)