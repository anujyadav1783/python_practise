# User se name lena
name = input("Enter the name: ")

# File ko append mode me open karna; purana data safe rahega
with open("index.txt", "a") as file:
    # Name ko new line ke saath save karna
    file.write(f"{name}\n")