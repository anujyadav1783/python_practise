import csv

# Students ki dictionaries is list mein store hongi.
# List multiple records ko store karne ke liye use hoti hai.
students = []

# CSV file ko read mode mein open kar rahe hain.
with open("name.csv") as file:
    # csv.reader file ki har row ko list ki form mein read karta hai.
    # Example row: ["anuj ", "ricco"]
    reader = csv.reader(file)

    # Har row ke do columns ko name aur home variables mein unpack kar rahe hain.
    for name, home in reader:
        # Dictionary data ko key-value pairs mein store karti hai.
        # "name" aur "home" keys hain; name aur home unki values hain.
        # Example: {"name": "Harry", "home": "Number Four"}
        # Isse student["name"] aur student["home"] se values read kar sakte hain.
        # Har row ko dictionary bana kar students list mein add kar rahe hain.
        students.append({"name": name, "home": home})


# sorted() ek nayi sorted list return karta hai.
# key batata hai ki har student mein kis value ke basis par sorting karni hai.
# lambda student: student["name"] ek chhota function hai jo name return karta hai.
# lambda ko () se call nahi karte, kyunki sorted() is function ko har student ke liye
# khud call karta hai. Agar lambda ke baad () lagayenge, function turant call ho jayega.
for student in sorted(students, key=lambda student: student["name"].strip()):
    # student ek dictionary hai.
    # Dictionary mein [] ke andar key likhkar uski value read karte hain.
    # Yahan student["name"] name aur student["home"] home return karta hai.
    print(f"{student['name'].strip()} is from {student['home'].strip()}")

# -----------------------------------------------------------------------------
# csv.DictReader ka example
# -----------------------------------------------------------------------------
# DictReader tab useful hota hai jab CSV ki first row column names (headers) ho.
# students.csv mein headers "name,home" hain, isliye har row automatically
# dictionary banegi, jaise: {"name": "Harry", "home": "Number Four"}.
students_from_dict_reader = []

with open("students.csv",) as file:
    # DictReader header names ko dictionary ki keys ke roop mein use karta hai.
    # Isliye humein name aur home ko manually unpack nahi karna padta.
    reader = csv.DictReader(file)

    # row har baar ek dictionary hoti hai.
    for row in reader:
        # row se values keys ke through read karke apni list mein save kar rahe hain.
        students_from_dict_reader.append(
            {"name": row["name"], "home": row["home"]}
        )
# DictReader ka use case:
# Jab CSV mein bahut saare columns hon, jaise name, home, age, course,
# tab row["name"] zyada clear hota hai row[0] ke comparison mein.
# Column order badalne par bhi keys ke naam same rahen to code readable rehta hai.
print("\nUsing csv.DictReader:")
for student in sorted(
    students_from_dict_reader,
    key=lambda student: student["name"].strip(),
):
    print(f"{student['name'].strip()} is from {student['home'].strip()}")
