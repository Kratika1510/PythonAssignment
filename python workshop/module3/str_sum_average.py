import re
str="English=78 Science=83 Math =68 History=65"
marks=[int(num)for num in re.findall(r'\b\d+\b',str)]
totalMarks=0
for mark in marks:
    totalMarks+=mark
percentage=totalMarks/len(marks)
print("Total marks is: ",totalMarks,"Percentage is",percentage)
