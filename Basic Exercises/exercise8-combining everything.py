students = [
    {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
    {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
    {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
    {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
    {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
]

def average(grades):
    count = 0
    for i in grades:
        count += i
    avg = count / len(grades)
    avg = round(avg,1)
    return avg

def get_status(avg):
    if avg >= 5.0:
        status = "PASS"
    else:
        status = 'FAIL'
    return status

for student in students:
    print(f'{student['name']}: {average(student['grades'])} -> {get_status(average(student['grades']))}')