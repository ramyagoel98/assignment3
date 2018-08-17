lists=[1,2,3,5,4,7,10,6,9]
even=0
odd=0
for x in lists:
    if(x%2==0):
      even=even+1
    else:
      odd=odd+1
print('count of Even no is: ',even)
print('count of Odd: ',odd)

