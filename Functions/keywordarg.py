def student(roll,name,course="UG"):
    print("Name:",name)
    print("Roll no:",roll)
    print("Course:",course)
student(course="UG",roll=41,name="Rupsa")#changing the order of parameters using keyword by which the compiler matches it with func parameters
student(roll=41,name="Rupsa")#omitting course as it is a default