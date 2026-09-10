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

students = []

with open("name.csv") as file:
    for line in file:

        # Remove newline and split CSV data at comma
        name, house = line.rstrip().split(",")

        # Create a sentence and add it to the list
        students.append(f"{name} is in {house}")

# Sort students alphabetically and print each one
for student in sorted(students):
    print(student)