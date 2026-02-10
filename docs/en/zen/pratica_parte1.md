# The Zen of Python - Practical Examples (Part 1)

> **Navigation:** [← Back to Home](../index.md) | [← Theory](teoria.md) | [Part 2 →](pratica_parte2.md) | [Optimization →](../otimizacao/guia_completo.md)

## Quick Index

**In this document (1-12):**

1. [Beautiful is better than ugly](#1-beautiful-is-better-than-ugly)
2. [Explicit is better than implicit](#2-explicit-is-better-than-implicit)
3. [Simple is better than complex](#3-simple-is-better-than-complex)
4. [Complex is better than complicated](#4-complex-is-better-than-complicated)
5. [Flat is better than nested](#5-flat-is-better-than-nested)
6. [Sparse is better than dense](#6-sparse-is-better-than-dense)
7. [Readability counts](#7-readability-counts)
8. [Special cases aren't special enough](#8-special-cases-arent-special-enough-to-break-the-rules)
9. [Although practicality beats purity](#9-although-practicality-beats-purity)
10. [Errors should never pass silently](#10-errors-should-never-pass-silently)
11. [Unless explicitly silenced](#11-unless-explicitly-silenced)
12. [In the face of ambiguity, refuse the temptation to guess](#12-in-the-face-of-ambiguity-refuse-the-temptation-to-guess)

**In Part 2:** [13-19 →](pratica_parte2.md)

---

## 1. Beautiful is better than ugly

### ❌ Ugly Code

```python
def calc(a,b,c):
    x=a+b
    if x>10:y=x*c
    else:y=x+c
    return y

# Bad names, inconsistent formatting, unclear logic
data=[1,2,3,4,5]
result=[]
for i in range(len(data)):
    if data[i]%2==0:result.append(data[i]*2)
```

### ✅ Beautiful Code

```python
def calculate_adjusted_total(base_amount, addition, multiplier):
    """
    Calculates the adjusted total based on the initial sum.

    If the sum of base_amount and addition exceeds 10,
    multiplies by multiplier, otherwise adds multiplier.
    """
    initial_sum = base_amount + addition

    if initial_sum > 10:
        adjusted_total = initial_sum * multiplier
    else:
        adjusted_total = initial_sum + multiplier

    return adjusted_total


# Clean code, well formatted, clear intentions
data = [1, 2, 3, 4, 5]
doubled_evens = [number * 2 for number in data if number % 2 == 0]
```

**Principles applied:**

- Descriptive names
- Consistent formatting (PEP 8)
- Proper spacing
- Clear structure

---

## 2. Explicit is better than implicit

### ❌ Implicit

```python
# Implicit type conversion (doesn't work in Python, but illustrates the concept)
def process_data(data):
    # Assumes data is a list, but it's not clear
    return sum(data)

# Using global variables implicitly
count = 0

def increment():
    global count  # At least this is explicit, but still problematic
    count += 1

# Wildcard import
from math import *
result = sqrt(16)  # Where does sqrt come from?
```

### ✅ Explicit

```python
# Clear types, explicit conversions
def process_data(data: list[int]) -> int:
    """Returns the sum of a list of integers."""
    if not isinstance(data, list):
        raise TypeError("data deve ser uma lista")
    return sum(data)

# Explicit state passed as argument
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self) -> int:
        return self.count

# Explicit import
import math
result = math.sqrt(16)  # Clearly from the math module

# Or specific import
from math import sqrt
result = sqrt(16)  # We know we imported sqrt
```

**More examples:**

```python
# ❌ Implicit: self is not passed implicitly in other languages
# Python forces explicitness
class Dog:
    def __init__(self, name):
        self.name = name  # explicit self

    def bark(self):
        print(f"{self.name} says woof!")  # explicit self

# ✅ Explicit arguments with default values
def create_user(name: str, age: int, active: bool = True):
    """
    Creates a user.
    active is explicitly True by default.
    """
    return {"name": name, "age": age, "active": active}

# ❌ Implicit modification
def add_item(list_items=[]):  # DANGER: mutable default
    list_items.append("item")
    return list_items

# ✅ Explicit about mutability
def add_item(list_items: list[str] | None = None) -> list[str]:
    """Adds item to list, creating a new list if None."""
    if list_items is None:
        list_items = []
    list_items.append("item")
    return list_items
```

---

## 3. Simple is better than complex

### ❌ Unnecessarily Complex

```python
# Over-engineering for a simple problem
class NumberProcessor:
    def __init__(self):
        self.operations = []

    def add_operation(self, op):
        self.operations.append(op)

    def process(self, number):
        result = number
        for operation in self.operations:
            result = operation(result)
        return result

processor = NumberProcessor()
processor.add_operation(lambda x: x * 2)
processor.add_operation(lambda x: x + 10)
result = processor.process(5)  # Result: 20

# Excessively abstract solution
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        raise ValueError("Unknown animal")

animal = AnimalFactory.create_animal("dog")
sound = animal.make_sound()
```

### ✅ Simple

```python
# Direct solution to the problem
def process_number(number):
    """Doubles the number and adds 10."""
    return (number * 2) + 10

result = process_number(5)  # Result: 20

# Direct solution without unnecessary abstractions
def get_dog_sound():
    return "Woof"

sound = get_dog_sound()

# Or if you really need structure:
ANIMAL_SOUNDS = {
    "dog": "Woof",
    "cat": "Meow",
    "cow": "Moo"
}

def get_animal_sound(animal_type):
    return ANIMAL_SOUNDS.get(animal_type, "Unknown sound")
```

**Example of simplicity with composition:**

```python
# ❌ Complex: deep inheritance
class Vehicle:
    def start(self): pass

class LandVehicle(Vehicle):
    def drive(self): pass

class Car(LandVehicle):
    def open_trunk(self): pass

class ElectricCar(Car):
    def charge(self): pass

# ✅ Simple: composition
class Engine:
    def start(self):
        return "Engine started"

    def stop(self):
        return "Engine stopped"

class Trunk:
    def open(self):
        return "Trunk opened"

class Battery:
    def charge(self):
        return "Charging battery"

class ElectricCar:
    def __init__(self):
        self.engine = Engine()
        self.trunk = Trunk()
        self.battery = Battery()

    def start(self):
        return self.engine.start()

    def charge(self):
        return self.battery.charge()
```

---

## 4. Complex is better than complicated

### ❌ Complicated (Confusing, Tangled)

```python
# Intertwined logic, hard to follow
def process_order(order):
    if order['status'] == 'pending':
        if order['payment']['method'] == 'credit_card':
            if order['payment']['verified']:
                if order['items']:
                    total = 0
                    for item in order['items']:
                        if item['stock'] > 0:
                            total += item['price']
                            item['stock'] -= 1
                        else:
                            return {'error': 'out_of_stock'}
                    if total > order['payment']['limit']:
                        return {'error': 'limit_exceeded'}
                    else:
                        order['status'] = 'processing'
                        return {'success': True, 'total': total}
                else:
                    return {'error': 'no_items'}
            else:
                return {'error': 'payment_not_verified'}
        else:
            return {'error': 'invalid_payment_method'}
    else:
        return {'error': 'invalid_status'}

# Function that does too many things
def handle_user_data(data, mode, options=None):
    if mode == 'create':
        # 50 lines of code
        pass
    elif mode == 'update':
        # 50 different lines
        pass
    elif mode == 'delete':
        # another 50 lines
        pass
    # ... continues
```

### ✅ Complex (Well Organized, Clear Structure)

```python
# Complexity organized into comprehensible modules
from dataclasses import dataclass
from typing import Optional

@dataclass
class OrderItem:
    name: str
    price: float
    stock: int

@dataclass
class Payment:
    method: str
    verified: bool
    limit: float

@dataclass
class Order:
    status: str
    payment: Payment
    items: list[OrderItem]

class OrderValidator:
    """Validates order business rules."""

    @staticmethod
    def validate_status(order: Order) -> Optional[str]:
        if order.status != 'pending':
            return 'invalid_status'
        return None

    @staticmethod
    def validate_payment(payment: Payment) -> Optional[str]:
        if payment.method != 'credit_card':
            return 'invalid_payment_method'
        if not payment.verified:
            return 'payment_not_verified'
        return None

    @staticmethod
    def validate_items(items: list[OrderItem]) -> Optional[str]:
        if not items:
            return 'no_items'
        for item in items:
            if item.stock <= 0:
                return 'out_of_stock'
        return None

class OrderCalculator:
    """Calculates order values."""

    @staticmethod
    def calculate_total(items: list[OrderItem]) -> float:
        return sum(item.price for item in items)

    @staticmethod
    def check_limit(total: float, limit: float) -> bool:
        return total <= limit

class OrderProcessor:
    """Processes orders by coordinating validation and calculation."""

    def __init__(self):
        self.validator = OrderValidator()
        self.calculator = OrderCalculator()

    def process_order(self, order: Order) -> dict:
        # Validation in clear steps
        if error := self.validator.validate_status(order):
            return {'error': error}

        if error := self.validator.validate_payment(order.payment):
            return {'error': error}

        if error := self.validator.validate_items(order.items):
            return {'error': error}

        # Calculation
        total = self.calculator.calculate_total(order.items)

        if not self.calculator.check_limit(total, order.payment.limit):
            return {'error': 'limit_exceeded'}

        # Processing
        self._update_stock(order.items)
        order.status = 'processing'

        return {'success': True, 'total': total}

    def _update_stock(self, items: list[OrderItem]):
        for item in items:
            item.stock -= 1

# Usage
processor = OrderProcessor()
result = processor.process_order(my_order)
```

**Key difference:**

- **Complicated**: Everything mixed together, hard to follow
- **Complex**: Multiple parts, each one clear, logical organization

---

## 5. Flat is better than nested

### ❌ Too Nested

```python
def process_data(data):
    result = []
    if data:
        if isinstance(data, list):
            if len(data) > 0:
                for item in data:
                    if item:
                        if isinstance(item, dict):
                            if 'value' in item:
                                if item['value'] > 0:
                                    if item['value'] < 100:
                                        result.append(item['value'] * 2)
    return result

# Deep inheritance
class A:
    pass

class B(A):
    pass

class C(B):
    pass

class D(C):
    pass

class E(D):
    pass  # 5 levels!
```

### ✅ Flat

```python
# Guard clauses - return early
def process_data(data):
    # Validations at the top
    if not data:
        return []

    if not isinstance(data, list):
        return []

    if len(data) == 0:
        return []

    # Main logic without deep nesting
    result = []
    for item in data:
        if should_process_item(item):
            result.append(process_item(item))

    return result

def should_process_item(item):
    """Checks if item should be processed."""
    if not item:
        return False
    if not isinstance(item, dict):
        return False
    if 'value' not in item:
        return False
    if not (0 < item['value'] < 100):
        return False
    return True

def process_item(item):
    """Processes a valid item."""
    return item['value'] * 2

# Composition instead of deep inheritance
class DataValidator:
    def validate(self, data):
        pass

class DataProcessor:
    def process(self, data):
        pass

class DataFormatter:
    def format(self, data):
        pass

class DataPipeline:
    """Composes functionalities horizontally."""
    def __init__(self):
        self.validator = DataValidator()
        self.processor = DataProcessor()
        self.formatter = DataFormatter()

    def run(self, data):
        validated = self.validator.validate(data)
        processed = self.processor.process(validated)
        formatted = self.formatter.format(processed)
        return formatted
```

**Flattening techniques:**

```python
# ❌ Nested
def find_user(users, user_id):
    for user in users:
        if user['id'] == user_id:
            if user['active']:
                if user['verified']:
                    return user
    return None

# ✅ Flat with comprehension
def find_user(users, user_id):
    active_verified_users = [
        user for user in users
        if user['id'] == user_id
        and user['active']
        and user['verified']
    ]
    return active_verified_users[0] if active_verified_users else None

# ✅ Flat with helper function
def is_valid_user(user, user_id):
    return (user['id'] == user_id and
            user['active'] and
            user['verified'])

def find_user(users, user_id):
    return next((user for user in users if is_valid_user(user, user_id)), None)
```

---

## 6. Sparse is better than dense

### ❌ Dense (Too Compact)

```python
# Everything crammed together, hard to read
def calc(x,y,z):return x*y+z if x>0 else y*z+x
data=[x**2 for x in range(10) if x%2==0 and x>2 and x<8]
result={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
user={'name':'John','age':30,'email':'john@example.com','active':True,'role':'admin'}

# Multiple operations on one line
x=10;y=20;z=x+y;print(z)

# Too-long comprehension
filtered_users=[u for u in users if u['age']>18 and u['active'] and u['verified'] and u['role']=='member' and u['subscription']=='premium']
```

### ✅ Sparse (Breathing Room)

```python
# Proper spacing, easy to read
def calculate_value(x, y, z):
    """Calculates value based on x, y, z."""
    if x > 0:
        return x * y + z
    else:
        return y * z + x

# Readable list comprehension
data = [
    x ** 2
    for x in range(10)
    if x % 2 == 0
    and x > 2
    and x < 8
]

# Dict with breathing room
result = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6
}

# Formatted user information
user = {
    'name': 'John',
    'age': 30,
    'email': 'john@example.com',
    'active': True,
    'role': 'admin'
}

# One operation per line
x = 10
y = 20
z = x + y
print(z)

# Comprehension broken into logical lines
def is_premium_member(user):
    """Checks if user is an active premium member."""
    return (
        user['age'] > 18
        and user['active']
        and user['verified']
        and user['role'] == 'member'
        and user['subscription'] == 'premium'
    )

filtered_users = [u for u in users if is_premium_member(u)]

# Or more explicit
filtered_users = [
    user
    for user in users
    if is_premium_member(user)
]
```

**Spacing in classes:**

```python
# ❌ Dense
class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):return f"Hello, {self.name}"
    def is_adult(self):return self.age>=18

# ✅ Sparse
class User:
    """Represents a system user."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        """Returns a personalized greeting."""
        return f"Hello, {self.name}"

    def is_adult(self) -> bool:
        """Checks if user is of legal age."""
        return self.age >= 18
```

---

## 7. Readability counts

### ❌ Poor Readability

```python
# Cryptic names
def f(x,y):
    return[i*2for i in x if i>y]

# Obscure logic
def calc(n):
    return n&1==0

# No context
data = [(1,2),(3,4),(5,6)]
result = [x+y for x,y in data]

# Single-letter variables
a = [1,2,3,4,5]
b = []
for i in a:
    if i % 2 == 0:
        b.append(i)
```

### ✅ High Readability

```python
# Descriptive names
def filter_and_double(numbers: list[int], threshold: int) -> list[int]:
    """
    Filters numbers above the threshold and doubles their values.

    Args:
        numbers: List of numbers to process
        threshold: Minimum value for inclusion

    Returns:
        List of doubled numbers that are above the threshold
    """
    return [number * 2 for number in numbers if number > threshold]

# Clear logic
def is_even(number: int) -> bool:
    """Checks if number is even."""
    return number % 2 == 0

# With context
coordinate_pairs = [(1, 2), (3, 4), (5, 6)]
coordinate_sums = [x + y for x, y in coordinate_pairs]

# Meaningful variables
numbers = [1, 2, 3, 4, 5]
even_numbers = []
for number in numbers:
    if is_even(number):
        even_numbers.append(number)

# Or more Pythonic
even_numbers = [number for number in numbers if is_even(number)]
```

**Readability in complex structures:**

```python
# ❌ Hard to read
def p(d):
    return sum([v for k,v in d.items() if k.startswith('p')])

# ✅ Easy to read
def calculate_premium_total(transactions: dict[str, float]) -> float:
    """
    Calculates the total of premium transactions.

    Considers only transactions whose keys start with 'p'.
    """
    premium_values = [
        value
        for key, value in transactions.items()
        if key.startswith('p')
    ]
    return sum(premium_values)

# Or even clearer
def calculate_premium_total(transactions: dict[str, float]) -> float:
    """Calculates the total of premium transactions."""
    total = 0
    for transaction_key, transaction_value in transactions.items():
        if is_premium_transaction(transaction_key):
            total += transaction_value
    return total

def is_premium_transaction(key: str) -> bool:
    """Checks if transaction is premium based on the key."""
    return key.startswith('p')
```

---

## 8. Special cases aren't special enough to break the rules

### ❌ Breaking Rules for Special Cases

```python
class Document:
    def save(self):
        """Saves document to the database."""
        database.save(self)

class SpecialDocument:
    def save(self):
        """Saves to file because it's special."""
        file.write(self)  # Breaks expectations!

# Inconsistency in API
def process_data(data):
    return [x * 2 for x in data]

def process_special_data(data):
    # Same function, but returns tuple instead of list
    return tuple(x * 2 for x in data)  # Inconsistent!

# Special treatment without justification
def calculate_discount(price, customer_type):
    if customer_type == "VIP":
        # Undocumented special rule
        return price * 0.5 if price > 1000 else price * 0.3
    return price * 0.1
```

### ✅ Consistency Maintained

```python
from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def save(self):
        """Saves document."""
        pass

class DatabaseDocument(Document):
    def save(self):
        """Saves document to the database."""
        database.save(self)

class FileDocument(Document):
    def save(self):
        """Saves document to a file."""
        file.write(self)

# Consistent interface
def process_data(data, output_type='list'):
    """
    Processes data returning the specified type.

    Args:
        data: Data to process
        output_type: 'list' or 'tuple'
    """
    processed = [x * 2 for x in data]
    if output_type == 'tuple':
        return tuple(processed)
    return processed

# Explicit and documented rules
DISCOUNT_RULES = {
    "VIP": {
        "high_value": 0.5,   # >1000
        "normal": 0.3
    },
    "REGULAR": {
        "high_value": 0.15,  # >1000
        "normal": 0.1
    }
}

def calculate_discount(price: float, customer_type: str) -> float:
    """
    Calculates discount based on price and customer type.

    Rules:
    - VIP: 50% for purchases >1000, 30% otherwise
    - REGULAR: 15% for purchases >1000, 10% otherwise
    """
    rules = DISCOUNT_RULES.get(customer_type, DISCOUNT_RULES["REGULAR"])

    if price > 1000:
        return price * rules["high_value"]
    return price * rules["normal"]
```

**Consistent protocol:**

```python
# All collections follow the same protocol
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {1: 'a', 2: 'b', 3: 'c'}

# All support:
len(my_list)      # Works
len(my_tuple)     # Works
len(my_set)       # Works
len(my_dict)      # Works

# All support:
2 in my_list      # Works
2 in my_tuple     # Works
2 in my_set       # Works
2 in my_dict      # Works (checks keys)

# All are iterable:
for item in my_list: pass
for item in my_tuple: pass
for item in my_set: pass
for item in my_dict: pass  # Iterates over keys
```

---

## 9. Although practicality beats purity

### Example: Purity vs Pragmatism

```python
# ❌ "Pure" but impractical
class ImmutableList:
    """Completely immutable list - pure but frustrating."""
    def __init__(self, items):
        self._items = tuple(items)  # Immutable

    def append(self, item):
        # Returns a NEW list - inefficient
        return ImmutableList(list(self._items) + [item])

    def __getitem__(self, index):
        return self._items[index]

# Impractical usage
lista = ImmutableList([1, 2, 3])
lista = lista.append(4)  # Must reassign every time
lista = lista.append(5)
lista = lista.append(6)

# ✅ Pragmatic - allows mutability when useful
class FlexibleList:
    """List that allows mutation when necessary."""
    def __init__(self, items):
        self._items = list(items)

    def append(self, item):
        self._items.append(item)  # Direct mutation - efficient

    def as_immutable(self):
        """Returns immutable version when needed."""
        return tuple(self._items)

# Pragmatic usage
lista = FlexibleList([1, 2, 3])
lista.append(4)
lista.append(5)
imutavel = lista.as_immutable()  # When you need a guarantee
```

**Another example: Type Hints (pragmatism)**

```python
# Python allows code without type hints (pragmatic)
def calcular_area(base, altura):
    return base * altura

# But allows adding them when useful
def calcular_area(base: float, altura: float) -> float:
    """Calculates the area of a rectangle."""
    return base * altura

# Does not force runtime checking (pragmatic)
# Uses external tools (mypy) when needed
```

**Pragmatism with the GIL:**

```python
# Python has the GIL (Global Interpreter Lock)
# Not "pure" for parallelism, but pragmatic:

# For CPU-bound tasks: use multiprocessing
from multiprocessing import Pool

def process_item(item):
    # Heavy computation
    return item ** 2

with Pool(4) as pool:
    results = pool.map(process_item, range(100))

# For I/O-bound tasks: threading works well despite the GIL
from threading import Thread
import requests

def fetch_url(url):
    response = requests.get(url)  # I/O not affected by the GIL
    return response.text

threads = [Thread(target=fetch_url, args=(url,)) for url in urls]
```

**Pragmatism in APIs:**

```python
# ✅ Pragmatic API - accepts multiple types
def process_input(data: str | list[str] | dict) -> list:
    """
    Processes input in multiple formats.
    Pragmatic - makes usage easier.
    """
    if isinstance(data, str):
        return [data]
    elif isinstance(data, list):
        return data
    elif isinstance(data, dict):
        return list(data.values())
    raise TypeError("Tipo não suportado")

# Convenient usage
process_input("hello")           # OK
process_input(["a", "b"])        # OK
process_input({"x": "a"})        # OK
```

---

## 10. Errors should never pass silently

### ❌ Silent Errors

```python
# Ignored error - NEVER do this
def read_config():
    try:
        with open('config.json') as f:
            return json.load(f)
    except:
        pass  # Error passes silently!
    return {}

# Returning None hides the error
def divide(a, b):
    if b == 0:
        return None  # Silent error
    return a / b

result = divide(10, 0)
print(result * 2)  # TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'

# Silent conversion can hide problems
def process_age(age_str):
    try:
        return int(age_str)
    except:
        return 0  # Is age 0 valid or an error?
```

### ✅ Explicit Errors

```python
# Explicit and informative error
def read_config():
    """Reads configuration from a JSON file."""
    try:
        with open('config.json') as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise ConfigurationError(
            "Arquivo config.json não encontrado"
        ) from e
    except json.JSONDecodeError as e:
        raise ConfigurationError(
            "Arquivo config.json contém JSON inválido"
        ) from e

# Specific exception
def divide(a: float, b: float) -> float:
    """
    Divides a by b.

    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b

# Or return a Result type for expected errors
from typing import Union

def divide_safe(a: float, b: float) -> Union[float, str]:
    """Divides returning result or error message."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Explicit validation
def process_age(age_str: str) -> int:
    """
    Converts an age string to an integer.

    Raises:
        ValueError: If age_str is not a valid number
        ValueError: If age is negative
    """
    try:
        age = int(age_str)
    except ValueError as e:
        raise ValueError(f"'{age_str}' não é uma idade válida") from e

    if age < 0:
        raise ValueError(f"Idade não pode ser negativa: {age}")

    return age
```

**Custom exceptions:**

```python
# Specific exception hierarchy
class ApplicationError(Exception):
    """Base application error."""
    pass

class ValidationError(ApplicationError):
    """Data validation error."""
    pass

class DatabaseError(ApplicationError):
    """Database operation error."""
    pass

class ConnectionError(DatabaseError):
    """Database connection error."""
    pass

# Usage
def save_user(user_data):
    if not user_data.get('email'):
        raise ValidationError("Email é obrigatório")

    try:
        db.connect()
    except Exception as e:
        raise ConnectionError("Falha ao conectar ao banco") from e

    try:
        db.save(user_data)
    except Exception as e:
        raise DatabaseError("Falha ao salvar usuário") from e
```

---

## 11. Unless explicitly silenced

### ❌ Accidental Suppression

```python
# Dangerous catch-all
try:
    result = complex_operation()
    process(result)
    save(result)
except:  # Catches EVERYTHING, including KeyboardInterrupt!
    pass

# Specific error handled incorrectly
try:
    data = fetch_data()
except Exception:
    data = None  # Hides the real problem
```

### ✅ Explicit and Justified Suppression

```python
import logging
from contextlib import suppress

logger = logging.getLogger(__name__)

# Explicit suppression with contextlib
def cleanup_temp_files():
    """Removes temporary files, ignoring if they don't exist."""
    temp_files = ['temp1.txt', 'temp2.txt', 'temp3.txt']

    for temp_file in temp_files:
        # We explicitly suppress FileNotFoundError
        # because it's not an error if the file was already deleted
        with suppress(FileNotFoundError):
            os.remove(temp_file)

# Explicit handling with logging
def load_optional_config():
    """Loads optional configuration."""
    try:
        with open('optional_config.json') as f:
            return json.load(f)
    except FileNotFoundError:
        # We explicitly decided that this error is OK
        logger.info("Optional configuration not found, using defaults")
        return DEFAULT_CONFIG
    except json.JSONDecodeError as e:
        # This error we do NOT suppress - it needs attention
        logger.error(f"Invalid configuration: {e}")
        raise

# Explicit fallback
def get_user_preference(user_id: str, preference: str) -> str:
    """
    Gets user preference with fallback to default.
    """
    try:
        return database.get_preference(user_id, preference)
    except PreferenceNotFoundError:
        # Explicit suppression - returns documented default
        logger.debug(
            f"Preference '{preference}' not found "
            f"for user {user_id}, using default"
        )
        return DEFAULT_PREFERENCES[preference]
    except DatabaseError:
        # This error we do NOT suppress
        logger.error(f"Error accessing database for user {user_id}")
        raise
```

**Retry pattern with suppression:**

```python
import time
from typing import Callable, TypeVar

T = TypeVar('T')

def retry_with_backoff(
    func: Callable[[], T],
    max_attempts: int = 3,
    backoff_seconds: float = 1.0
) -> T:
    """
    Attempts to execute function with retry and exponential backoff.

    Suppresses transient errors but re-raises after max_attempts.
    """
    last_exception = None

    for attempt in range(max_attempts):
        try:
            return func()
        except TransientError as e:
            # Explicit suppression of transient error
            last_exception = e
            if attempt < max_attempts - 1:
                wait_time = backoff_seconds * (2 ** attempt)
                logger.warning(
                    f"Attempt {attempt + 1} failed: {e}. "
                    f"Retrying in {wait_time}s"
                )
                time.sleep(wait_time)
            else:
                logger.error(
                    f"All {max_attempts} attempts failed"
                )

    # After all attempts, error is no longer suppressed
    raise last_exception
```

---

## 12. In the face of ambiguity, refuse the temptation to guess

### ❌ Guessing

```python
# Guesses type based on value
def process(value):
    # BAD: Tries to guess what to do
    if value < 10:
        return value * 2
    elif value < 100:
        return value * 3
    else:
        return str(value)  # Changes return type!

# Guesses date format
def parse_date(date_string):
    # Tries multiple formats - which one to use?
    formats = ['%Y-%m-%d', '%d/%m/%Y', '%m-%d-%Y']
    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    return None  # Silent failure!

# Inconsistent behavior
def get_value(data, key):
    # Sometimes returns value, sometimes list, sometimes None
    if key in data:
        value = data[key]
        if isinstance(value, list) and len(value) == 1:
            return value[0]  # Automatically "simplifies"
        return value
    return None
```

### ✅ Explicit, No Guessing

```python
# Explicit type and behavior
def double_number(value: int) -> int:
    """Doubles an integer number."""
    if not isinstance(value, int):
        raise TypeError(f"Esperado int, recebido {type(value)}")
    return value * 2

def triple_number(value: int) -> int:
    """Triples an integer number."""
    if not isinstance(value, int):
        raise TypeError(f"Esperado int, recebido {type(value)}")
    return value * 3

# Explicit date format
def parse_date_iso(date_string: str) -> datetime:
    """
    Parses a date in ISO format (YYYY-MM-DD).

    Raises:
        ValueError: If format is not valid ISO
    """
    try:
        return datetime.strptime(date_string, '%Y-%m-%d')
    except ValueError as e:
        raise ValueError(
            f"Date '{date_string}' is not in ISO format (YYYY-MM-DD)"
        ) from e

# Or allows specifying the format
def parse_date(date_string: str, format: str) -> datetime:
    """
    Parses a date in the specified format.

    Args:
        date_string: String containing the date
        format: strptime format (e.g.: '%Y-%m-%d')
    """
    try:
        return datetime.strptime(date_string, format)
    except ValueError as e:
        raise ValueError(
            f"Date '{date_string}' does not match format '{format}'"
        ) from e

# Consistent and explicit behavior
def get_value(data: dict, key: str) -> any:
    """
    Gets value for key, raising error if it doesn't exist.

    Raises:
        KeyError: If key doesn't exist
    """
    if key not in data:
        raise KeyError(f"Chave '{key}' não encontrada")
    return data[key]

def get_value_or_default(data: dict, key: str, default: any = None) -> any:
    """Gets value or returns default if key doesn't exist."""
    return data.get(key, default)

def get_values_list(data: dict, key: str) -> list:
    """
    Gets value as a list.

    If value is not a list, returns a list with a single element.
    """
    value = get_value(data, key)
    if isinstance(value, list):
        return value
    return [value]
```

**Explicit conversions:**

```python
# ❌ Implicit conversion/guessing
def add(a, b):
    # Tries to guess whether to add, concatenate, etc.
    try:
        return int(a) + int(b)
    except:
        return str(a) + str(b)

# ✅ Explicit type
def add_numbers(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b

def concatenate_strings(a: str, b: str) -> str:
    """Concatenates two strings."""
    return a + b

def add_flexible(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Adds numbers, preserving float type if present."""
    return a + b
```

---

---

> **Continues:** [Part 2 - Principles 13-19 →](pratica_parte2.md)
