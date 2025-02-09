# CONSTRUCTOR
# 1. Constructor in Python
A **constructor** in Python is a special method used to initialize objects. The constructor is called automatically when a new object of a class is created. In Python, the `__init__` method serves as the constructor.

**Purpose and Usage:**
- Initialize the object's attributes
- Set up initial states for new objects

# 2. Parameterless vs Parameterized Constructor
- **Parameterless Constructor:** No arguments other than `self`.
- **Parameterized Constructor:** Takes additional parameters to initialize attributes.

# 3. Defining a Constructor
```python
class Example:
    def __init__(self, value):  # Constructor
        self.value = value
```

# 4. `__init__` Method
The `__init__` method initializes the object's attributes when an instance is created.

# 5. `Person` Class Example
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object
person = Person("Alice", 30)
```

# 6. Explicitly Calling Constructor
```python
person = Person.__new__(Person)
Person.__init__(person, "Bob", 25)
```

# 7. Significance of `self`
`self` represents the instance and is used to access attributes and methods.

# 8. Default Constructors
A default constructor takes only `self` and is used when no specific initialization is needed.

# 9. `Rectangle` Class Example
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

# 10. Multiple Constructors
Python doesn't support multiple constructors directly but can be implemented using default arguments or class methods.

```python
class Example:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
```

# 11. Method Overloading
Python doesn't support method overloading natively. It's handled using default arguments or variable arguments.

# 12. `super()` Function
Used to call the constructor of the parent class.
```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
```

# 13. `Book` Class Example
```python
class Book:
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year

    def display(self):
        return f"{self.title} by {self.author}, published in {self.published_year}"
```

# 14. Constructors vs Regular Methods
- Constructors initialize objects.
- Regular methods define object behavior.

# 15. Role of `self` in Initialization
`self` allows instance-specific data initialization.

# 16. Preventing Multiple Instances (Singleton Pattern)
```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
```

# 17. `Student` Class with Subjects
```python
class Student:
    def __init__(self, subjects):
        self.subjects = subjects
```

# 18. `__del__` Method
Destructor that cleans up resources when an object is deleted.

# 19. Constructor Chaining
```python
class A:
    def __init__(self):
        print("Constructor of A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor of B")
```

# 20. `Car` Class Example
```python
class Car:
    def __init__(self, make="Toyota", model="Corolla"):
        self.make = make
        self.model = model

    def display(self):
        return f"Car Make: {self.make}, Model: {self.model}"
```

# INHERITANCE
# 1. Inheritance in Python
**Inheritance** allows a class (child) to acquire properties and methods from another class (parent). It promotes code reusability and logical hierarchy.

# 2. Single vs Multiple Inheritance
- **Single Inheritance:** Child inherits from one parent.
```python
class Parent:
    pass

class Child(Parent):
    pass
```
- **Multiple Inheritance:** Child inherits from multiple parents.
```python
class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass
```

# 3. `Vehicle` and `Car` Classes
```python
class Vehicle:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

class Car(Vehicle):
    def __init__(self, color, speed, brand):
        super().__init__(color, speed)
        self.brand = brand

car = Car("Red", 120, "Toyota")
```

# 4. Method Overriding
```python
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")
```

# 5. Accessing Parent Attributes
```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet_parent(self):
        super().greet()
```

# 6. `super()` Function
Used to call parent class methods.

# 7. `Animal`, `Dog`, and `Cat` Classes
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")
```

# 8. `isinstance()` Function
Checks if an object is an instance of a class.

# 9. `issubclass()` Function
Checks if a class is derived from another class.
```python
issubclass(Dog, Animal)  # True
```

# 10. Constructor Inheritance
Child class can inherit the constructor of the parent using `super()`.

# 11. `Shape`, `Circle`, and `Rectangle` Classes
```python
import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

# 12. Abstract Base Classes
```python
from abc import ABC, abstractmethod

class AbstractShape(ABC):
    @abstractmethod
    def area(self):
        pass
```

# 13. Prevent Modifications
Use double underscore `__` to make attributes private.

# 14. `Employee` and `Manager` Classes
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
```

# 15. Method Overloading vs Overriding
- **Overloading:** Same method name with different parameters (not native in Python).
- **Overriding:** Child class modifies parent method behavior.

# 16. `__init__()` in Inheritance
Initializes attributes in both parent and child classes.

# 17. `Bird`, `Eagle`, and `Sparrow` Classes
```python
class Bird:
    def fly(self):
        print("Bird is flying")

class Eagle(Bird):
    def fly(self):
        print("Eagle soars high")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flutters")
```

# 18. Diamond Problem
Occurs in multiple inheritance. Python resolves it using the Method Resolution Order (MRO).

# 19. "is-a" and "has-a" Relationships
- **is-a:** Inheritance relationship (e.g., `Car is-a Vehicle`).
- **has-a:** Composition relationship (e.g., `Car has-a Engine`).

# 20. University System Class Hierarchy
```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

class Professor(Person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department
```
# ENCAPSULATION
# 1. Encapsulation in Python
**Encapsulation** is the bundling of data with methods that operate on that data. It restricts direct access to some of an object's components, enhancing security and control.

# 2. Key Principles of Encapsulation
- **Access Control:** Defines how data can be accessed.
- **Data Hiding:** Prevents unintended interference by restricting access.

# 3. Achieving Encapsulation in Python
```python
class Example:
    def __init__(self):
        self.__hidden = 0  # Private attribute

    def get_hidden(self):
        return self.__hidden

    def set_hidden(self, value):
        self.__hidden = value
```

# 4. Access Modifiers
- **Public:** Accessible from anywhere (`name`).
- **Protected:** Intended for subclass use (`_name`).
- **Private:** Not directly accessible (`__name`).

# 5. `Person` Class with Private Attribute
```python
class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
```

# 6. Getter and Setter Methods
Control access and modification of private attributes.

# 7. Name Mangling
Python changes private attribute names to include the class name to avoid conflicts.

# 8. `BankAccount` Class
```python
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
```

# 9. Advantages of Encapsulation
- Improves code maintainability
- Enhances security
- Simplifies debugging

# 10. Accessing Private Attributes
```python
obj = Example()
print(obj._Example__hidden)  # Access via name mangling
```

# 11. School System Class Hierarchy
```python
class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

class Teacher:
    def __init__(self, name, subject):
        self.__name = name
        self.__subject = subject

class Course:
    def __init__(self, title):
        self.__title = title
```

# 12. Property Decorators
```python
class Example:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
```

# 13. Data Hiding
Protects data from unauthorized access.

# 14. `Employee` Class
```python
class Employee:
    def __init__(self, employee_id, salary):
        self.__employee_id = employee_id
        self.__salary = salary

    def calculate_bonus(self):
        return self.__salary * 0.1
```

# 15. Accessors and Mutators
Control attribute access, enforcing rules.

# 16. Drawbacks of Encapsulation
- Increased complexity
- Overhead from getter/setter methods

# 17. Library System Class
```python
class Book:
    def __init__(self, title, author, available=True):
        self.__title = title
        self.__author = author
        self.__available = available
```

# 18. Encapsulation and Code Reusability
Promotes modular, maintainable code.

# 19. Information Hiding
Essential for security and preventing misuse.

# 20. `Customer` Class
```python
class Customer:
    def __init__(self, name, address, contact):
        self.__name = name
        self.__address = address
        self.__contact = contact

    def get_details(self):
        return self.__name, self.__address, self.__contact
```

