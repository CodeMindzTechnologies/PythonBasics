"""
Create a empty student dictionary and add first_name, last_name, gender, age, marital status, skills, address as keys 
for the dictionary with values. Print the values in dictionary using the keys
"""
student = { }

# Keys can be in single or double quote. 
# String Values can also be in single or double quote
student['first_name'] = "Mark"   
student['last_name'] = "Donald"
student['gender'] = "Male"
student['age'] = 30
student['is_marred'] = True
student['skills'] = ['Java', 'SQL', 'Python']
student['address'] = {
        'street':'MG street',
        "city": "Delhi",
        'country': 'India',
        'zipcode':'02210'
        }

print("First Name: ",student['first_name'])
print("Last Name: ",student['last_name'])
print("Gender: ",student['gender'])
print("Age: ",student['age'])
print("Married: ",student['is_marred'])
print("Skills: ",student['skills'])
print("Address: ")
print("     Street Name: ",student['address']['street'])
print("     City: ",student['address']['city'])
print("     Country: ",student['address']['country'])
print("     ZipCode: ",student['address']['zipcode'])
