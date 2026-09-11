# # name=input("enter your name")
# # city=input("enter your city")
# # with open("name.csv","a") as file:
# #     file.write(f"{name},{city}\n")
# # print("data updated ")

# # Open name.csv in read mode to read the saved name and city data.
# with open("name.csv") as file:
#     # Process the CSV file one row at a time.
#     for line in file:
#         # Remove the line break, then split the row at the comma.
#         row = line.rstrip().split(",")

#         # row[0] is the name and row[1] is the city.
#         print(f"{row[0]} live in {row[1]}")

# students = []

# with open("name.csv") as file:
#     for line in file:

#         # Remove newline and split CSV data at comma
#         name, house = line.rstrip().split(",")

#         # Create a sentence and add it to the list
#         students.append(f"{name} is in {house}")

# # Sort students alphabetically and print each one
# for student in sorted(students):
#     print(student)
# Store each CSV row as a dictionary in this list.
student=[]

# Read the name and city values from the CSV file.
with open("name.csv") as file:
    for line in file:
        name,city=line.rstrip().split(",")

        # Create one dictionary for the current student.
        students={ "name":name,"city":city}
        # students["name"]=name
        # students["city"]=city
        student.append(students)

# Return the name used to sort each dictionary.
# sorted() will call this function once for every dictionary.
def get_name(student):
    return student["name"]

# key tells sorted() which value to compare when ordering the records.
# We pass get_name without parentheses because sorted() needs the function
# itself so it can call get_name(student) for every item.
# Writing get_name() would call the function immediately without an argument
# and would return a string instead of giving sorted() a function to use.
# reverse=False is the default, so the names are sorted from A to Z.
for students in sorted(student,key=lambda students:students["city"]):
    print(f"{students['name']} is in {students['city']}")
          # Lambda Function:
# A lambda function is a small anonymous function written in one line.
# Syntax: lambda arguments: expression
# Example: lambda student: student["name"]
# It takes one student and returns the student's name.
#
# sorted():
# sorted() is used to sort items in a list and returns a new sorted list.
# The key parameter tells sorted() what value to use for sorting.
# Example: sorted(students, key=lambda student: student["name"])
# This sorts the students alphabetically by their name.