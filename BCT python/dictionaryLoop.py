students = {"Sam": 85, "Joe": 65, "Mia": 92}           
for name, marks in students.items():                    
    if marks > 70:
        print(f"{name} scored above 70")
avg = sum(students.values()) / len(students)        
print(f"Average Marks: {avg}")