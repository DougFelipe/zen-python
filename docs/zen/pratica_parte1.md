# O Zen of Python - Exemplos Práticos (Parte 1)

> **Navegação:** [← Voltar ao Início](../index.md) | [← Teoria](teoria.md) | [Parte 2 →](pratica_parte2.md) | [Otimização →](../otimizacao/guia_completo.md)

## Índice Rápido

**Neste documento (1-12):**

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

**Na Parte 2:** [13-19 →](pratica_parte2.md)

---

## 1. Beautiful is better than ugly

### ❌ Código Feio

```python
def calc(a,b,c):
    x=a+b
    if x>10:y=x*c
    else:y=x+c
    return y

# Nomes ruins, formatação inconsistente, lógica pouco clara
data=[1,2,3,4,5]
result=[]
for i in range(len(data)):
    if data[i]%2==0:result.append(data[i]*2)
```

### ✅ Código Bonito

```python
def calculate_adjusted_total(base_amount, addition, multiplier):
    """
    Calcula o total ajustado baseado na soma inicial.
    
    Se a soma de base_amount e addition excede 10,
    multiplica pelo multiplier, caso contrário adiciona multiplier.
    """
    initial_sum = base_amount + addition
    
    if initial_sum > 10:
        adjusted_total = initial_sum * multiplier
    else:
        adjusted_total = initial_sum + multiplier
    
    return adjusted_total


# Código limpo, bem formatado, intenções claras
data = [1, 2, 3, 4, 5]
doubled_evens = [number * 2 for number in data if number % 2 == 0]
```

**Princípios aplicados:**

- Nomes descritivos
- Formatação consistente (PEP 8)
- Espaçamento adequado
- Estrutura clara

---

## 2. Explicit is better than implicit

### ❌ Implícito

```python
# Conversão implícita de tipo (não funciona em Python, mas exemplo do conceito)
def process_data(data):
    # Assume que data é lista, mas não está claro
    return sum(data)

# Uso de variáveis globais implicitamente
count = 0

def increment():
    global count  # Pelo menos isso é explícito, mas ainda problemático
    count += 1

# Importação com wildcard
from math import *
result = sqrt(16)  # De onde vem sqrt?
```

### ✅ Explícito

```python
# Tipos claros, conversões explícitas
def process_data(data: list[int]) -> int:
    """Retorna a soma de uma lista de inteiros."""
    if not isinstance(data, list):
        raise TypeError("data deve ser uma lista")
    return sum(data)

# Estado explícito passado como argumento
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
    
    def get_count(self) -> int:
        return self.count

# Importação explícita
import math
result = math.sqrt(16)  # Claramente do módulo math

# Ou importação específica
from math import sqrt
result = sqrt(16)  # Sabemos que importamos sqrt
```

**Mais exemplos:**

```python
# ❌ Implícito: self não passado explicitamente em outras linguagens
# Python força explicitação
class Dog:
    def __init__(self, name):
        self.name = name  # self explícito
    
    def bark(self):
        print(f"{self.name} says woof!")  # self explícito

# ✅ Argumentos explícitos com valores padrão
def create_user(name: str, age: int, active: bool = True):
    """
    Cria um usuário.
    active é explicitamente True por padrão.
    """
    return {"name": name, "age": age, "active": active}

# ❌ Modificação implícita
def add_item(list_items=[]):  # PERIGO: default mutable
    list_items.append("item")
    return list_items

# ✅ Explícito sobre mutabilidade
def add_item(list_items: list[str] | None = None) -> list[str]:
    """Adiciona item a lista, criando nova lista se None."""
    if list_items is None:
        list_items = []
    list_items.append("item")
    return list_items
```

---

## 3. Simple is better than complex

### ❌ Complexo Desnecessariamente

```python
# Over-engineering para problema simples
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
result = processor.process(5)  # Resultado: 20

# Solução excessivamente abstrata
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

### ✅ Simples

```python
# Solução direta para o problema
def process_number(number):
    """Dobra o número e adiciona 10."""
    return (number * 2) + 10

result = process_number(5)  # Resultado: 20

# Solução direta sem abstrações desnecessárias
def get_dog_sound():
    return "Woof"

sound = get_dog_sound()

# Ou se realmente precisa de estrutura:
ANIMAL_SOUNDS = {
    "dog": "Woof",
    "cat": "Meow",
    "cow": "Moo"
}

def get_animal_sound(animal_type):
    return ANIMAL_SOUNDS.get(animal_type, "Unknown sound")
