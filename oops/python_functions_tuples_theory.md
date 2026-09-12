# Python Notes: Functions, Dictionaries, and Object-Oriented Basics

## 1. What is a function?
A function is a reusable block of code.
It helps us break a program into smaller, manageable parts.

```python
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")
```

A function is created using `def` and can be called later.

Why use functions?
- reusability
- cleaner code
- easier debugging
- better organization

---

## 2. Function call and return values
A function can take input, process it, and return a result.

```python
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}
```

This function:
- asks the user for a name
- asks the user for a house
- returns both values together as a dictionary

---

## 3. What is a dictionary?
A dictionary stores data as key-value pairs.

```python
student = {
    "name": "Harry",
    "house": "Gryffindor"
}
```

In this dictionary:
- `"name"` is the key
- `"Harry"` is the value
- `"house"` is the key
- `"Gryffindor"` is the value

This is better than storing values in separate variables when the data is related.

---

## 4. Accessing dictionary values
We access values using square brackets with the key.

```python
student["name"]
student["house"]
```

Example:

```python
print(student["name"])   # Harry
print(student["house"])  # Gryffindor
```

This is a simple and readable way to work with structured data.

---

## 5. Example: dictionary-based program
```python
def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()
```

### What happens here?
1. `main()` calls `get_student()`.
2. The function returns a dictionary.
3. The dictionary contains the student's name and house.
4. We check if the name is `Padma`.
5. If yes, we change the house to `Ravenclaw`.
6. Then we print the final result.

---

## 6. Why use `main()`?
`main()` is the main function that starts the program.

```python
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")
```

This keeps the program clean and organized.
The central logic is placed in one function.

---

## 7. What is the meaning of `if __name__ == "__main__":`?
This line is used to check whether a file is being run directly.

```python
if __name__ == "__main__":
    main()
```

Meaning:
- If the file is run directly, Python calls `main()`.
- If the file is imported into another file, it does not run automatically.

This is a standard Python pattern used in real programs.
8. Object-oriented version of the same idea
The same concept can also be written using a class.

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student(input("Name: "), input("House: "))
    return student


if __name__ == "__main__":
    main()
```

### Key idea
A class is a blueprint for creating objects.
An object stores attributes like `name` and `house`.

`student.name` and `student.house` are accessed using dot notation.

This is the object-oriented approach to the same problem.

---

## 9. Dictionary vs class
Dictionary style:

```python
student = {"name": "Harry", "house": "Gryffindor"}
print(student["name"])
```

Class style:

```python
student = Student("Harry", "Gryffindor")
print(student.name)
```

### When to use which?
- Use a dictionary for simple related data.
- Use a class when you want structure and behavior together.

---

## 10. Example output
```python
Name: Harry
House: Gryffindor
Harry from Gryffindor
```

---

## 11. Main concepts covered
This topic teaches:
- functions
- return values
- dictionaries
- key-value pairs
- conditionals
- `main()`
- `if __name__ == "__main__":`
- classes and objects

These are some of the most important foundations of Python programming.

---

## 12. Final summary
Python programs become easier to read and manage when we organize code into functions.
We can return data as a dictionary or as an object.
The `main()` function controls the flow of the program, and `if __name__ == "__main__":` ensures the program runs only when executed directly.

This is the basis of writing clean, real-world Python applications.
