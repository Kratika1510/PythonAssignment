a=input("Enter the first name: ")
i=[]
i.append(a)
for m in range(5):
    k=int(input("Enter the theory number: "))
    i.append(k)
for n in range(3):
    k=int(input("Enter the practical number: "))
    i.append(k)
#print(i)
j=i[1:6]
#print(j)
jsum=sum(j)
k=i[6:9]

ksum=sum(k)
s=sum(j+k)
#print(s)
per=(s/500)*100
#print(per,"%")
print("Robert obtained ",jsum," marks out of 460 in theory and ",ksum," marks out of 40 in practical and successfully passed the exam with ",per," in aggregate.Many congratulations to Robert.")




    
    
