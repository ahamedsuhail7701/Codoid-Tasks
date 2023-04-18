#1) IMPLEMENT FACTORIAL USING RECURSION

"""def fact(n):

    if n == 1:
        return n
    elif n < 0:
        print("Sorry, factorial Doesn't Exist For Negative Numbers")
    else:
        return n*fact(n-1)

num = int(input("Enter the number To find Factorial of a Number : "))
print("factorial of a Number :", fact(num))"""

#4 Print All Pronic Numbers From 1 to 100

"""def ispronicnumber(num):
    i = 0
    flag = 0
    while i<= num:
        if num == i *(i+1):
            flag = 1
            break
        i = i+1
    return flag

minpro = int(input("Enter the minimum Pronic Number ="))
maxpro = int(input("Enter the maximum Pronic Number ="))
print("\nThe List of pronic Numbers from {0} and {1}".format(minpro, maxpro))
for i in range(minpro, maxpro):
    if(ispronicnumber(i) ==1):
        print(i, end =' ')"""

#5)a Implement Method Overloading in python

"""def sum_numbers(*args):
    result = 0

    for num in args:
        result += num
    print("sum :", result)

if (__name__ == "__main__"):
    print("Method overloading\n")
    print("Single argument   ->", end = " ")
    sum_numbers(10)

    print("Two arguments   ->", end=" ")
    sum_numbers(30 , 2)

    print("Multiple arguments   ->", end=" ")
    sum_numbers(1 ,2, 3, 4, 5)"""

#5)b Implementation of method Overriding In python
"""class A:
    def first(self):
        print("First function of class A")

    def second(self):
        print('Second function of class A')



class B(A):
    # Overriden Function
    def first(self):
        print("Redefined function of class A in class B")

    def display(self):
        print('Display Function of Child class')

if (__name__ == "__main__"):
    child_obj = B()

    # Calling the overridden method
    print("Method Overriding\n")
    child_obj.first()
    A().first()"""

#6) Python Program To Print Duplicate Vales of Array List

"""arr = [1,2,3,4,7,4,8,8,3]

print("Duplicate elements in given array:")

for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i] == arr[j]):
            print(arr[j])"""

#7) python Program to Print Elements of array in reverse order

"""arr = [1, 2, 3, 4, 5]
print("Original array: ")
for i in range(0, len(arr)):
    print(arr[i])   
print("Array in reverse order: ")
#Loop through the array in reverse order
for i in range(len(arr)-1, -1, -1):
    print(arr[i])"""

#8) Python program to Determine whether the given number is a Harshad Number

"""num = int(input("Enter the number :"))
rem = sum = 0

# Make a copy of num and store it in variable n    
n = num

# Calculates sum of digits
while (num > 0):
    rem = num % 10
    sum = sum + rem
    num = num // 10

# Checks whether the number is divisible by the sum of digits
if (n % sum == 0):
    print(str(n) + " is a harshad number")
else:
    print(str(n) + " is not a harshad number")"""

#9) Implement a program to merge two arrays

"""def append_lists():
    # list 1
    ls1 = [1, 2, 3, 4]
    # list 2
    ls2 = [5, 6, 7, 8]
    for i in ls2:
        ls1.append(i)
    print(ls1)
append_lists()"""

#12) Python Program for Fibonacci Series

"""nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1"""
#58) Change the Vowel characters to "S"  Python


"""text = input("Enter the text :")
new_var = " "
for char in text:
    if char.lower() in 'aeiou':
        new_var = text.replace(char,"S")
print(new_var)"""

#57) Find The largest Number in an array without Predefine function

"""l = list(map(int,input("Enter array Elements:").split(" ")))
max_1 =l[0]
for i in range(1,len(l)):
    if(l[i]>max_1):
        max_1 = l[i]
print(max_1)"""

#55)Python program to check the vowels in the string

"""text = input("Enter the text :")
for char in text:
    if char.lower() in 'aeiou':
       print(char)"""

#53)Program to check the string is Palindrome or not

"""def ispalindrome(s):
    return s ==s[::-1]

s = input("Enter the text: ")
ans = ispalindrome(s)

if ans:
    print("yes it is a palindrome String")
else:
    print("No it is not a Palindrome")"""

#51) program to print all prime numbers between regular intervlas

"""lower_value = int(input("Enter Lowest Range Value:"))

upper_value = int(input("Enter highest range value :"))

print("prime Numbers in Between given Intervals are :")

for number in range(lower_value,upper_value+1):
    if number >1:
        for i in range (2,number):
            if (number%i) ==0:
                break
        else:
            print(number)"""

#50) Swap two variables with out using Third variables

"""x = 5
y = 7

print("Before swapping:")
print("Value of x:",x,"and y:",y)
x,y = y,x
print("After swapping:")
print("Value of x:",x,"and y:",y)"""
