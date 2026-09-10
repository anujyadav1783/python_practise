
# Open the names.txt file in read ("r") mode
# "file" is the variable/reference used to access the opened file
with open("index.txt", "r") as file:

    # Read all lines from the file
    # readlines() returns the lines as a list
    lines = file.readlines()


# Go through the list one line at a time
for line in lines:

    # Print "hello," followed by the current line/name
    print("hello,", line.rstrip())