```

**Exemplo de simplicidade com composição:**

```python
# ❌ Complexo: herança profunda
class Vehicle:
    def start(self): pass

class LandVehicle(Vehicle):
    def drive(self): pass

class Car(LandVehicle):
    def open_trunk(self): pass

class ElectricCar(Car):
    def charge(self): pass

# ✅ Simples: composição
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

### ❌ Complicado (Confuso, Emaranhado)

```python
# Lógica entrelaçada, difícil de seguir
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

# Função que faz muitas coisas
def handle_user_data(data, mode, options=None):
    if mode == 'create':
        # 50 linhas de código
        pass
    elif mode == 'update':
        # 50 linhas diferentes
        pass
    elif mode == 'delete':
        # mais 50 linhas
        pass
    # ... continua
```

### ✅ Complexo (Bem Organizado, Clara Estrutura)

```python
# Complexidade organizada em módulos compreensíveis
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
    """Valida regras de negócio do pedido."""
    
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
    """Calcula valores do pedido."""
    
    @staticmethod
    def calculate_total(items: list[OrderItem]) -> float:
        return sum(item.price for item in items)
    
    @staticmethod
    def check_limit(total: float, limit: float) -> bool:
        return total <= limit

class OrderProcessor:
    """Processa pedidos coordenando validação e cálculo."""
    
    def __init__(self):
        self.validator = OrderValidator()
        self.calculator = OrderCalculator()
    
    def process_order(self, order: Order) -> dict:
        # Validação em etapas claras
        if error := self.validator.validate_status(order):
            return {'error': error}
        
        if error := self.validator.validate_payment(order.payment):
            return {'error': error}
        
        if error := self.validator.validate_items(order.items):
            return {'error': error}
        
        # Cálculo
        total = self.calculator.calculate_total(order.items)
        
        if not self.calculator.check_limit(total, order.payment.limit):
            return {'error': 'limit_exceeded'}
        
        # Processamento
        self._update_stock(order.items)
        order.status = 'processing'
        
        return {'success': True, 'total': total}
    
    def _update_stock(self, items: list[OrderItem]):
        for item in items:
            item.stock -= 1

# Uso
processor = OrderProcessor()
result = processor.process_order(my_order)
```

**Diferença chave:**

- **Complicado**: Tudo misturado, difícil seguir
- **Complexo**: Múltiplas partes, cada uma clara, organização lógica

---

## 5. Flat is better than nested

### ❌ Muito Aninhado

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

# Herança profunda
class A:
    pass

class B(A):
    pass

class C(B):
    pass

class D(C):
    pass

class E(D):
    pass  # 5 níveis!
```

### ✅ Plano (Flat)

```python
# Guard clauses - retorna cedo
def process_data(data):
    # Validações no topo
    if not data:
        return []
    
    if not isinstance(data, list):
        return []
    
    if len(data) == 0:
        return []
    
    # Lógica principal sem aninhamento profundo
    result = []
    for item in data:
        if should_process_item(item):
            result.append(process_item(item))
    
    return result

def should_process_item(item):
    """Verifica se item deve ser processado."""
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
    """Processa um item válido."""
    return item['value'] * 2

# Composição ao invés de herança profunda
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
    """Compõe funcionalidades horizontalmente."""
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

**Técnicas de "aplanamento":**

```python
# ❌ Aninhado
def find_user(users, user_id):
    for user in users:
        if user['id'] == user_id:
            if user['active']:
                if user['verified']:
                    return user
    return None

# ✅ Plano com compreensão
def find_user(users, user_id):
    active_verified_users = [
        user for user in users
        if user['id'] == user_id
        and user['active']
        and user['verified']
    ]
    return active_verified_users[0] if active_verified_users else None

# ✅ Plano com função auxiliar
def is_valid_user(user, user_id):
    return (user['id'] == user_id and 
            user['active'] and 
            user['verified'])

def find_user(users, user_id):
    return next((user for user in users if is_valid_user(user, user_id)), None)
```

---

## 6. Sparse is better than dense

### ❌ Denso (Compacto Demais)

```python
# Tudo apertado, difícil de ler
def calc(x,y,z):return x*y+z if x>0 else y*z+x
data=[x**2 for x in range(10) if x%2==0 and x>2 and x<8]
result={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
user={'name':'John','age':30,'email':'john@example.com','active':True,'role':'admin'}

# Múltiplas operações em uma linha
x=10;y=20;z=x+y;print(z)

# Comprehension muito longa
filtered_users=[u for u in users if u['age']>18 and u['active'] and u['verified'] and u['role']=='member' and u['subscription']=='premium']
```

