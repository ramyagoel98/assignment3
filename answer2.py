l=[]
n=int(input("enter no of elements in list"))
for i in range (n):
    x=input("enter value")
    l.append(x)
print(l)
l2=['google','apple','facebook','microsoft','tesla']
l.extend(l2)
print(l)
