# Python intro
## Why Python
### Python use cases
#### Python set up with Pycharm
##### Python variables

- Env Testing `print("hello world")`

```python
# print("Good Morning, Please Enter your Name")
# name = input()# took user input & stored in the var called name
# print("Hello dear")
```
```python
# testing the env with print statement

# Python Variables?
# To store any data -
# To store user data - hard code the data - any other type
# first_name = "Angel" - String
# name = "Ayoub"

# UK_resident = yes or no - Boolean

# DOB = 99 - Integer
# travel = 15.4 Float
# salary = 40000 Integer
# gross_salary = "salary + travel"

first_name = "Ayoub"
last_name = "Igozouln"
Salary = 50
Travel = 3.5 # float

#print("Ayoub")
#print("first_name")
# Display the value of variable first_name
print(last_name)

#print(Salary)
print(Travel)

# How to find out the type of data stored in the var
# type(
print(type(last_name))

# # interact with users by taking user data in - input()
# print("Good Morning, Please Enter your Name")
# name = input()# took user input & stored in the var called name
# print("Hello dear")

# Get user first_name and last_name
# Display the names in the line
# User DOB
# course name
# UK_resident

print("What is your first name?")
first_name = input()
print("What is your last name?")
last_name = input()
print("What is your DOB?")
DOB = input()
print("What is your course name?")
course_name = input()
print("Are you a UK_resident?")
UK_resident = input()
```

#Week 2


# Why Python?

- In comparison to other languages it is easy learn 
- Versatility, Efficiency, Reliability, and Speed
- Efficient and reliable
- Hundreds of Python Libraries and Frameworks

![image](https://user-images.githubusercontent.com/115165899/194916313-8c549e97-bcb4-4306-9178-6e7a735152e7.png)

# What are Python use cases?

- Web development
- DevOps
- Data Analysis

# Output Console:

![image](https://user-images.githubusercontent.com/115165899/194915988-04d5c30d-3517-43c2-8771-35ae99defb93.png)


# Python variables


# Data types

- Integer - A whole number
- String - A sequence of characters
- Character - Single
- Booeleon - Value of either true or false
- Float Number - A number with a decimal point


## Git & Github
- Add changes to our git-hub reo - the changes that we made on local host

-`git add filename` or `git add .` means push everything from current location
- `git commit -m "new markdown guide added"`
- now let's send this new data to github
- `git push -u origin main`
- `git status` Will tell us what's changed






### Intro to Data types & Operators
-`+ - * / `

###### Comparison Operators
- `>` Greater than
- `<` Less than
- `==`True or False
- `>=` Greater than or equal
- `<=` Less than or equal
- 

```python
a = 24
b = 16
user_ages = 18
print(a + b) # outcome added value of a & b
print(a - b) #outcome - a from b
# comparison
print(a > b) # True
print(a < b) # False
print(a == b)
```
### Boolean Methods:
```python
# Boolean Builtin methods in Python - Boolean Methods
# - DRY do not repeat yourself print("")

greeting = "Hello World!"
print(greeting)
print(greeting.isalpha())
print(greeting.islower())
print(greeting.startswith("H"))
print(greeting.endswith("!"))_# check if it wnds with specific letter
print(greeting.isdigit())
```
### Pyhton slicing/Indexing:
```python
# String Slicing
# string indexing - starts from 0
# H e l l o     W o r l d !
# 0 1 2 3 4 5 6 7 8 9 10 11
#                  -3 -2 -1

#greeting = "Hello World!"
#print(greeting)
# we have builtin method that checks the length of string
print(len(greeting))
print(greeting[0])

greeting = "Hello"
print(greeting)
print(len(greeting))
print(greeting[4])
```

### Python String methods:
```python
# String methods are available

# # use var =  string "aslkddjalkfjalkdfj                     "
# white_space = "lot's of spaces at the end                        "
# print(len(white_space))
# # strip() removes the white spaces
# print(len(white_space.strip()))
# print(print(len(white_space)))

Example_text = "ayoub here's some text with lots of text"
print(Example_text.count("text"))
print(Example_text)
print(Example_text.lower())
print(Example_text.upper())
print(Example_text.capitalize())
print(Example_text.replace("with", ","))
```

#### Tuples and Data Collections
```python
# Data Collections
# Lists
# Tuples
# Dict
# lists
 syntax list_name = ["sfksdf", "dkfsdf"]
# apply DRY
# shopping_list = ["ketchup", "fanta", "eggs", "bread"]
# #     # indexing      0          1        2        3
 print(shopping_list)
 print(type(shopping_list))
# # shopping_list.append("chicken")
# # print(shopping_list)_# add an item to the list
 print(shopping_list[2])
 shopping_list[2] = "icecream"
 print(shopping_list)
# # find out how to remove an item from the list
# # find out how to remove fanta from list
 shopping_list[0] = "fanta"
 shopping_list.remove("fanta")
 print(shopping_list)
# Can list have multiple data types
# multiple_type = [1, 2, 3, "one", "five", "ten"]
 print(multiple_type)
 print(multiple_type[2])

# Tuples
# Immutable - cant be changed - edited - added
# User_details = DOB - country name - city name -
# Syntax ("")
essentials = ("milk", "paracetamol","drinks")
 print(essentials)
 print(type(essentials))
# what is the diff between Lists and Tuples
 essentials[0] = "coffee"
 print(essentials)
```
```python
# What is a Dictionary - Data collection type
# How to manage Dictionaries - How to manage the data using Dict
# It works as Key value pair key = value
# Syntax { "name": "Sparta"         }
#           # 0       1
# store student's data - name, course_name, progress, completed_lessons_names
student_1 = {
    "name": "Ayoub",
    "Stream": "DevOps",
    "completed_lessons": 4,
    "completed_lessons_names": ["lists", "tuples", "strings"]
}                            #     0        1           2
# print(type(student_1))
# print(student_1)
# print(student_1["stream"]) # This will display the value saved inside stream
# # print/display completed_lesson_names
# # print/display completed_lesson_names index 0 means lists

print(student_1)
print(type(student_1))
print(student_1["name"])
print(student_1["completed_lessons_names"])
print(student_1["completed_lessons_names"][0])

```
