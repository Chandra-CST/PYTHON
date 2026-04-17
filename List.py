 MEAN OF ALL LIST ELEMENTS:

num = [1,4,7,12,45,9,0]
total = 0  

for i in num:
    total += i

mean = total/ len(num)
print('mean', mean)


           
 PRINT POSITIVE AND NEGATIVE ELEMENTS SEPERATELY:

Num = [-34,-12,43,56,10,-10,-20,20,30,-30]
print('The Positive Elements are: ')
for i in Num:
    if i >= 0:
        print(i)

print('The Negative Elements are: ')
for i in Num:
    if i<=0:
        print(i)
           
           
