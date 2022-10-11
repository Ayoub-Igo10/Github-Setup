# Let's see the operators in action
### Intro to Data types & Operators
# -`+ - * / `
#
###### Comparison Operators
# - `>` Greater than
# - `<` Less than
# - `==`True or False
# - `>=` Greater than or equal
# - `<=` Less than or equal

# a = 24
# b = 16
# user_ages = 18
# print(a + b) # outcome added value of a & b
# print(a - b) #outcome - a from b
# # comparison
# print(a > b) # True
# print(a < b) # False
# print(a == b)

# % operator - find out what it is and how it's used in python
# create a print statement to show the use case of it

# != operator
# The not-equal-to operator (!=) returns true if the operands don't have the same value; otherwise, it returns false.

# # Boolean Builtin methods in Python - Boolean Methods
# # - DRY do not repeat yourself print("")
#
# greeting = "Hello World!"
# print(greeting)
# print(greeting.isalpha())
# print(greeting.islower())
# print(greeting.startswith("H"))
# print(greeting.endswith("!"))_# check if it wnds with specific letter
# print(greeting.isdigit())

# # String Slicing
# # string indexing - starts from 0
# # H e l l o     W o r l d !
# # 0 1 2 3 4 5 6 7 8 9 10 11
# #                  -3 -2 -1
#
# #greeting = "Hello World!"
# #print(greeting)
# # we have builtin method that checks the length of string
# print(len(greeting))
# print(greeting[0])
#
# greeting = "Hello"
# print(greeting)
# print(len(greeting))
# print(greeting[4])

# # String methods are available
#
# # # use var =  string "aslkddjalkfjalkdfj                     "
# # white_space = "lot's of spaces at the end                        "
# # print(len(white_space))
# # # strip() removes the white spaces
# # print(len(white_space.strip()))
# # print(print(len(white_space)))
#
# Example_text = "ayoub here's some text with lots of text"
# print(Example_text.count("text"))
# print(Example_text)
# print(Example_text.lower())
# print(Example_text.upper())
# print(Example_text.capitalize())
# print(Example_text.replace("with", ","))

# user data input
# first_name = "ayoub"
# last_name = "igozouln"
# salary = 40
# # print(first_name)
# # print(last_name)
# # print(first_name + last_name)
# # print(first_name + " " + last_name , salary)_# cast int to string using coma instead of +
# # F - string
# print(f"Hello {first_name} {last_name} ")_# Python 3.5/6 or above

#
# print("Good Morning, Please enter your First Name")
# first_name = input()
# #
# print ("Enter Last Name")
# last_name = input()
# #
# print("Enter DOB")
# DOB = input()
#
# print("Are you a Uk resident? Answer Yes or No")
# uk_resident = input()
#
# print("Do you enjoy football Answer Yes or No")
# Hobbies = input()

# Hobbies=input("Can you please enter your Hobbies")
#
#
# print(f'Hello   {first_name}  {last_name} {DOB} {uk_resident} {Hobbies}')