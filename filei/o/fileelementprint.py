name=[]
with open("index.txt","r") as file:
    for line in file:
        name.append(line.strip())
for element in sorted(name):
    print("hello",element)