### ✅ Esparso (Breathing Room)

```python
# Espaçamento adequado, fácil de ler
def calculate_value(x, y, z):
    """Calcula valor baseado em x, y, z."""
    if x > 0:
        return x * y + z
    else:
        return y * z + x

# List comprehension legível
data = [
    x ** 2 
    for x in range(10) 
    if x % 2 == 0 
    and x > 2 
    and x < 8
]

# Dict com breathing room
result = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6
}

# Informação de usuário formatada
user = {
    'name': 'John',
    'age': 30,
    'email': 'john@example.com',
    'active': True,
    'role': 'admin'
}

# Uma operação por linha
x = 10
y = 20
z = x + y
print(z)

# Comprehension quebrada em linhas lógicas
def is_premium_member(user):
    """Verifica se usuário é membro premium ativo."""
    return (
        user['age'] > 18
        and user['active']
        and user['verified']
        and user['role'] == 'member'
        and user['subscription'] == 'premium'
    )

filtered_users = [u for u in users if is_premium_member(u)]

# Ou mais explícito
filtered_users = [
    user
    for user in users
    if is_premium_member(user)
]
```

**Espaçamento em classes:**

```python
# ❌ Denso
class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):return f"Hello, {self.name}"
    def is_adult(self):return self.age>=18

# ✅ Esparso
class User:
    """Representa um usuário do sistema."""
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def greet(self) -> str:
        """Retorna saudação personalizada."""
        return f"Hello, {self.name}"
    
    def is_adult(self) -> bool:
        """Verifica se usuário é maior de idade."""
        return self.age >= 18
```

---

## 7. Readability counts

### ❌ Pouca Legibilidade

```python
# Nomes crípticos
def f(x,y):
    return[i*2for i in x if i>y]

# Lógica obscura
def calc(n):
    return n&1==0

# Sem contexto
data = [(1,2),(3,4),(5,6)]
result = [x+y for x,y in data]

# Variáveis de uma letra
a = [1,2,3,4,5]
b = []
for i in a:
    if i % 2 == 0:
        b.append(i)
```

### ✅ Alta Legibilidade

```python
# Nomes descritivos
def filter_and_double(numbers: list[int], threshold: int) -> list[int]:
    """
    Filtra números acima do threshold e dobra seus valores.
    
    Args:
        numbers: Lista de números para processar
        threshold: Valor mínimo para inclusão
    
    Returns:
        Lista de números dobrados que estão acima do threshold
    """
    return [number * 2 for number in numbers if number > threshold]

# Lógica clara
def is_even(number: int) -> bool:
    """Verifica se número é par."""
    return number % 2 == 0

# Com contexto
coordinate_pairs = [(1, 2), (3, 4), (5, 6)]
coordinate_sums = [x + y for x, y in coordinate_pairs]

# Variáveis significativas
numbers = [1, 2, 3, 4, 5]
even_numbers = []
for number in numbers:
    if is_even(number):
        even_numbers.append(number)

# Ou mais pythônico
even_numbers = [number for number in numbers if is_even(number)]
```

**Legibilidade em estruturas complexas:**

```python
# ❌ Difícil de ler
def p(d):
    return sum([v for k,v in d.items() if k.startswith('p')])

# ✅ Fácil de ler
def calculate_premium_total(transactions: dict[str, float]) -> float:
    """
    Calcula o total de transações premium.
    
    Considera apenas transações cujas chaves começam com 'p'.
    """
    premium_values = [
        value 
        for key, value in transactions.items() 
        if key.startswith('p')
    ]
    return sum(premium_values)

# Ou ainda mais claro
def calculate_premium_total(transactions: dict[str, float]) -> float:
    """Calcula o total de transações premium."""
    total = 0
    for transaction_key, transaction_value in transactions.items():
        if is_premium_transaction(transaction_key):
            total += transaction_value
    return total

def is_premium_transaction(key: str) -> bool:
    """Verifica se transação é premium baseado na chave."""
    return key.startswith('p')
```

---

## 8. Special cases aren't special enough to break the rules

### ❌ Quebrando Regras para Casos Especiais

