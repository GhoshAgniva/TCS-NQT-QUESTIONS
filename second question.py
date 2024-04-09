st=input("enter input")
s=tuple(st)
a=0
b=0
for i in s:
    if i=='*':
        a=a+1
    elif i=='#':
        b=b+1
    
    

if a>b:
    print("positive")
elif a<b:
    print("negetive")
elif a==b:
    print("0")