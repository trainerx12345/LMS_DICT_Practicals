favorite_food = 'Pizza'
friend_name = 'tina'
favorite_drink = 'soda'

print('I like' + favorite_food + '.')
print('I like eating' + favorite_drink + ' with my friend, ' + friend_name + '.')
print('We like to drink' + favorite_drink + ',too.')

print('Roses are red, violets are blue')
if 10 > 7:
    print('Ten is greater than seven!')
if 16 < 42:
    print('Sixteen is less than forty-two')
print('A long time ago in a galaxy far, far away ...')


def hello_function(name):
    print('Hello ' + name + '.')


hello_function('Rose')


def hello_function2(firstname, lastname):
    print('Hello ' + firstname + ' ' + lastname + '.')


hello_function2('Rose', 'Bluews')


def nice_day(name):
    print('Have a nice day, ' + name + '!')


nice_day("Marissa")

input_name = input('Enter your name: ')
print('Your name is ' + input_name + '! Have a nice day!')

input_int = int(input('Enter your age: '))
print('Your age is ' + str(input_int) + ' years old')


def add_number(num1, num2):
    total = num1 + num2
    return total


number1 = float(input('Enter a decimal number:'))
number2 = float(input('Enter a decimal number:'))

print('The total of the number is ' + str(add_number(number1, number2)))

# Input: true
input_bool = input('Enter True or False: ').lower() == 'true'
print('Boolean value:', input_bool)
# Boolean value: True


# # Input: 1 2 3 4 5
input_list = [int(x) for x in input('Enter a list of integers separated by space: ').split()]
print('List of integers:', input_list)
# List of integers: [1, 2, 3, 4, 5]

# Input: 5 * 3 + 2
input_expr = eval(input('Enter any Python expression: '))
print('Result of expression:', input_expr)
# Result of expression: 17


input_your_name = input('Enter your name: ')
input_your_age = int(input('Enter your age: '))
input_your_favorite_color = input('Enter your favorite color: ')
input_your_favorite_movie = input('Enter your favorite movie: ')
input_your_mobile_number = input('Enter your mobile number: ')
input_your_motto = input('Enter your motto in life: ')


def print_information(name, age, fav_color, fav_movie, contact_number, motto):
    print('Name:', name)
    print('Age:', age)
    print('Favorite Color:', fav_color)
    print('Favorite Movie:', fav_movie)
    print('Mobile Number:', contact_number)
    print('Motto in Life:', motto)


# Call the function with the provided inputs
print_information(input_your_name, input_your_age, input_your_favorite_color, input_your_favorite_movie,
                  input_your_mobile_number, input_your_motto)

float_number = 30.5
print(int(float_number))

int_number = 20
print(float(int_number))

string_to_convert = 'dog'
print(tuple(string_to_convert))
# ('d','o','g')
print(list(string_to_convert))
# ['d','o','g']

print((10 > 7))
print(str(73911))
print(tuple("Thank God it's Friday!"))
print(float(4302))
print(int(3299.35640))

print(22 > 21)
print(345 == 11)
print(1 < 5)


class NewClass:
    pass


class Pets:
    looks = 'Adorable!'  # class Variable

    # Methods are a function that's within a class
    def __init__ (self,name):
        self.name = name


d1 = Pets('Hamster')

# instances
hamster = Pets()

# attribute = hamster.looks
print(hamster.looks)


class Guest:
    # pass is a placeholder so that the program doesn't break
    pass


g_1 = Guest()

# instance variables = g_1.first
# 'Eve' attribute
g_1.first = 'Eve'
g_1.last = 'Dela Cruz'
g_1.interest = 'Anime'
g_1.phone = 12345

# attributes and methods
print(g_1.interest)

g_2 = Guest()
g_2.first = "Adam"
g_2.last = "Perez"
g_2.interest = "Russian Literature"
g_2.phone = 87654

print(g_2.phone)


class Customer:
    greeting = "Welcome to Coffee Palace!"


c_1 = Customer();
c_1.name = "Samirah"
c_1.beverage = "Iced Caffe latte"
c_1.food = "Cinnamon roll"
c_1.total = 225

c_2 = Customer()
c_2.name = "Jerry"
c_2.beverage = "Caramel macchiato"
c_2.food = "Glazed doughnut"
c_2.total = 230

print(Customer.greeting)
print(c_1.beverage)
print(c_2.food)


print(25 + 40)
x = 32
y = 76
print(x + y)
va = 1230
vb = 952
print(va - vb)
print(50 * 10)
print(1000 / 12)
print(1000 % 6)
print(3 ** 2)
print(36 // 8) #4.5 = 4

colors = ["blue","red","green"]
things = ["car","pen","ball"]
for x in colors:
    print(x)
for x in "orange":
    print(x)
for x in colors:
    if x == "red":
        continue
    else:
        break

dataset = range(8)
for x in dataset:
    print(x)
for x in colors:
    for y in things:
        print(x,y)

count =1
while count <=10:
    print(str(count))
    count+=1

count_two =0
while count_two <=10:
    count_two += 1
    if count_two == 4:
        continue
    print(str(count_two))

count_three = 0
while count_three <= 10:
    print(str(count_three))
    count_three += 1
else:
    print("count three is no longer less than ")

