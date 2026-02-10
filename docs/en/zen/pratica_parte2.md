# The Zen of Python - Practical Examples (Part 2)

> **Navigation:** [← Back to Home](../index.md) | [← Theory](teoria.md) | [← Part 1](pratica_parte1.md) | [Optimization →](../otimizacao/guia_completo.md)

## Quick Index

**In this document (13-19):**

13. [There should be one obvious way to do it](#13-there-should-be-one-and-preferably-only-one-obvious-way-to-do-it)
14. [Although that way may not be obvious at first](#14-although-that-way-may-not-be-obvious-at-first-unless-youre-dutch)
15. [Now is better than never](#15-now-is-better-than-never)
16. [Although never is often better than right now](#16-although-never-is-often-better-than-right-now)
17. [If the implementation is hard to explain](#17-if-the-implementation-is-hard-to-explain-its-a-bad-idea)
18. [If the implementation is easy to explain](#18-if-the-implementation-is-easy-to-explain-it-may-be-a-good-idea)
19. [Namespaces are one honking great idea](#19-namespaces-are-one-honking-great-idea-lets-do-more-of-those)

**In Part 1:** [← Principles 1-12](pratica_parte1.md)

---

## 13. There should be one-- and preferably only one --obvious way to do it

### Multiple Ways vs One Obvious Way

```python
# ===== ITERATING OVER A LIST =====

# ✅ Obvious way (Pythonic)
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)

# ❌ Possible, but not obvious
for i in range(len(fruits)):
    print(fruits[i])

# ❌ Possible, but not idiomatic
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# ===== CHECK IF LIST IS EMPTY =====

my_list = []

# ✅ Obvious way (Pythonic)
if not my_list:
    print("Empty list")

# ❌ Possible, but not idiomatic
if len(my_list) == 0:
    print("Empty list")

# ❌ Possible, but verbose
if my_list == []:
    print("Empty list")

# ===== READ FILE =====

# ✅ Obvious way (context manager)
with open('data.txt') as f:
    data = f.read()

# ❌ Possible, but forgets to close
f = open('data.txt')
data = f.read()
f.close()

# ❌ Possible, but complex
try:
    f = open('data.txt')
    data = f.read()
finally:
    f.close()

# ===== CREATE COUNTING DICTIONARY =====

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# ✅ Obvious way (Counter)
from collections import Counter
word_count = Counter(words)

# ❌ Possible, but more code
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# ❌ Possible, but less clear
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# ===== SWAP VARIABLE VALUES =====

a, b = 10, 20

# ✅ Obvious way (tuple unpacking)
a, b = b, a

# ❌ Possible, but more code
temp = a
a = b
b = temp

# ===== COMBINE TWO LISTS =====

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# ✅ Obvious way to combine
combined = list1 + list2

# ✅ Obvious way to iterate simultaneously
for item1, item2 in zip(list1, list2):
    print(item1, item2)

# ❌ Possible, but not idiomatic
for i in range(len(list1)):
    print(list1[i], list2[i])

# ===== STRING FORMATTING =====

name = "Alice"
age = 30

# ✅ Obvious way (f-strings, Python 3.6+)
message = f"My name is {name} and I am {age} years old"

# ❌ Possible, but outdated
message = "My name is %s and I am %d years old" % (name, age)

# ❌ Possible, but verbose
message = "My name is {} and I am {} years old".format(name, age)

# ===== CHECK MULTIPLE VALUES =====

value = 5

# ✅ Obvious way
if value in {1, 2, 3, 4, 5}:
    print("Found")

# ❌ Possible, but repetitive
if value == 1 or value == 2 or value == 3 or value == 4 or value == 5:
    print("Found")
```

**Cases where there are multiple legitimate ways:**

```python
# List comprehension vs map/filter
# Both are acceptable, but comprehension is generally preferred

numbers = [1, 2, 3, 4, 5]

# ✅ Preferred (more Pythonic)
doubled = [n * 2 for n in numbers]
evens = [n for n in numbers if n % 2 == 0]

# ✅ Acceptable (functional)
doubled = list(map(lambda n: n * 2, numbers))
evens = list(filter(lambda n: n % 2 == 0, numbers))

# Choice depends on context:
# - Comprehension: generally more readable
# - map/filter: useful with already existing functions

def double(n):
    return n * 2

doubled = list(map(double, numbers))  # OK when function already exists
```

---

## 14. Although that way may not be obvious at first unless you're Dutch

### Pythonic Idioms You Learn Over Time

```python
# ===== ENUMERATE =====

# ❌ Not obvious for beginners
items = ['a', 'b', 'c']
for i in range(len(items)):
    print(f"Index {i}: {items[i]}")

# ✅ Pythonic (you learn it)
for index, item in enumerate(items):
    print(f"Index {index}: {item}")

# Enumerate with custom start
for index, item in enumerate(items, start=1):
    print(f"Item {index}: {item}")

# ===== ZIP =====

# ❌ Beginner way
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old")

# ✅ Pythonic
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# ✅ Zip with multiple lists
cities = ['NYC', 'LA', 'Chicago']
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, lives in {city}")

# ===== DICT COMPREHENSION =====

# ❌ Beginner way
pairs = [('a', 1), ('b', 2), ('c', 3)]
result = {}
for key, value in pairs:
    result[key] = value

# ✅ Pythonic
result = {key: value for key, value in pairs}

# ✅ Transformation
numbers = [1, 2, 3, 4, 5]
squares = {n: n**2 for n in numbers}

# ===== ANY and ALL =====

# ❌ Beginner way
numbers = [1, 3, 5, 7, 8]
has_even = False
for n in numbers:
    if n % 2 == 0:
        has_even = True
        break

# ✅ Pythonic
has_even = any(n % 2 == 0 for n in numbers)

# ❌ Beginner way
all_positive = True
for n in numbers:
    if n <= 0:
        all_positive = False
        break

# ✅ Pythonic
all_positive = all(n > 0 for n in numbers)

# ===== UNPACKING =====

# ❌ Beginner way
point = (10, 20)
x = point[0]
y = point[1]

# ✅ Pythonic
x, y = point

# ✅ Extended unpacking
first, *middle, last = [1, 2, 3, 4, 5]
# first = 1, middle = [2, 3, 4], last = 5

# ✅ Swapping
a, b = b, a

# ===== DICT.GET WITH DEFAULT =====

# ❌ Beginner way
config = {'debug': True}
if 'timeout' in config:
    timeout = config['timeout']
else:
    timeout = 30

# ✅ Pythonic
timeout = config.get('timeout', 30)

# ===== SETDEFAULT =====

# ❌ Beginner way
word_positions = {}
words = ['a', 'b', 'a', 'c', 'b']

for i, word in enumerate(words):
    if word not in word_positions:
        word_positions[word] = []
    word_positions[word].append(i)

# ✅ Pythonic
word_positions = {}
for i, word in enumerate(words):
    word_positions.setdefault(word, []).append(i)

# ✅ Or use defaultdict
from collections import defaultdict
word_positions = defaultdict(list)
for i, word in enumerate(words):
    word_positions[word].append(i)

# ===== TERNARY =====

# ❌ Beginner way
age = 25
if age >= 18:
    status = "adult"
else:
    status = "minor"

# ✅ Pythonic
status = "adult" if age >= 18 else "minor"

# ===== CHAINED COMPARISONS =====

# ❌ Beginner way
x = 5
if x > 0 and x < 10:
    print("In range")

# ✅ Pythonic
if 0 < x < 10:
    print("In range")

# ===== REVERSED AND SORTED =====

# ❌ Beginner way
items = [1, 2, 3, 4, 5]
reversed_items = []
for i in range(len(items)-1, -1, -1):
    reversed_items.append(items[i])

# ✅ Pythonic
reversed_items = list(reversed(items))

# ❌ Beginner way to sort
sorted_items = items.copy()
sorted_items.sort()

# ✅ Pythonic (does not modify original)
sorted_items = sorted(items)

# ===== WALRUS OPERATOR (Python 3.8+) =====

# ❌ Double evaluation
data = fetch_data()
if len(data) > 10:
    print(f"Processing {len(data)} items")

# ✅ Pythonic with walrus
if (n := len(data)) > 10:
    print(f"Processing {n} items")

# Useful in list comprehensions
# ❌ Calculates twice
results = [expensive_func(x) for x in data if expensive_func(x) > 0]

# ✅ Calculates once
results = [y for x in data if (y := expensive_func(x)) > 0]
```

---

## 15. Now is better than never

### Examples of Action vs Procrastination

```python
# ===== REFACTORING =====

# ❌ Leaving for later (technique: leave a TODO comment)
def process_order(order):
    # TODO: Refactor this, it's confusing
    # TODO: Extract validation
    # TODO: Add logging
    if order['status'] == 'pending' and order['verified']:
        # 50 lines of confusing code
        pass

# ✅ Refactor now (when you see the problem)
def process_order(order: Order) -> OrderResult:
    """Processes a pending order."""
    validate_order(order)
    log_order_processing(order)
    return execute_order(order)

# ===== DOCUMENTATION =====

# ❌ Code without documentation ("I'll document later")
def calc(x, y, z):
    return x * y + z if x > 0 else y * z + x

# ✅ Document as you write
def calculate_value(x: float, y: float, z: float) -> float:
    """
    Calculates value based on x, y, and z.

    If x is positive: x * y + z
    Otherwise: y * z + x

    Args:
        x: First value
        y: Second value
        z: Third value

    Returns:
        Calculated value
    """
    if x > 0:
        return x * y + z
    return y * z + x

# ===== TESTS =====

# ❌ "I'll write tests later"
def divide(a, b):
    return a / b
# (No tests, division by zero bug not detected)

# ✅ Write tests now (TDD)
def divide(a: float, b: float) -> float:
    """Divides a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Test
import pytest

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    with pytest.raises(ValueError):
        divide(10, 0)

# ===== ERROR HANDLING =====

# ❌ "I'll add error handling later"
def load_config():
    with open('config.json') as f:
        return json.load(f)
# (Can crash in production)

# ✅ Add error handling now
def load_config() -> dict:
    """Loads configuration from JSON file."""
    try:
        with open('config.json') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning("Config file not found, using defaults")
        return DEFAULT_CONFIG
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in config: {e}")
        raise ConfigurationError("Invalid configuration file") from e

# ===== DUPLICATED CODE =====

# ❌ Duplication ("I'll extract later")
def process_user_data(data):
    if not data.get('name'):
        raise ValueError("Name required")
    if not data.get('email'):
        raise ValueError("Email required")
    if not data.get('age'):
        raise ValueError("Age required")
    # ... more code

def process_admin_data(data):
    if not data.get('name'):
        raise ValueError("Name required")
    if not data.get('email'):
        raise ValueError("Email required")
    if not data.get('age'):
        raise ValueError("Age required")
    # ... different code

# ✅ Extract now (DRY - Don't Repeat Yourself)
def validate_required_fields(data: dict, fields: list[str]):
    """Validates that required fields are present."""
    for field in fields:
        if not data.get(field):
            raise ValueError(f"{field.title()} is required")

def process_user_data(data: dict):
    validate_required_fields(data, ['name', 'email', 'age'])
    # ... more code

def process_admin_data(data: dict):
    validate_required_fields(data, ['name', 'email', 'age'])
    # ... different code
```

**Principle: The Boy Scout Rule**

```python
# "Leave the code better than you found it"

# Found this:
def get_user(id):
    return db.query("SELECT * FROM users WHERE id="+str(id))

# Improved (SQL injection fix, naming, type hints):
def get_user(user_id: int) -> Optional[User]:
    """Fetches user by ID."""
    query = "SELECT * FROM users WHERE id = ?"
    result = db.query(query, (user_id,))
    return User.from_db(result) if result else None
```

---

## 16. Although never is often better than *right* now

### Examples of When NOT to Do It (Yet)

```python
# ===== YAGNI (You Aren't Gonna Need It) =====

# ❌ Over-engineering "just in case"
class User:
    def __init__(self, name):
        self.name = name
        self.email = None  # "We'll need this"
        self.phone = None  # "Might need it"
        self.address = None  # "Just in case"
        self.backup_email = None  # "Could be useful"
        self.preferences = {}  # "Eventually"
        self.metadata = {}  # "For extensibility"

# ✅ Add only what you need NOW
class User:
    def __init__(self, name: str):
        self.name = name

# Add other fields when you ACTUALLY need them

# ===== PREMATURE OPTIMIZATION =====

# ❌ Optimization before measuring
def process_items(items):
    # Using complex cache "for performance"
    cache = {}
    results = []
    for item in items:
        key = hash(item)
        if key in cache:
            results.append(cache[key])
        else:
            result = expensive_operation(item)
            cache[key] = result
            results.append(result)
    return results

# ✅ Start simple, optimize if necessary
def process_items(items):
    """Processes items."""
    return [expensive_operation(item) for item in items]

# If profiling shows it's a bottleneck, then optimize:
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_operation(item):
    # ... expensive operation
    pass

# ===== PREMATURE ABSTRACTION =====

# ❌ Abstraction without clear need
class DataProcessorFactory:
    @staticmethod
    def create_processor(processor_type):
        if processor_type == "simple":
            return SimpleDataProcessor()
        elif processor_type == "complex":
            return ComplexDataProcessor()
        raise ValueError("Unknown processor")

class DataProcessorInterface(ABC):
    @abstractmethod
    def process(self, data):
        pass

class SimpleDataProcessor(DataProcessorInterface):
    def process(self, data):
        return [x * 2 for x in data]

# ✅ Start concrete
def process_data(data):
    """Doubles values in data."""
    return [x * 2 for x in data]

# Add abstraction when you have MULTIPLE real implementations

# ===== SPECULATIVE FEATURES =====

# ❌ Implementing features "they might ask for"
class Report:
    def generate(self):
        # Generates basic report
        pass

    def export_to_pdf(self):
        # "Maybe they'll want PDF"
        pass

    def export_to_excel(self):
        # "Or Excel"
        pass

    def export_to_csv(self):
        # "CSV too"
        pass

    def send_by_email(self):
        # "Could be useful"
        pass

    def schedule_generation(self):
        # "Maybe in the future"
        pass

# ✅ Implement only what was requested
class Report:
    def generate(self):
        """Generates report."""
        # Implements only what was asked for
        pass

# Add export/email/schedule when they ACTUALLY ask for it

# ===== CODE UNDER PRESSURE =====

# Situation: Critical bug in production, pressure to fix it "NOW"

# ❌ Quick and dirty fix
def process_payment(amount):
    # Quick fix: skips validation to "resolve quickly"
    # TODO: Add validation later
    charge_card(amount)
    return True

# ✅ Better to wait and do it right (or make a temporary quick fix + task to fix properly)
def process_payment(amount: float) -> bool:
    """Processes payment with validation."""
    validate_amount(amount)

    try:
        charge_card(amount)
        return True
    except PaymentError as e:
        logger.error(f"Payment failed: {e}")
        raise

# If you REALLY need an emergency fix:
def process_payment_emergency(amount):
    """
    TEMPORARY: Emergency fix for production issue.

    TODO: Replace with proper implementation (TICKET-123)
    REMOVE BY: 2025-03-01
    """
    # Quick fix here, but documented and scheduled for removal
    pass

# ===== FRAMEWORKS AND LIBRARIES =====

# ❌ Adding a library at the first doubt
# Problem: Need to format a date
import arrow  # Full library just to format a date
import pendulum  # Another library
from datetime import datetime

# ✅ Use stdlib first
from datetime import datetime

def format_date(date: datetime) -> str:
    """Formats date in Brazilian standard."""
    return date.strftime('%d/%m/%Y')

# Add an external library only if stdlib is insufficient
```

**Decision: Now vs Never vs Later**

```python
# Framework for deciding:

def should_implement_now(feature):
    """
    Criteria to implement now:
    - [ ] It was requested/required
    - [ ] There is a clear use case
    - [ ] Implementation cost is low
    - [ ] Risk of not having it is high
    """
    pass

def should_never_implement(feature):
    """
    Never implement if:
    - [ ] Speculative without evidence
    - [ ] Complexity > Benefit
    - [ ] A simpler solution exists
    - [ ] Violates YAGNI
    """
    pass

def should_implement_later(feature):
    """
    Implement later if:
    - [ ] Needs more research
    - [ ] Requires careful design
    - [ ] Unresolved dependencies
    - [ ] Can learn more by waiting
    """
    pass
```

---

## 17. If the implementation is hard to explain, it's a bad idea

### Examples of Hard vs Easy to Explain

```python
# ===== CONFUSING ALGORITHM =====

# ❌ Hard to explain
def mystery_func(lst):
    return [i for i, x in enumerate(lst) if x == lst[i::-1][0]]

# Try to explain: "Returns indices where... hmm... when the element equals...
# the first element of the reversed sublist starting from that index?"

# ✅ Easy to explain
def find_palindrome_centers(text: str) -> list[int]:
    """
    Finds indices that are centers of palindromes.

    Returns list of indices where the character equals the character
    at the same position counting from the beginning of the string.
    """
    centers = []
    for index, char in enumerate(text):
        if char == text[-(index + 1)]:
            centers.append(index)
    return centers

# ===== COMPLEX LOGIC =====

# ❌ Hard to explain
def calc(a, b, c=None, d=None, mode='x'):
    if mode == 'x':
        return (a * b) + (c or 0) - (d or 0)
    elif mode == 'y':
        return (a + b) * (c or 1) / (d or 1)
    else:
        return ((a if c else b) * (d if d else c if c else 1))

# ✅ Easy to explain
def calculate_total(base: float, multiplier: float,
                   addition: float = 0, subtraction: float = 0) -> float:
    """
    Calculates: (base * multiplier) + addition - subtraction

    Args:
        base: Base value
        multiplier: Multiplier
        addition: Value to add (default 0)
        subtraction: Value to subtract (default 0)

    Returns:
        Calculation result
    """
    return (base * multiplier) + addition - subtraction

def calculate_ratio(numerator: float, denominator: float,
                   numerator_factor: float = 1,
                   denominator_factor: float = 1) -> float:
    """
    Calculates: (numerator + denominator) * numerator_factor / denominator_factor
    """
    return (numerator + denominator) * numerator_factor / denominator_factor

# ===== CONFUSING DATA STRUCTURE =====

# ❌ Hard to explain
data = {
    'u': {
        'n': 'John',
        'a': 30,
        'p': {
            'c': 'NYC',
            's': 'NY'
        }
    }
}

# ✅ Easy to explain
from dataclasses import dataclass

@dataclass
class Address:
    """User address."""
    city: str
    state: str

@dataclass
class User:
    """User information."""
    name: str
    age: int
    address: Address

user = User(
    name='John',
    age=30,
    address=Address(city='NYC', state='NY')
)

# ===== FUNCTION WITH HIDDEN SIDE EFFECTS =====

# ❌ Hard to explain the full behavior
global_counter = 0
cache = {}

def process_data(data):
    global global_counter
    global_counter += 1

    if data in cache:
        return cache[data] * global_counter

    result = expensive_operation(data)
    cache[data] = result

    if global_counter > 100:
        cache.clear()
        global_counter = 0

    return result * global_counter

# Try to explain: "Processes data, but also increments a global counter,
# uses cache, but clears cache every 100 calls, and multiplies result
# by the counter..."

# ✅ Easy to explain
class DataProcessor:
    """Processes data with cache and counting."""

    def __init__(self, cache_limit: int = 100):
        self.call_count = 0
        self.cache = {}
        self.cache_limit = cache_limit

    def process(self, data):
        """
        Processes data, using cache when possible.

        Cache is automatically cleared after cache_limit calls.
        """
        self.call_count += 1

        if self.call_count > self.cache_limit:
            self.clear_cache()

        if data not in self.cache:
            self.cache[data] = expensive_operation(data)

        return self.cache[data] * self.call_count

    def clear_cache(self):
        """Clears cache and resets counter."""
        self.cache.clear()
        self.call_count = 0
```

**The explanation test:**

```python
# If you can't explain it in 2-3 simple sentences, reconsider the design

# ❌ Hard
def complex_function(x, y, z, mode=None, *args, **kwargs):
    # Tries to do too many things
    # Behavior changes based on kwargs
    # Hidden side effects
    pass

# ✅ Easy
def calculate_average(numbers: list[float]) -> float:
    """Calculates the average of a list of numbers."""
    return sum(numbers) / len(numbers)
```

---

## 18. If the implementation is easy to explain, it may be a good idea

### "May be" - Ease of Explanation Does Not Guarantee Quality

```python
# ===== EASY TO EXPLAIN, BUT BAD =====

# ❌ Easy to explain: "Just ignores the error"
def divide(a, b):
    try:
        return a / b
    except:
        pass  # Ignores error - simple!
# Problem: Hides bugs

# ❌ Easy to explain: "Uses a global variable"
total = 0

def add_to_total(value):
    global total
    total += value  # Adds to global total
# Problem: Global state, hard to test

# ❌ Easy to explain: "Copies and pastes the code"
def process_users():
    users = get_users()
    for user in users:
        validate_email(user.email)
        save_to_db(user)
        send_notification(user)

def process_admins():
    admins = get_admins()
    for admin in admins:
        validate_email(admin.email)
        save_to_db(admin)
        send_notification(admin)
# Problem: Duplication

# ===== EASY TO EXPLAIN AND GOOD =====

# ✅ Easy to explain: "Doubles each number"
def double_numbers(numbers: list[int]) -> list[int]:
    """Doubles each number in the list."""
    return [n * 2 for n in numbers]

# ✅ Easy to explain: "Fetches user by ID"
def get_user_by_id(user_id: int) -> Optional[User]:
    """
    Fetches user from the database by ID.

    Returns None if user is not found.
    """
    return db.query(User).filter(User.id == user_id).first()

# ✅ Easy to explain: "Validates email"
import re

def is_valid_email(email: str) -> bool:
    """Checks if email has a valid format."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# ===== CHECKLIST BEYOND EXPLAINABILITY =====

def evaluate_solution(solution):
    """
    Checklist for evaluating a solution beyond being easy to explain:

    ✓ Easy to explain
    ✓ Solves the problem correctly
    ✓ Secure (no vulnerabilities)
    ✓ Efficient (acceptable performance)
    ✓ Maintainable
    ✓ Testable
    ✓ No unexpected side effects
    ✓ Follows SOLID principles
    """
    pass

# Example: Solution that passes all criteria

class UserService:
    """Service for user operations."""

    def __init__(self, db_session, email_service):
        self.db = db_session
        self.email = email_service

    def create_user(self, name: str, email: str) -> User:
        """
        Creates a new user.

        1. Validates email
        2. Checks if email already exists
        3. Creates user in the database
        4. Sends welcome email

        Raises:
            ValueError: If email is invalid
            UserExistsError: If email is already registered
        """
        # Easy to explain: validates
        if not self._is_valid_email(email):
            raise ValueError(f"Invalid email: {email}")

        # Easy to explain: checks for duplicate
        if self._email_exists(email):
            raise UserExistsError(f"Email already registered: {email}")

        # Easy to explain: creates user
        user = User(name=name, email=email)
        self.db.add(user)
        self.db.commit()

        # Easy to explain: sends welcome
        self.email.send_welcome(user)

        return user

    def _is_valid_email(self, email: str) -> bool:
        """Validates email format."""
        return '@' in email and '.' in email

    def _email_exists(self, email: str) -> bool:
        """Checks if email is already registered."""
        return self.db.query(User).filter(User.email == email).exists()
```

---

## 19. Namespaces are one honking great idea -- let's do more of those!

### Effective Use of Namespaces

```python
# ===== MODULES AS NAMESPACES =====

# ❌ Pollutes global namespace
from math import *
from statistics import *

result1 = sqrt(16)  # Where does it come from?
result2 = mean([1, 2, 3])  # Where does it come from?

# ✅ Explicit namespace
import math
import statistics

result1 = math.sqrt(16)  # Clearly from the math module
result2 = statistics.mean([1, 2, 3])  # Clearly from statistics

# ✅ Specific import when there is no conflict
from math import sqrt, pi
from statistics import mean, median

# ===== PACKAGES FOR ORGANIZATION =====

# Project structure with clear namespaces
"""
myproject/
    __init__.py
    models/
        __init__.py
        user.py
        product.py
    services/
        __init__.py
        user_service.py
        payment_service.py
    utils/
        __init__.py
        validators.py
        formatters.py
"""

# Usage with clear namespaces
from myproject.models.user import User
from myproject.models.product import Product
from myproject.services.user_service import UserService
from myproject.utils.validators import validate_email

# ===== CLASSES AS NAMESPACES =====

# ❌ Related global functions
def validate_user_email(email):
    pass

def validate_user_age(age):
    pass

def validate_user_password(password):
    pass

def format_user_name(name):
    pass

# ✅ Grouped in a class/namespace
class UserValidator:
    """Namespace for user validations."""

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validates user email."""
        return '@' in email

    @staticmethod
    def validate_age(age: int) -> bool:
        """Validates user age."""
        return 0 < age < 150

    @staticmethod
    def validate_password(password: str) -> bool:
        """Validates user password."""
        return len(password) >= 8

class UserFormatter:
    """Namespace for user formatting."""

    @staticmethod
    def format_name(name: str) -> str:
        """Formats user name."""
        return name.title()

    @staticmethod
    def format_phone(phone: str) -> str:
        """Formats user phone number."""
        return f"({phone[:2]}) {phone[2:7]}-{phone[7:]}"

# Usage
if UserValidator.validate_email(email):
    formatted_name = UserFormatter.format_name(name)

# ===== ENUM AS NAMESPACE =====

# ❌ Global constants
USER_STATUS_ACTIVE = 'active'
USER_STATUS_INACTIVE = 'inactive'
USER_STATUS_SUSPENDED = 'suspended'

ORDER_STATUS_PENDING = 'pending'
ORDER_STATUS_PROCESSING = 'processing'

# ✅ Enum namespace
from enum import Enum

class UserStatus(Enum):
    """Possible user statuses."""
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    SUSPENDED = 'suspended'

class OrderStatus(Enum):
    """Possible order statuses."""
    PENDING = 'pending'
    PROCESSING = 'processing'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

# Clear usage
user.status = UserStatus.ACTIVE
order.status = OrderStatus.PENDING

# ===== DATACLASS/NAMEDTUPLE AS NAMESPACE =====

# ❌ Dict with magic strings
config = {
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'mydb'
}

host = config['db_host']  # Prone to typos

# ✅ Dataclass namespace
from dataclasses import dataclass

@dataclass
class DatabaseConfig:
    """Database configuration."""
    host: str
    port: int
    name: str
    user: str
    password: str

config = DatabaseConfig(
    host='localhost',
    port=5432,
    name='mydb',
    user='admin',
    password='secret'
)

# Access with autocomplete and type checking
host = config.host

# ===== NAMESPACE CONTEXT =====

# ❌ Global variable accessible from anywhere
current_user = None

def process_order():
    global current_user
    # Uses current_user
    pass

# ✅ Context namespace (threading.local or contextvars)
from contextvars import ContextVar

current_user: ContextVar[User] = ContextVar('current_user')

def process_order():
    user = current_user.get()
    # Uses user from context, not global

# ===== NAMESPACE HIERARCHY =====

# Python uses LEGB for name resolution:
# Local -> Enclosing -> Global -> Built-in

x = "global"  # Global namespace

def outer():
    x = "enclosing"  # Enclosing namespace

    def inner():
        x = "local"  # Local namespace
        print(x)  # Prints "local"

    inner()
    print(x)  # Prints "enclosing"

outer()
print(x)  # Prints "global"

# Built-in
len([1, 2, 3])  # len comes from the built-in namespace

# ===== BEST PRACTICES WITH NAMESPACES =====

# ✅ Use specific imports for clarity
from collections import Counter, defaultdict
from typing import List, Dict, Optional

# ✅ Group imports by type
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from myproject.models import User
from myproject.services import UserService

# ✅ Use aliases when names conflict
from myproject.models import User as UserModel
from external_lib import User as ExternalUser

# ✅ Use __all__ to control module namespace
# mymodule.py
__all__ = ['public_function', 'PublicClass']

def public_function():
    pass

def _private_function():
    pass

class PublicClass:
    pass

# ✅ Use _ to indicate private names
class MyClass:
    def __init__(self):
        self.public_attr = "public"
        self._private_attr = "private (convention)"
        self.__very_private = "private (name mangling)"

    def public_method(self):
        pass

    def _private_method(self):
        pass

# ===== ANTI-PATTERNS WITH NAMESPACES =====

# ❌ from module import *
from os import *  # Pollutes namespace with dozens of names

# ❌ Too generic names in global scope
data = []  # Too generic name
result = None
temp = ""

# ✅ Descriptive names
user_data = []
calculation_result = None
temp_file_path = ""

# ❌ Modifying another module's namespace
import math
math.sqrt = lambda x: x ** 0.5  # DO NOT do this!

# ✅ Create your own function
def my_sqrt(x):
    return x ** 0.5
```

**Benefits of Namespaces:**

```python
# 1. AVOIDS CONFLICTS
# Without namespace
def process():  # Which process?
    pass

# With namespace
class UserProcessor:
    def process(self):  # Clearly processes user
        pass

class OrderProcessor:
    def process(self):  # Clearly processes order
        pass

# 2. ORGANIZATION
# Related functions grouped together
class StringUtils:
    @staticmethod
    def reverse(s): ...

    @staticmethod
    def capitalize_words(s): ...

    @staticmethod
    def remove_special_chars(s): ...

# 3. EXPLICITNESS
import requests
response = requests.get(url)  # Clearly from requests

# 4. MODULARIZATION
from myapp.auth import authenticate
from myapp.db import save_to_database
from myapp.email import send_email
# Each module is a clear namespace
```

---

## Practical Conclusion

The Zen of Python is not a set of absolute rules, but rather **guiding principles**. Effective Python programming practice comes from:

1. **Knowing the principles** (this document)
2. **Practicing application** (writing code)
3. **Receiving feedback** (code reviews)
4. **Studying Pythonic code** (open source projects)
5. **Reflecting on trade-offs** (technical discussions)

Over time, these principles become **natural intuition**, and you will write Pythonic code without consciously thinking about each principle.

**Remember**: Python is about **readability**, **simplicity**, and **practicality**. When in doubt, choose the solution that a colleague would understand most easily.

---

## Next Steps

- [← Back to Part 1 (Principles 1-12)](pratica_parte1.md)
- [← Dive Deeper into Theory](teoria.md)
- [→ Apply to Code Optimization](../otimizacao/guia_completo.md)
- [→ Quick Optimization Reference](../otimizacao/referencia_rapida.md)
- [→ Run Practical Examples](https://github.com/DougFelipe/zen-python/blob/main/src/zen_python_exemplos.py)
