import re

# Ask the user to enter a name
name = input("enter the name : ")

# Check whether the input matches this pattern:
# starts with something, then a comma and space, then something else
# Example valid input: "Kumar, Anuj"  (this pattern is for normal names, not with braces)
# But the current pattern is written as r"^{.+}, {.+}$", which expects curly braces around both parts
# Example it looks for: {Kumar}, {Anuj}
matches = re.search(r"^{.+}, {.+}$", name)

# If a match is found, swap the name order
if matches:
    # matches.group() returns the whole matched string
    # Example: "{Kumar}, {Anuj}"
    # This line is not correct for normal names because it unpacks characters one by one
    last, first = matches.group()
    name = f"{first}+{last}"

# Print the final result
print(name)