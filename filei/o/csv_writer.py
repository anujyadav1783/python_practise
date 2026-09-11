import csv

# User se student ka name aur home lena.
name = input("What's your name? ")
home = input("Where's your home? ")


# ============================================================================
# Method 1: csv.DictWriter
# ============================================================================
# DictWriter dictionary ke saath kaam karta hai.
# Dictionary mein keys column names hoti hain: "name" aur "home".
#
# Is method mein fieldnames bahut important hain.
# fieldnames CSV ke columns ke naam aur unka order define karta hai.
#
# "a" ka matlab append mode hai.
# Append mode purana data delete nahi karta; nayi row file ke end mein add karta hai.
with open("students_dictwriter.csv", "a", newline="", encoding="utf-8") as file:
    # DictWriter ko bataya ja raha hai ki CSV mein kaunse columns honge.
    writer = csv.DictWriter(file, fieldnames=["name", "home"])

    # Dictionary ko CSV ki ek row mein convert karke save karta hai.
    writer.writerow({"home": home, "name": name})


# ============================================================================
# Method 2: csv.writer
# ============================================================================
# csv.writer list ya tuple ke saath kaam karta hai.
# Isliye row ko [name, home] ke order mein dena zaroori hai.
#
# Is method mein column names use nahi hote.
# CSV ka order humein khud yaad rakhna padta hai:
# pehla value name column mein aur doosra value home column mein jayega.
with open("students_writer.csv", "a", newline="", encoding="utf-8") as file:
    # Simple writer object banaya.
    writer = csv.writer(file)

    # List ki values ko CSV ki ek row ke roop mein save karta hai.
    writer.writerow([name, home])


# ============================================================================
# Dono methods ka difference aur use case
# ============================================================================
# 1. csv.DictWriter
#    - Dictionary ke saath kaam karta hai.
#    - fieldnames se columns clearly define hote hain.
#    - writer.writerow({"name": name, "home": home}) likhna readable hai.
#    - Bahut saare columns wale data ke liye useful hai.
#    - Agar columns ka order change ho jaye, keys ki wajah se code samajhna easy hai.
#
# 2. csv.writer
#    - List ya tuple ke saath kaam karta hai.
#    - Values ka order bahut important hota hai.
#    - writer.writerow([name, home]) simple aur short hai.
#    - Chhote aur fixed-format data ke liye useful hai.
#    - Jab rows list ke form mein already available hon, tab ye convenient hai.
#
# Kaunsa better hai?
# - Readability, many columns, aur mistakes kam karne ke liye DictWriter better hai.
# - Simple two-three columns aur short code ke liye csv.writer enough hai.
# - General projects mein main DictWriter prefer karunga, kyunki keys se clear hota hai
#   ki kaunsi value kis column mein ja rahi hai.
#
# Important:
# - Dono writers file mein data append kar rahe hain.
# - Isliye program har baar run karne par nayi row add karega.
# - "w" mode use karne par purani file overwrite ho jayegi.
# - newline="" Windows par extra blank lines se bachne ke liye use kiya gaya hai.
