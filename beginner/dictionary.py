student={'name':'Rupsa','age':19,'height':171}
print(len(student))
print(str(student))
print(dict.keys(student))
print(dict.values(student))
print(dict.items(student))
stud={'roll':41}
student.update(stud)
print(student)
print(student.get('age'))
#or print(student['age'])
#list to dictionary
num=[1,2,3,4,5,7,6]
dict_sq={k:k**2 for k in num}
print(dict_sq)
