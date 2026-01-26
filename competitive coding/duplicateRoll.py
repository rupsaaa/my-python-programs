'''Detect Duplicate Student Roll Number
In a school, roll numbers are assigned from 1 to N. But due to a system issue, one roll number is assigned to two students. The school wants you to identify the duplicate roll number.
Input Format
First line: Integer N (number of students).
Second line: N+1 integers (roll numbers recorded).
Output Format
Print the duplicate roll number.'''


N=int(input())
dt={}
for i in range (0,N+1):
    n=int(input())
    if n not in dt:
       dt[n]=i
    else:
        c=n
print(c)

