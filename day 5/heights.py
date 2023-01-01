student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
height=0
for i in student_heights:
    height+=i
stud=0
for no_of_stud in student_heights:
    stud+=1
average=height/stud
ans=round(average)
print(ans)