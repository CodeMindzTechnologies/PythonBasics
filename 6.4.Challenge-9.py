"""
Create a python Script with an empty list. 
The script should ask top 3 favourite subjects one by one and add these to the list. 
Last, it should Print my favourite subjects are: [subject1], [subject 2] and [subject 3]
"""
subjects = []
fav_subject_1 = input("Enter your 1st Favorite Subject: ")
fav_subject_2 = input("Enter your 2nd Favorite Subject: ")
fav_subject_3 = input("Enter your 3rd Favorite Subject: ")

subjects.append(fav_subject_1)
subjects.append(fav_subject_2)
subjects.append(fav_subject_3)

print("my favourite subjects are: ",subjects[0],subjects[1],subjects[2])
