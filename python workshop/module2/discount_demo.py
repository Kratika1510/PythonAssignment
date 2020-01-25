qty=int(input("Enter the number of packages purchased: "))
if qty in range(10,20):
    dis=0.10
    print(10%)
elif qty in range(20,50):
    dis=0.20
    print(20%)
elif qty in range(50,100):
    dis=0.30
    print(30%)
else:
    dis=0.40
    print(40%)
#k=dis*99   
a=(99*qty)*dis
k=(99*qty)-a

print(k)
    
