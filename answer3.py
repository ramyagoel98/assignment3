l=[]
n=int(input("enter no of elements in list"))
for i in range (n):
    x=input("enter value")
    l.append(x)
print(l)

xx=input("enter object to be searched")
p=l.count(xx)
print("number of times %s has occured in list is %s" % (xx,p))
