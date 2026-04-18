Merging two dictionaries:

d1 = {10:100,20:200,30:300}
d2 = {40:400,50:500,60:600} 

d3 = d1 | d2

print(d3)

WRITE A PYTHON PROGRAM TO SUM ALL THE VALUES IN A DICTIONARY:

D1 = {'A':10,'B':15,'C':20,'D':25}
total = 0
for i in D1.values():
    total += i
print('The sum of all the values inside a dictionary is:', total)


 COUNT THE FREQUENCY OF EACH ELEMENTS:

a = [1,1,1,1,2,2,2,3,3,4,4,45,5,6,6]

d1 ={}
for i in a:
    if i in d1.keys():
        d1[i] += 1
    else:
        d1[i] = 1
print(d1)

WRITE A PYHTON PROGRAM TO COMBINE TWO DICTIONARY BY ADDING VALUES FOR COMMON KEYS:

d1 = {'A': 1,'B': 2 ,'C': 3,'D': 4,'E': 5,'F': 6}
d2 = {'D': 1,'E': 2 ,'F': 3,'G': 7,'H': 8,'I': 9}

for i in d2:
    if i in d1.keys():
       d1[i] += d2[i]
    else:
        d1[i] = d2[i]
print(d1)