```python
class Document:
    def save(self):
        """Salva documento no banco de dados."""
        database.save(self)

class SpecialDocument:
    def save(self):
        """Salva em arquivo porque é especial."""
        file.write(self)  # Quebra expectativa!

# Inconsistência em API
def process_data(data):
    return [x * 2 for x in data]

def process_special_data(data):
    # Mesma função, mas retorna tuple invés de lista
    return tuple(x * 2 for x in data)  # Inconsistente!

# Tratamento especial sem justificativa
def calculate_discount(price, customer_type):
    if customer_type == "VIP":
        # Regra especial não documentada
        return price * 0.5 if price > 1000 else price * 0.3
    return price * 0.1
```

### ✅ Consistência Mantida

```python
from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def save(self):
        """Salva documento."""
        pass

class DatabaseDocument(Document):
    def save(self):
        """Salva documento no banco de dados."""
        database.save(self)

class FileDocument(Document):
    def save(self):
        """Salva documento em arquivo."""
        file.write(self)

# Interface consistente
def process_data(data, output_type='list'):
    """
    Processa dados retornando tipo especificado.
    
    Args:
        data: Dados para processar
        output_type: 'list' ou 'tuple'
    """
    processed = [x * 2 for x in data]
    if output_type == 'tuple':
        return tuple(processed)
    return processed

# Regras explícitas e documentadas
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
    Calcula desconto baseado em preço e tipo de cliente.
    
    Regras:
    - VIP: 50% para compras >1000, 30% caso contrário
    - REGULAR: 15% para compras >1000, 10% caso contrário
    """
    rules = DISCOUNT_RULES.get(customer_type, DISCOUNT_RULES["REGULAR"])
    
    if price > 1000:
        return price * rules["high_value"]
    return price * rules["normal"]
```

**Protocolo consistente:**

```python
# Todas as coleções seguem mesmo protocolo
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {1: 'a', 2: 'b', 3: 'c'}

# Todas suportam:
len(my_list)      # Funciona
len(my_tuple)     # Funciona
len(my_set)       # Funciona
len(my_dict)      # Funciona

# Todas suportam:
2 in my_list      # Funciona
2 in my_tuple     # Funciona
2 in my_set       # Funciona
2 in my_dict      # Funciona (verifica keys)

# Todas são iteráveis:
for item in my_list: pass
for item in my_tuple: pass
for item in my_set: pass
for item in my_dict: pass  # Itera sobre keys
```

---

## 9. Although practicality beats purity

### Exemplo: Pureza vs Pragmatismo

```python
# ❌ "Puro" mas impraticável
class ImmutableList:
    """Lista completamente imutável - pura mas frustrante."""
    def __init__(self, items):
        self._items = tuple(items)  # Imutável
    
    def append(self, item):
        # Retorna NOVA lista - ineficiente
        return ImmutableList(list(self._items) + [item])
    
    def __getitem__(self, index):
        return self._items[index]

# Uso impraticável
lista = ImmutableList([1, 2, 3])
lista = lista.append(4)  # Precisa reatribuir sempre
lista = lista.append(5)
lista = lista.append(6)

# ✅ Pragmático - permite mutabilidade quando útil
class FlexibleList:
    """Lista que permite mutação quando necessário."""
    def __init__(self, items):
        self._items = list(items)
    
    def append(self, item):
        self._items.append(item)  # Mutação direta - eficiente
    
    def as_immutable(self):
        """Retorna versão imutável quando necessário."""
        return tuple(self._items)

# Uso pragmático
lista = FlexibleList([1, 2, 3])
lista.append(4)
lista.append(5)
imutavel = lista.as_immutable()  # Quando precisa de garantia
```

**Outro exemplo: Type Hints (pragmatismo)**

```python
# Python permite código sem type hints (pragmático)
def calcular_area(base, altura):
    return base * altura

# Mas permite adicionar quando útil
def calcular_area(base: float, altura: float) -> float:
    """Calcula área do retângulo."""
    return base * altura

# Não força verificação em runtime (pragmático)
# Usa ferramentas externas (mypy) quando necessário
```

**Pragmatismo com GIL:**

```python
# Python tem GIL (Global Interpreter Lock)
# Não é "puro" para paralelismo, mas pragmático:

# Para tarefas CPU-bound: usa multiprocessing
from multiprocessing import Pool

def process_item(item):
    # Computação pesada
    return item ** 2

with Pool(4) as pool:
    results = pool.map(process_item, range(100))

# Para I/O-bound: threading funciona bem apesar do GIL
from threading import Thread
import requests

def fetch_url(url):
    response = requests.get(url)  # I/O não afetado pelo GIL
    return response.text

threads = [Thread(target=fetch_url, args=(url,)) for url in urls]
```

**Pragmatismo em APIs:**

