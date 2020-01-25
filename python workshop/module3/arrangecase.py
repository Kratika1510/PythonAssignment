a=input("Enter the string: ")
i=[x for x in a ]

#for k in a:
#    i.append(k)
print(i)
i.sort(reverse=True)
res = ''.join(map(str,i))
print(str(res))

  
    
