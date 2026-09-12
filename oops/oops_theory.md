# Object-Oriented Programming (OOP) Theory

## 1. What is OOP?
OOP means writing code by creating objects that contain both data and behavior.

For example, a `Student` object can store:
- name
- house

and can also have methods to validate or print itself.

---

## 2. What is a class?
A class is a blueprint for creating objects.

```python
class Student:
    pass
```

It describes what the object should look like and what it can do.

---

## 3. What is an object?
An object is an actual instance of a class.

```python
student = Student()
```

So the class is the design, and the object is the actual created thing.

---

## 4. `__init__` method
`__init__` runs automatically when a new object is created.

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
```

This means:
- `self` refers to the current object
- `self.name` stores the name
- `self.house` stores the house

---

## 5. Why do we need validation?
Because we do not want invalid values to enter the object.

If someone writes:

```python
student.house = "Mars"
```

that should not be allowed, because houses must be only one of the Hogwarts houses.

So we add checks:

```python
if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
    raise ValueError("Invalid house")
```

This ensures data is valid before saving it.

---

## 6. What is `raise ValueError`?
It is Python’s way of saying:

“Something is wrong, stop the program and show an error.”

Example:

```python
raise ValueError("Invalid house")
```

This prevents bad data from being stored.

---

## 7. What is a getter?
A getter is a method used to read an attribute in a controlled way.

```python
@property
def house(self):
    return self._house
```

This means when we write:

```python
student.house
```

Python calls the getter and returns the value.

The getter is useful because we can decide how data is read.

---

## 8. What is a setter?
A setter is a method used to assign or update a value safely.

```python
@house.setter
def house(self, house):
    if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
        raise ValueError("Invalid house")
    self._house = house
```

This means when we do:

```python
student.house = "Ravenclaw"
```

Python runs the setter first.

If the value is invalid, it raises an error.
If it is valid, it stores it.

---

## 9. Why use `@property` and `@house.setter`?
Because we want to look like we are using a normal attribute, but we still want to protect the data.

Without property methods, we might do this:

```python
student.house = "Mars"
```

and no validation would happen.

With properties, we write:

```python
student.house = "Ravenclaw"
```

but the setter checks it first.

So the syntax stays simple while the logic stays safe.

---

## 10. Why do we use `_house`?
Because `house` is being used as the property name.

We store the real value in `_house` so that the getter and setter can manage it safely.

Example:

```python
self._house = house
```

This keeps the property and the underlying storage separate.

---

## 11. What is `__str__`?
`__str__` defines how the object should appear when printed.

```python
class Student:
    def __str__(self):
        return f"{self.name} from {self.house}"
```

Now:

```python
print(student)
```

prints:

```python
Harry from Gryffindor
```

This makes the object easier to read.

---

## 12. Full advanced example
```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
```

### What is happening here?
- `__init__` creates the object
- `house` property protects attribute access
- setter validates the house before assigning
- `__str__` prints the student nicely

---

## 13. Why this is important
This is an advanced OOP pattern used in real programs.

It helps with:
- data validation
- safe attribute access
- clean code structure
- better object design

This is why professionals use property methods in classes.

---

## 14. Very short summary
A getter lets us read the value safely, and a setter lets us assign it safely.
The `@property` decorator makes it look like a normal attribute while still running checks.

So the class remains controlled and protected.

That is why properties are used here.
