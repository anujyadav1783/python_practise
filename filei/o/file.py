# Ask the user for the name that should be saved.
name = input("Enter the name: ")

# Open index.txt in append mode so existing names are kept.
file = open("index.txt", "a")

# Write the name and move to a new line for the next entry.
file.write(f"{name}\n")

# Close the file after writing to release the file resource.
file.close()