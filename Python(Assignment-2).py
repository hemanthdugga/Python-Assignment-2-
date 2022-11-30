#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1)Write a program to accept two numbers from the user and calculate multiplication, division.
x=int(input("Type your first number :"))
y=int(input("Type your second number :"))
p=x*y
q=x/y
print(p)
print(q)


# In[8]:


#2)write a python program to print the characters from a string that are present at an even index.
word = input('Enter word: ')
size = len(word)
for i in range(0, size, 2):
    print("index[", i, "]", word[i])


# In[9]:


#3)write a python program to print the characters from a string that are present at an odd index
word = input('Enter word: ')
size = len(word)
for i in range(1, size, 2):
    print("index[", i, "]", word[i])


# In[22]:


#4)write a pyhton program which will print the sum of the two numbers if the two numbers are even or it will print the difference
# of two numbers
num1=int(input("Enter first number "))
num2=int(input("Enter second number "))
if num1%2==0 and num2%2==0:
    print("{} + {} = {}".format(num1,num2,num1+num2))
else:
    print("{} - {} = {}".format(num1,num2,num1-num2)) 


# In[24]:


#5)Write a python program to convert all even indexed alphabets to upper and odd indexed char.

test_str = "hemanthkumar"
print("The original string is : " + str(test_str))
res = ""
for x in range(len(test_str)):
    if not x % 2 :
        res = res + test_str[x].upper()
    else:
        res = res + test_str[x].lower()
print("The alternate case string is : " + str(res))


# In[28]:


#6)Write a python program which will print True if the input number is divisible by 5 or else False
list_1 = [13, 10, 87, 50, 71, 25]
result = list (map (lambda x: (x %5 == 0), list_1))
print ("Numbers that are divisible by 5 are:", result)


# In[29]:


#7)Given two integer numbers return their product only if the product is greater than 1000, else return their sum.
num1 = int(input("Type your first number: "))
num2 = int(input("Type your second number: "))
if num1*num2>=1000:
    print("{} * {} = {}".format(num1,num2,num1*num2))
else:
    print("{} + {} = {}".format(num1,num2,num1+num2))


# In[35]:


#8)Given two strings x, y writes a program to return a new string made of x and y’s first, middle, and last characters
#Example:
#Input
#X=” pytho”
#Y=” javas”
#Output
#” pjtvos”

