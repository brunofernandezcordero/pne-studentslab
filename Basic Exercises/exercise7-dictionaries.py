student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

grades = student["grades"]
count = 0
for i in grades.values():
    count += i
    avg = count / len(grades)
    avg = round(avg,2)

print("Name:",student["name"])
print("Number of subjects:", len(student["subjects"]))
print("Enrolled in PNE:","PNE" in student["subjects"])
print("Databeses grade:", student["grades"]["Databases"])
print("Average grade:",avg)
for i in grades.items():
    print(f"{key}: {value}")