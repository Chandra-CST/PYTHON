Write a program to find the sum of all even numbers in the list:

a = [12, 7, 9, 20, 33, 18, 5, 2]
sum = 0
for i in a:
    if i % 2 == 0:
        sum = sum + i
print("The sum of all Even numbers are:" , sum)

Write a program to count the number of vowels in the string:

A = "programming is fun"
vowel = ['a','e','i','o','u']
count = 0

for i in A:
    if i in vowel:
        count += 1
print(count)
   
 Count frequency of characters in:

a = "banana"
d1 = {}

for i in a:
    if i in d1.keys():
        d1[i] += 1
    else:
        d1[i] = 1
print(d1)

Write a program to print all numbers from 1 to 50 that are divisible by both 3 and 5:

for i in range(1, 51):
    if i % 3  == 0 and i % 5 == 0:
        print(i) 

Write a program to reverse the string:

a = "python"
for i in range(len(a)-1,-1,-1):
    print(a[i], end="")















# MEDIUM LEVEL QUESTIONS :

 Write a program to find the smallest element and its index in:

A = [45, 12, 78, 3, 25, 10]
smallest = A[0]
index = 0

for i in range(len(A)):
    if A[i] < smallest:
        smallest = A[i]
        index = i
print('The Smallest Element of the list is :',smallest)


 Write a program to count the frequency of each character in:

a = "banana"
d1 = {}     # for counting we use an empty dictionary
for i in a:
    if i in d1.keys():
        d1[i] += 1
    else:
        d1[i] = 1
print(d1)
