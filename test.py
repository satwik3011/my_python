'''
#Removing spaces from string

getString = input('Enter string for action: ')

#Removing spaces from left
print(getString.lstrip(), 'has length: ', len(getString.lstrip()))

#Removing spaces from right
print(getString.rstrip(), 'has length: ', len(getString.rstrip()))

#Removing all spaces
print(getString.strip(), 'has length: ', len(getString.strip()))




#Program for checking Even/Odd
var = int(input("Enter Number: "))
if (var % 2 == 0):
     print(var,"is Even")
else :
    print(var,"is Odd")



#For loops

name = input("Your Name: ")
for element in range(0, len(name)):
    if name[element] == 'i':
        break
    else:
        print(name[element])


name = input("Your Name: ")
for element in range(0, len(name)):
    if name[element] == 'i':
        continue
    else:
        print(name[element])


name = input("Your Name: ")
for element in range(0, len(name)):
    if name[element] == 'i':
        continue
    else:
        print(name[element], end='')
'''



'''
#Fibonacci sequence
length = int(input("Enter length of series: "))
firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
print(str(firstNumber) + "," + str(secondNumber),end = ",")
for i in range(2,length):
    next = firstNumber + secondNumber
    print(next, end=",")
    firstNumber = secondNumber
    secondNumber = next
'''




'''
#Program to check for prime
var = int(input("Enter Number: "))
flag=1
for i in range(2,var):
    if var%i==0:
        flag=0
        break
    else:
        flag=1
if flag==0:
   print("Number is not prime")
else:
    print("Number is prime")
'''




'''
#Check for palindrome
name = input("Enter name: ")
if name.lower()[::] == name.lower()[::-1]:
    print(name," is a Palindrome")
else:
    print(name," is not a Palindrome")
'''



'''
#Counting different datatypes
mainString = 'Python 2019 Batch'
countChar = countDigit = 0
for i in mainString:
    if i.isalpha():
        countChar += 1
    elif i.isdigit():
        countDigit += 1
    else:
        pass
print("Number of characters: ",countChar)
print("Number of digits: ",countDigit)
'''



'''
#Checking for Anagram
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")
if sorted(name1) == sorted(name2):
    print("They are Anagrams")
else:
    print("They are not Anagrams")
'''



'''
#Input into list
elements = int(input("Enter number of elements: "))
lst = []
for ele in range(elements):
    print("Enter Element", ele+1, ende+',')
'''



'''
#Splitting

name = input("What is your name: ")
var = name.split()
print(var)


name1, name2 = input('What are the names: (with,splitting): ').split(',')
print(name1,name2)
'''


'''
#Joining

lst = [10, 20, 30]
string = "-".join(str(e) for e in lst)
print(string)
'''


'''
#Ammending Lists

lst = [20, 10, 30, 40]
lst.append(999)         #Adds a value to the list
print(lst)

lst[2]=500              #Replaces a value in the list
print(lst)

lst[3:4]=111,222        #Replaces multiple values in list
print(lst)

del lst[0]              #Deletes a term in the list by index
print(lst)

lst.remove(111)         #Deletes a term in the list by value
print(lst)

print(lst.index(999))   #Prints index value of the term





#Aliasing
lst = [10, 20, 30, 40]
lst1 = lst
lst[2] = 30
print(lst1)



#Copying
lst = [1, 2, 3, 4, 5]
lst1 = lst.copy()



#Pop
print(lst.pop()) #Removes last term of the list and prints it out
'''


'''
#Sorting
lst = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday]
print("Original: ",lst)
print("Sorted: ", sorted(lst, reverse = True))
'''


'''
#EmployeeData
name = input("Enter name: ")
age = int(input("Enter age: "))
salary = float(input("Enter salary: "))
lst = []
lst.append(name)
lst.append(age)
lst.append(salary)

name1 = input("Enter name 2: ")
age1 = int(input("Enter age 2: "))
salary1 = float(input("Enter salary 2: "))
lst1 = []
lst1.append(name1)
lst1.append(age1)
lst1.append(salary1)

name2 = input("Enter name 3: ")
age2 = int(input("Enter age 3: "))
salary2 = float(input("Enter salary 3: "))
lst2 = []
lst2.append(name2)
lst2.append(age2)
lst2.append(salary2)

mainlst = []
mainlst.append(lst)
mainlst.append(lst1)
mainlst.append(lst2)
print(mainlst)
'''



'''
#Functions
def primex(var):
    for i in range(2,var):
        if var%i==0:
            flag=0
            break
        else:
            flag=1
    if flag==0:
        print("Number is not prime")
    else:
        print("Number is prime")
n = eval(input("Enter Number: "))
primex(n)


def divbyfive(var):
    if var%5==0:
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")

n = eval(input("Enter Number: "))
divbyfive(n) 


div = lambda a: a**0.5
n = eval(input("Enter Number: "))
div(n)
'''



#FileHAndling
'''
f = open('myfile.txt',"a")
str = input("Enter my text: ")
f.write(str)
f.close()
'''
'''
f = open("myfile.txt",'r')
str = f.read()
print(str)
f.close()
'''

f = open("myfile.txt",'w')
print("Enter text (@ at the end): ")
while str != '@':
    str = input()
    if str != '@':
        f.write(str + '\n')
        

