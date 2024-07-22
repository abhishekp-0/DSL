n=int(input("Enter total no. of students:"))
marks=[]

no_present_students=0
percentage_passed=0
print("Enter Marks of students out of 100:")
for i in range(n):
    x=int(input())
    if(x>=0):
        marks.append(x)
        no_present_students+=1
        if(x>40):
            percentage_passed+=100/n

highest_frequency=0
highest_frequency_marks=marks[0]
for i in marks:
	if(marks.count(i))>highest_frequency:
		highest_frequency=marks.count(i)
for i in marks:
	if(marks.count(i))==highest_frequency:
		highest_frequency_marks=i
		
marks.sort()




print("Number of Present: ",no_present_students)
print("Highest marks: ", max(marks))
print("Lowest Marks" , min(marks))
print("Average marks: ", sum(marks)/n)
print("Percentage of students passed: ", percentage_passed)
print("Percentageof Students Failed: ", 100-percentage_passed)
print("Marks with highest frequency is ", highest_frequency_marks)