x= input("enter any character ")
y= input("enter any character ")
z=a[0]+b[0]+a[len(a)//2]+b[(len(b)//2)]+a[-1]+b[-1]
print(z)


# In[4]:


#9)Write a python program to take three names as input from a user in the single input () function call
#Input: Enter three names: - “person1 person2 person3” Output: Name1: - “person1” Name2: - “person2” Name3: - “person3”
a=input("enter the names :")
b=a.split()
for i in b:
    print("name1 :",b[0])
    print("name2 :",b[1])
    print("name3 :",b[2])
    break;


# In[3]:


#10) Write a Python program to get a string from a given string where all occurrences of its first char have been 
# changed to '@', except the first char itself.
# Example:
# Input:
# 'malayalam’
# Output:
# 'malayala@'
# Input:
# ' abcabab'
# Output:
# ‘abc@b@b
s = input("Type string : ")
char = s[0]
for i in s:
    s = s.replace(s[0],'@')
    s = char + s[1:]
print(s)


# In[4]:


# 11)Write a Python program to add 'ing' at the end of a given string (string length should be equal to or more than 3). 
# If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3,
# leave it unchanged
# Example:
# Input:
# 'sing’
# Output:
#'singing'
# Input:
# ' playing'
# Output:
# ‘playly’
# Input:
# ' on'
# Output:
# ‘on’
var3= input("Enter any string ")
var4=[]
if len(var3)>=3 and var3.endswith("ing"):
    var4=var3.replace("ing","ly")
    print(var4)
elif len(var3)>=3:
    var3=var4.append(var3+"ing")
    print(var4)
elif len(var3)<3:
    var4.append(var3)
    print(var4)


# In[6]:


#12)Write a python program that accepts two inputs num1 and num2 print True if one of them is 10 or if their sum is 10 otherwise print False

a=int(input("enter the numbe1 :"))
b=int(input("eneter the number2 :"))
c=a+b
if a>=10 or b>=10 or c==10:
    print("True")
else:
    print("False")


# In[8]:


#13)Write a python program that accepts three inputs x, y and z print True if x*y>z otherwise False
p=int(input("enter the numbe1 :"))
q=int(input("eneter the number2 :"))
r=int(input("eneter the number3 :"))
d=p*q
if r>d:
    print("True")
else:
    print("False")


# In[10]:


#14)Write a python program that accepts two strings inputs return True depending on whether the total number of characters in the first string is equal to the total number of characters in the second string

m=tuple(input("enter the numbe1 :"))
n=tuple(input("eneter the number2 :"))
if len(m)==len(n):
    print("True")
else:
    print("NOT EQUAL")


# In[12]:


#15)Write a python program that takes a string input, we'll say that the front is the first three characters of the string. If the string length is less than three characters, the front is whatever is there. Return a new string, which is three copies of the front
x=input("Enter your  string :")
if len(x)<3:
    print(x)
elif len(x)>=3:
    print(x[0:4]*3)


# In[13]:


#16)Write a python program that takes in a word and determines whether or not it is plural. A plural word is one that ends in "s".
str2= input("Enter your string ")
if str2.endswith("s"):
    print("The word is Plural")
else:
    print("The word is Singular")


# In[16]:


#17)A bartender is writing a simple program to determine whether he should serve drinks to someone. He only serves drinks to people 18 and older and when he's not on break (True means break and False means not a break time). Given the person's age, and whether break time is in session, create a python program which prints whether he should serve drinks or not.
x=input("Is bartender on break(True/False): ")
if x=="True":
    print("Bartender should not serve drinks")
elif x=="False":
    y=int(input(" plese enter the Age of the customer: "))
    if y>=18:
        print("Bartender  serve drinks")
    else:
        print("Bartender  not serve drinks")
else:
    print("Input has to be True or False")


# In[17]:


#18)Manoj Kumar has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Manoj Kumar.
#Person Relation
#Shiva father
#Letha mother
#Tarun brother
name=input("enter the name :")
if name=="Shiva":
    print(name,"father")
elif name=="Letha":
    print(name,"mother")
elif name=="Tarun":
    print(name,"brother")
elif name=="Kavita":
    print(name,"sister")
elif name=="Stranger":
    print(name,"coder")


# In[18]:


#19)Write a python program that takes a string, breaks it up and returns it with vowels first, consonants second. For any character that's not a vowel (like special characters or spaces), treat them like consonants
x=input("Type the string: ")
x1=""
x2=""
for y in range(len(x)):
    if x[y]=="a" or x[y]=="e" or x[y]=="i" or x[y]=="o" or x[y]=="u":
        x1=x1+x[y]
    else:
        x2=x2+x[y]
print(x1+x2)  


# In[20]:


#20) Create a dynamic calculator which asks for numbers and operator and return the answers
#Example
#Input:
#Type first number: 10
#Type any of this (+, -, *, /, %, **): *
#Assignment-2
#Type second number: 19
#Output:
#Answer is 190
a=int(input("eneter first value :"))
b=int(input("enter second value :"))
c=input("type any of this [+, -, *, /, %, **] ")
if c=="+":
    print("The addition of two numbers is :",a+b)
elif c=="-":
    print("The substraction of two numbers is :",a-b)
elif c=="*":
    print("The product of two numbers is :",a*b)
elif c=="%":
    print("The  floor division of two numbers is",a%b)
elif c=="/":
    print("The floor division of twi numbers is ",a/b)
elif c=="**":
    print("The power of two numbers is",a**b)


# In[ ]:




