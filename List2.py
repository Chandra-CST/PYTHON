
  FIND THE GREATEST ELEMENT AND PRINT ITS INDEX AS WELL:

num = [1,10,4,7,9,12,14,8]

largest = num[0]
index = 0
for i in range(len(num)):
    if num[i] > largest:
        largest = num[i]
        index = i
    
print(f'The Greatest Element is:', largest)
print(f'And the index is:', index)
           
  FIND THE SECOND LARGEST ELEMENT:

num = [1,3,6,7,12,45,9,0]

largest = num[0]
secondlargest = num[0] 

for i in  range(1,len(num)):
    if num[i] > largest:
        secondlargest = largest
        largest = num[i]
    elif num[i] < largest and num[i] > secondlargest:
        secondlargest = num[i]

print('The Second Largest Number is :', secondlargest)
           
           
           