```python
# ✅ API pragmática - aceita múltiplos tipos
def process_input(data: str | list[str] | dict) -> list:
    """
    Processa entrada em múltiplos formatos.
    Pragmático - facilita uso.
    """
    if isinstance(data, str):
        return [data]
    elif isinstance(data, list):
        return data
    elif isinstance(data, dict):
        return list(data.values())
    raise TypeError("Tipo não suportado")

# Uso conveniente
process_input("hello")           # OK
process_input(["a", "b"])        # OK
process_input({"x": "a"})        # OK
```

---

## 10. Errors should never pass silently

### ❌ Erros Silenciosos

```python
# Erro ignorado - NUNCA faça isso
def read_config():
    try:
        with open('config.json') as f:
            return json.load(f)
    except:
        pass  # Erro passa silenciosamente!
    return {}

# Retorno de None esconde erro
def divide(a, b):
    if b == 0:
        return None  # Erro silencioso
    return a / b

result = divide(10, 0)
print(result * 2)  # TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'

# Conversão silenciosa pode esconder problemas
def process_age(age_str):
    try:
        return int(age_str)
    except:
        return 0  # Idade 0 pode ser válida ou erro?
```

### ✅ Erros Explícitos

```python
# Erro explícito e informativo
def read_config():
    """Lê configuração do arquivo JSON."""
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

# Exceção específica
def divide(a: float, b: float) -> float:
    """
    Divide a por b.
    
    Raises:
        ValueError: Se b for zero
    """
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b

# Ou retorna Result type para erros esperados
from typing import Union

def divide_safe(a: float, b: float) -> Union[float, str]:
    """Divide retornando resultado ou mensagem de erro."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Validação explícita
def process_age(age_str: str) -> int:
    """
    Converte string de idade para inteiro.
    
    Raises:
        ValueError: Se age_str não for número válido
        ValueError: Se idade for negativa
    """
    try:
        age = int(age_str)
    except ValueError as e:
        raise ValueError(f"'{age_str}' não é uma idade válida") from e
    
    if age < 0:
        raise ValueError(f"Idade não pode ser negativa: {age}")
    
    return age
```

**Exceções customizadas:**

```python
# Hierarquia de exceções específicas
class ApplicationError(Exception):
    """Erro base da aplicação."""
    pass

class ValidationError(ApplicationError):
    """Erro de validação de dados."""
    pass

class DatabaseError(ApplicationError):
    """Erro de operação de banco de dados."""
    pass

class ConnectionError(DatabaseError):
    """Erro de conexão com banco."""
    pass

# Uso
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

### ❌ Supressão Acidental

```python
# Catch-all perigoso
try:
    result = complex_operation()
    process(result)
    save(result)
except:  # Pega TUDO, inclusive KeyboardInterrupt!
    pass

# Erro específico tratado incorretamente
try:
    data = fetch_data()
except Exception:
    data = None  # Esconde o verdadeiro problema
```

### ✅ Supressão Explícita e Justificada

```python
import logging
from contextlib import suppress

logger = logging.getLogger(__name__)

# Supressão explícita com contextlib
def cleanup_temp_files():
    """Remove arquivos temporários, ignorando se não existem."""
    temp_files = ['temp1.txt', 'temp2.txt', 'temp3.txt']
    
    for temp_file in temp_files:
        # Explicitamente suprimimos FileNotFoundError
        # porque não é erro se arquivo já foi deletado
        with suppress(FileNotFoundError):
            os.remove(temp_file)

# Tratamento explícito com logging
def load_optional_config():
    """Carrega configuração opcional."""
    try:
        with open('optional_config.json') as f:
            return json.load(f)
    except FileNotFoundError:
        # Explicitamente decidimos que este erro é OK
        logger.info("Configuração opcional não encontrada, usando padrões")
        return DEFAULT_CONFIG
    except json.JSONDecodeError as e:
        # Este erro NÃO suprimimos - precisa atenção
        logger.error(f"Configuração inválida: {e}")
        raise

# Fallback explícito
def get_user_preference(user_id: str, preference: str) -> str:
    """
    Obtém preferência do usuário com fallback para padrão.
    """
    try:
        return database.get_preference(user_id, preference)
    except PreferenceNotFoundError:
        # Supressão explícita - retorna padrão documentado
        logger.debug(
            f"Preferência '{preference}' não encontrada "
            f"para usuário {user_id}, usando padrão"
        )
        return DEFAULT_PREFERENCES[preference]
    except DatabaseError:
        # Este erro NÃO suprimimos
        logger.error(f"Erro ao acessar banco para usuário {user_id}")
        raise
