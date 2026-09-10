# name=input("enter your name")
# city=input("enter your city")
# with open("name.csv","a") as file:
#     file.write(f"{name},{city}\n")
# print("data updated ")

# Open name.csv in read mode to read the saved name and city data.
with open("name.csv") as file:
    # Process the CSV file one row at a time.
    for line in file:
        # Remove the line break, then split the row at the comma.
        row = line.rstrip().split(",")

        # row[0] is the name and row[1] is the city.
        print(f"{row[0]} live in {row[1]}")
