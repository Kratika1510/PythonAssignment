l1=int(input("enter the size of list 1"))
li1=[]
for i in range(l1):
    a=int(input(""))
    li1.append(a)
l2=int(input("enter the size of list2 one less tham list1"))
li2=[]
for j in range(l2):
    b=int(input(""))
    li2.append(b)
    
for k in range(len(li1)):
    if li1[k] not in li2:
        print(li1[k])
