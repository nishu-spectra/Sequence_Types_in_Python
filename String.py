""" Strings are the collection of characters surrounded by single quotes, double quotes or triple quotes """

# creation of string in python
str1 = 'Hello' #single quote
print(str1)
str2 = "World" #double quote
print(str2)
str3 = '''Multiline string or docstring''' #triple quote
print (str3)

#indexing in Python String
string = "Hi"
print(string[0])
print(string[1])

#splitting/slicing in Python String
string = "Hello"
print(string[0:5])
print(string[:4])
print(string[1:])
print(string[2:4])

#Reassigning in String
string = "Nidhi"
print(string)
string= 'Nishu'
print(string)

#Deletion of String
string = "Nidhi"
print(string)
del string
# print(string)- since the string is now deleted so it will show 'string' is not defined



""" String Formatting Methods"""

# Old style formatting = similar to 'printf' function in C programming. It uses '%' operator for formatting
string = "Nishu"
age = 21
formatted_string = ("My name is %s and i am %d" %(string , age))
print(formatted_string)


# .format() method = it uses {} as placeholder for formatting 
string = "Nishu"
age = 21
formatted_string = ("My name is {} and i am {}" .format(string , age))
print(formatted_string)

# f-string formatting = it uses 'f' prefix before the string and expression is directly embedded using curly braces '{}' 
string = "Nishu"
age = 21
print(f"My name is {string} and i am {age}")

# template string = Template strings, provided by the string module, offer a way to substitute values into strings with placeholders indicated by a dollar sign ($). Used for user generated content
from string import Template
string = "Nishu"
age = 21
template = Template("My name is $string and i am $age" )
formatted_string = template.substitute(string= string , age = age)
print(formatted_string)


""" Escape Sequences"""
# escape characters are used when any character in the string is illegal

print ("We are \"Hikers\" ")  # double quote
print ('We are \'Hikers\' ')  # single quote
print ("Hello \nWorld")    # new line
print ("Hello \bWorld")    # backspace
print ("Hello \tWorld")    # tab
print ("Hello\rNishu")     # carriage return


# Python Booleans = it represents one of two values i.e true or false . WE can use bool() function to evaluate if any value is true or false

print(bool("Hello"))   # true
print(bool(10>9))      # true
print(7>10)            # false