```

**Padrão de retry com supressão:**

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
    Tenta executar função com retry e backoff exponencial.
    
    Suprime erros transitórios mas re-levanta após max_attempts.
    """
    last_exception = None
    
    for attempt in range(max_attempts):
        try:
            return func()
        except TransientError as e:
            # Supressão explícita de erro transitório
            last_exception = e
            if attempt < max_attempts - 1:
                wait_time = backoff_seconds * (2 ** attempt)
                logger.warning(
                    f"Tentativa {attempt + 1} falhou: {e}. "
                    f"Tentando novamente em {wait_time}s"
                )
                time.sleep(wait_time)
            else:
                logger.error(
                    f"Todas as {max_attempts} tentativas falharam"
                )
    
    # Após todas tentativas, erro não é mais suprimido
    raise last_exception
```

---

## 12. In the face of ambiguity, refuse the temptation to guess

### ❌ Adivinhação

```python
# Adivinha tipo baseado em valor
def process(value):
    # RUIM: Tenta adivinhar o que fazer
    if value < 10:
        return value * 2
    elif value < 100:
        return value * 3
    else:
        return str(value)  # Muda tipo de retorno!

# Adivinha formato de data
def parse_date(date_string):
    # Tenta múltiplos formatos - qual usar?
    formats = ['%Y-%m-%d', '%d/%m/%Y', '%m-%d-%Y']
    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    return None  # Falha silenciosa!

# Comportamento inconsistente
def get_value(data, key):
    # Às vezes retorna valor, às vezes lista, às vezes None
    if key in data:
        value = data[key]
        if isinstance(value, list) and len(value) == 1:
            return value[0]  # "Simplifica" automaticamente
        return value
    return None
```

### ✅ Explícito, Não Adivinha

```python
# Tipo e comportamento explícitos
def double_number(value: int) -> int:
    """Dobra um número inteiro."""
    if not isinstance(value, int):
        raise TypeError(f"Esperado int, recebido {type(value)}")
    return value * 2

def triple_number(value: int) -> int:
    """Triplica um número inteiro."""
    if not isinstance(value, int):
        raise TypeError(f"Esperado int, recebido {type(value)}")
    return value * 3

# Formato de data explícito
def parse_date_iso(date_string: str) -> datetime:
    """
    Parseia data no formato ISO (YYYY-MM-DD).
    
    Raises:
        ValueError: Se formato não for ISO válido
    """
    try:
        return datetime.strptime(date_string, '%Y-%m-%d')
    except ValueError as e:
        raise ValueError(
            f"Data '{date_string}' não está no formato ISO (YYYY-MM-DD)"
        ) from e

# Ou permite especificar formato
def parse_date(date_string: str, format: str) -> datetime:
    """
    Parseia data no formato especificado.
    
    Args:
        date_string: String contendo data
        format: Formato strptime (ex: '%Y-%m-%d')
    """
    try:
        return datetime.strptime(date_string, format)
    except ValueError as e:
        raise ValueError(
            f"Data '{date_string}' não corresponde ao formato '{format}'"
        ) from e

# Comportamento consistente e explícito
def get_value(data: dict, key: str) -> any:
    """
    Obtém valor da chave, levantando erro se não existir.
    
    Raises:
        KeyError: Se chave não existir
    """
    if key not in data:
        raise KeyError(f"Chave '{key}' não encontrada")
    return data[key]

def get_value_or_default(data: dict, key: str, default: any = None) -> any:
    """Obtém valor ou retorna padrão se chave não existir."""
    return data.get(key, default)

def get_values_list(data: dict, key: str) -> list:
    """
    Obtém valor como lista.
    
    Se valor não for lista, retorna lista com único elemento.
    """
    value = get_value(data, key)
    if isinstance(value, list):
        return value
    return [value]
```

**Conversões explícitas:**

```python
# ❌ Conversão implícita/adivinhação
def add(a, b):
    # Tenta adivinhar se deve somar, concatenar, etc
    try:
        return int(a) + int(b)
    except:
        return str(a) + str(b)

# ✅ Tipo explícito
def add_numbers(a: int, b: int) -> int:
    """Soma dois números inteiros."""
    return a + b

def concatenate_strings(a: str, b: str) -> str:
    """Concatena duas strings."""
    return a + b

def add_flexible(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Soma números, preservando tipo float se presente."""
    return a + b
```

---

---

> **Continua:** [Parte 2 - Princípios 13-19 →](pratica_parte2.md)

