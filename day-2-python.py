class Guest:
    def __init__(self, first, last, interest, phone):
        self.first = first
        self.last = last
        self.interest = interest
        self.phone = phone


g_1 = Guest("Eve", 'Dela Cruz', "Anime", 12345)
g_2 = Guest("Adam", 'Perez', "Russian Literature", 59821)
g_3 = Guest("Mike", 'Lim', "Movies", 59821)
g_4 = Guest("Katie", 'Lopez', "Sports", 81901)
g_5 = Guest("Bert", 'Smith', "Cooking", 19027)

print(g_1.last, g_2.phone, g_3.interest)


class Customers:
    greeting = "Welcome to Coffee Palace!"

    def __init__(self, name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total


c_1 = Customers("Nate", 'Espresso', "Pastrami on rye", 220)
c_2 = Customers("Elaine", 'Strawberry frappuccino', "Tuna wrap", 270)
c_3 = Customers("Samirah", 'Iced caffe latte', "Cinamon roll", 225)
c_4 = Customers("Jerry", 'Caramel macchiato', "Glazed doughnut", 238)
c_5 = Customers("Paz", 'Iced tea', "Blueberry pancakes", 315)

print(Customers.greeting)
print(c_2.name)
print(c_2.beverage)
print(c_2.food)
print(c_2.total)
print(c_4.name)
print(c_4.beverage)
print(c_4.food)
print(c_4.total)


# Inheritance
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display1(self):
        print("(parent class/User) Username:", self.username, "password:", self.password)


# Method overriding
class Admin(User):
    def __init__(self, username, password, code):
        self.code = code
        User.__init__(self, username, password)

    def display2(self):
        print("(subclass/Admin) Username:", self.username, "password:", self.password, "code:", self.code)


# super method same as above
class Admin2(User):
    def __init__(self, username, password, code):
        self.code = code
        super().__init__(username, password)

    def display3(self):
        super().display1()
        print("(subclass/Admin) Username:", self.username, "password:", self.password, "code:", self.code)


u_45 = User("pretty_jun25", "otherpaassword287")
a_1 = Admin("leslie2001", "password1234", "CODE")
a_2 = Admin2("leslie2001", "password1234", 23)

u_45.display1()
a_1.display2()
a_2.display3()


class ClubMembers:
    def __init__(self, name, birthday, age, favorite_food, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal

    def display(self):
        print("Name:", self.name)
        print("Birthday: ", self.birthday)
        print("Age: ", self.age)
        print("Favorite food:", self.favorite_food)
        print("Goal:", self.goal)


class Clubofficers(ClubMembers):
    def __init__(self, name, birthday, age, favorite_food, goal, position):
        self.position = position
        ClubMembers.__init__(self, name, birthday, age, favorite_food, goal)

    def display2(self):
        print("Name:", self.name)
        print("Birthday: ", self.birthday)
        print("Age: ", self.age)
        print("Favorite food:", self.favorite_food)
        print("Goal:", self.goal)
        print("Position:", self.position)


m_1 = ClubMembers("Ton", "January 16", 14, "Ice cream", "To be Happy")
o_4 = Clubofficers("Vera", "June 22", 16, "Beef stroganoff", "To be the world's greatest chef", "Treasurer")

m_1.display()
o_4.display2()

# DICTIONARIES
# Dictionary printing
basketball_teams = {"tigers": ['data1', 'data2', 'data3', 'data4', 'data5'],
                    "Kalaban": ['data1', 'data2', 'data3', 'data4', 'data5']}
print(basketball_teams)
# dictionary adding
shopping_list = {"weird hat": 25, "purple ring": 450}

shopping_list["tsinelas"] = 35
print(shopping_list)
shopping_list.update({"weird hat": 25, "purple ring": 450, "tsinelas": 30, "baguio": 30})
print(shopping_list)

relative = ["Tita malou", "Jeff", "Tito Roger", "Veronica"]
age = [54, 14, 55, 19]

print(relative, age)
combined_list = zip(relative, age)

# dictionaries
relative_age = dict(zip(relative, age))

print(list(combined_list))
print(relative_age)

flavors = ["boots", "chocolate", "strawberry", "cookies n' cream", "bubblegum"]
toppings = ["almonds", "banana slices", "chocolate syrup", "caramel syrup", "white chocolate chips"]
ice_cream = dict(zip(flavors, toppings))
print(ice_cream)
ice_cream["chocolate"] = "blueberries"
ice_cream.update({"matcha": "pistachios", "ube": "mango slices"})
print(ice_cream)

exam_scores = {"Jonathan": 85, "Erica": 99, "Rose": 83, "Henry": 92, "Missy": 77, "Ashleigh": 88, "Paul": 68,
               "Gordon": 86, "Lisa": 90, "Kelly": 77, "Joe": 65, "Tiffany": 67, "Wesley": 97, "Gail": 71}

print(exam_scores["Paul"])
check_key = "Andrew"

if check_key in exam_scores:
    print(check_key, "took the test")
else:
    print(check_key, "didnt take the test!")

print(exam_scores.get("Lisa"))
print(exam_scores.get("Wesley"))
print(exam_scores.get("Sam"))

neighbors = {"Ms. Santos": "fruitcake", "Mr. Reyes": "cookies", "Mrs. Dela Cruz": "cupcakes",
             "Mr. Tiu": "gingerbread man"}

# remove the key in the dictionary
done = neighbors.pop("Mr. Reyes")
w = neighbors.values()
y = neighbors.items()
print(neighbors)
print(w)
print(y)

groceries = {"chicken": 8, "apples": 6, "cucumbers": 3, "milk": 2, "oranges": 4}
remove = groceries.pop("oranges")
print(groceries)
speakers = {"Sir Rafael": 54, "Ms. Joan": 33, "Ms. Dana": 67}
name = speakers.keys()
print(name)

tryout_result = {"Carl": "passed", "Quentin": "failed", "John Y.":
    "passed", "Peter": "failed", "Max T.": "passed", "Joseph":
                     "passed", "Jone": "failed", "Jorge": "failed", "George": "passed",
                 "Ben": "passed", "Jerome": "passed", "Rick": "failed", "Max G.":
                     "failed", "John P.": "failed", "Vince": "passed"}
print(tryout_result.get("Jorge"))

employee_1 = {"Name": "Frank", "Position": "Sales Representative", "Email Address": "frank@company.com"}
for key, value in employee_1.items():
    print(key)
    print(value)

characters_weapons = {"Harry Potter": "wand", "Percy Jackson": "Riptide",
                      "Katniss Everdeen": "bow and arrow", "Bilbo Baggins": "Ring"}
for name in characters_weapons.keys():
    print(name)

for name in characters_weapons.keys():
    if name == "Percy Jackson":
        continue
        print(name)
for val in characters_weapons.values():
    print(val)

cat = {1: {"name": "Sweetie", "age": "12", "color": "white"},
       2: {"name": "Ethel", "age": "3", "color": "orange"}}
print(cat(2)["age"])
print(cat[1]["name"])

cat = {1: {"name": "Sweetie", "age": "12", "color": "white"},
       2: {"name": "Ethel", "age": "3", "color": "orange"}}
cat[3] = {}
cat[3]["name"] = "Tuna"
cat[3]["age"] = "5"
cat[3]["color"] = "black"
cat(3)["personality"]: "friendly"
cat[4] = {'name': 'Bubbles', 'age': '7', 'color': 'gray', 'personality': 'grumpy'}
print(cat[1])
print(cat[2])
print(cat[3])
print(cat[4])

# R read
# A append
# W write
# X create
f = open("newfile.txt", "x")
f = open("newfile.txt", "w")
f.write("Python is easy!")
f = open("newfile.txt", "a")
f.write("\nPython Intermediate!")
f = open("newfile.txt", "r")
print(f.read())
f.close()

f = open("pythonessay.txt", "w")
f.write("I like Python because it's very interesting.")
f = open("pythonessay.txt", "a")
f.write(")nI plan to learn data visualization.")
f.write(")nI want to work in the field of data science.")
f.write(")nI plan to make a better world for the future generation.")
f = open("pythonessay.txt", "r")
print(f.read(12))
print(f.readline())
for x in f:
    print(x)

with open("filename.txt", "r") as file:
    for line in file:
        print(line)

f.close

import os

if os.path.exists("newfile. txt"):
    os.remove("newfile.txt")
else:
    print("The file does not exist")

# Exceptions
n = -5
if n < 0:
    raise Exception("No negative numbers allowed!")

employee_of_the_year = "Roger"

assert employee_of_the_year == "Roger"

assert employee_of_the_year == "Suzanne"

try:
    print(x + "macarons")
except NameError:
    print("Please define your variable.")
except IndentationError:
    print("Please be careful when indenting your code.")
except:
    print("Something else went wrong. We need to figure it out.")
else:
    print("No issues here!")
finally:
    print("Let's run the code anyway")

X = 500
 if X > 100:
     raise Exception ("This code will result in an error if X is bigger than 100.")
 
try:
     print (variable_1)
except:
     print("variable_1 is not yet defined")
