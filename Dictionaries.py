

# DICTIONARIES
#store information in key-value pairs and all keys are unique
student = {
    'name': 'Dorcas',
    'age': 21,
    'course': 'Computer Science',
    'year': 3,
    'paid_fees': True
}

print(student['name'])
print(student.get('course'))

student['grade'] = 'A'
print(student['grade'])