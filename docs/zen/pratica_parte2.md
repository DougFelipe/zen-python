# O Zen of Python - Exemplos Práticos (Parte 2)

> **Navegação:** [← Voltar ao Início](../index.md) | [← Teoria](teoria.md) | [← Parte 1](pratica_parte1.md) | [Otimização →](../otimizacao/guia_completo.md)

## Índice Rápido

**Neste documento (13-19):**

13. [There should be one obvious way to do it](#13-there-should-be-one-and-preferably-only-one-obvious-way-to-do-it)
14. [Although that way may not be obvious at first](#14-although-that-way-may-not-be-obvious-at-first-unless-youre-dutch)
15. [Now is better than never](#15-now-is-better-than-never)
16. [Although never is often better than right now](#16-although-never-is-often-better-than-right-now)
17. [If the implementation is hard to explain](#17-if-the-implementation-is-hard-to-explain-its-a-bad-idea)
18. [If the implementation is easy to explain](#18-if-the-implementation-is-easy-to-explain-it-may-be-a-good-idea)
19. [Namespaces are one honking great idea](#19-namespaces-are-one-honking-great-idea-lets-do-more-of-those)

**Na Parte 1:** [← Princípios 1-12](pratica_parte1.md)

---

## 13. There should be one-- and preferably only one --obvious way to do it

### Múltiplas Formas vs Uma Forma Óbvia

```python
# ===== ITERAR SOBRE LISTA =====

# ✅ Forma óbvia (Pythônica)
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)

# ❌ Possível, mas não óbvio
for i in range(len(fruits)):
    print(fruits[i])

# ❌ Possível, mas não idiomático
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# ===== VERIFICAR SE LISTA ESTÁ VAZIA =====

my_list = []

# ✅ Forma óbvia (Pythônica)
if not my_list:
    print("Lista vazia")

# ❌ Possível, mas não idiomático
if len(my_list) == 0:
    print("Lista vazia")

# ❌ Possível, mas verboso
if my_list == []:
    print("Lista vazia")

# ===== LER ARQUIVO =====

# ✅ Forma óbvia (context manager)
with open('data.txt') as f:
    data = f.read()

# ❌ Possível, mas esquece de fechar
f = open('data.txt')
data = f.read()
f.close()

# ❌ Possível, mas complexo
try:
    f = open('data.txt')
    data = f.read()
finally:
    f.close()

# ===== CRIAR DICIONÁRIO DE CONTAGEM =====

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# ✅ Forma óbvia (Counter)
from collections import Counter
word_count = Counter(words)

# ❌ Possível, mas mais código
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# ❌ Possível, mas menos claro
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# ===== TROCAR VALORES DE VARIÁVEIS =====

a, b = 10, 20

# ✅ Forma óbvia (tuple unpacking)
a, b = b, a

# ❌ Possível, mas mais código
temp = a
a = b
b = temp

# ===== COMBINAR DUAS LISTAS =====

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# ✅ Forma óbvia para combinar
combined = list1 + list2

# ✅ Forma óbvia para iterar simultaneamente
for item1, item2 in zip(list1, list2):
    print(item1, item2)

# ❌ Possível, mas não idiomático
for i in range(len(list1)):
    print(list1[i], list2[i])

# ===== STRING FORMATTING =====

name = "Alice"
age = 30

# ✅ Forma óbvia (f-strings, Python 3.6+)
message = f"My name is {name} and I am {age} years old"

# ❌ Possível, mas desatualizado
message = "My name is %s and I am %d years old" % (name, age)

# ❌ Possível, mas verboso
message = "My name is {} and I am {} years old".format(name, age)

# ===== CHECAR MÚLTIPLOS VALORES =====

value = 5

# ✅ Forma óbvia
if value in {1, 2, 3, 4, 5}:
    print("Found")

# ❌ Possível, mas repetitivo
if value == 1 or value == 2 or value == 3 or value == 4 or value == 5:
    print("Found")
```

**Casos onde há múltiplas formas legítimas:**

```python
# List comprehension vs map/filter
# Ambas são aceitáveis, mas comprehension é geralmente preferida

numbers = [1, 2, 3, 4, 5]

# ✅ Preferido (mais pythônico)
doubled = [n * 2 for n in numbers]
evens = [n for n in numbers if n % 2 == 0]

# ✅ Aceitável (funcional)
doubled = list(map(lambda n: n * 2, numbers))
evens = list(filter(lambda n: n % 2 == 0, numbers))

# Escolha depende do contexto:
# - Comprehension: geralmente mais legível
# - map/filter: útil com funções já existentes

def double(n):
    return n * 2

doubled = list(map(double, numbers))  # OK quando função já existe
```

---

## 14. Although that way may not be obvious at first unless you're Dutch

### Idiomas Pythônicos que se Aprende com o Tempo

```python
# ===== ENUMERATE =====

# ❌ Não óbvio para iniciantes
items = ['a', 'b', 'c']
for i in range(len(items)):
    print(f"Index {i}: {items[i]}")

# ✅ Pythônico (aprende-se)
for index, item in enumerate(items):
    print(f"Index {index}: {item}")

# Enumerate com start customizado
for index, item in enumerate(items, start=1):
    print(f"Item {index}: {item}")

# ===== ZIP =====

# ❌ Forma iniciante
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old")

# ✅ Pythônico
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# ✅ Zip com múltiplas listas
cities = ['NYC', 'LA', 'Chicago']
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, lives in {city}")

# ===== DICT COMPREHENSION =====

# ❌ Forma iniciante
pairs = [('a', 1), ('b', 2), ('c', 3)]
result = {}
for key, value in pairs:
    result[key] = value

# ✅ Pythônico
result = {key: value for key, value in pairs}

# ✅ Transformação
numbers = [1, 2, 3, 4, 5]
squares = {n: n**2 for n in numbers}

# ===== ANY e ALL =====

# ❌ Forma iniciante
numbers = [1, 3, 5, 7, 8]
has_even = False
for n in numbers:
    if n % 2 == 0:
        has_even = True
        break

# ✅ Pythônico
has_even = any(n % 2 == 0 for n in numbers)

# ❌ Forma iniciante
all_positive = True
for n in numbers:
    if n <= 0:
        all_positive = False
        break

# ✅ Pythônico
all_positive = all(n > 0 for n in numbers)

# ===== UNPACKING =====

# ❌ Forma iniciante
point = (10, 20)
x = point[0]
y = point[1]

# ✅ Pythônico
x, y = point

# ✅ Extended unpacking
first, *middle, last = [1, 2, 3, 4, 5]
# first = 1, middle = [2, 3, 4], last = 5

# ✅ Swapping
a, b = b, a

# ===== DICT.GET COM DEFAULT =====

# ❌ Forma iniciante
config = {'debug': True}
if 'timeout' in config:
    timeout = config['timeout']
else:
    timeout = 30

# ✅ Pythônico
timeout = config.get('timeout', 30)

# ===== SETDEFAULT =====

# ❌ Forma iniciante
word_positions = {}
words = ['a', 'b', 'a', 'c', 'b']

for i, word in enumerate(words):
    if word not in word_positions:
        word_positions[word] = []
    word_positions[word].append(i)

# ✅ Pythônico
word_positions = {}
for i, word in enumerate(words):
    word_positions.setdefault(word, []).append(i)

# ✅ Ou use defaultdict
from collections import defaultdict
word_positions = defaultdict(list)
for i, word in enumerate(words):
    word_positions[word].append(i)

# ===== TERNÁRIO =====

# ❌ Forma iniciante
age = 25
if age >= 18:
    status = "adult"
else:
    status = "minor"

# ✅ Pythônico
status = "adult" if age >= 18 else "minor"

# ===== CHAIN DE COMPARAÇÕES =====

# ❌ Forma iniciante
x = 5
if x > 0 and x < 10:
    print("In range")

# ✅ Pythônico
if 0 < x < 10:
    print("In range")

# ===== REVERSED E SORTED =====

# ❌ Forma iniciante
items = [1, 2, 3, 4, 5]
reversed_items = []
for i in range(len(items)-1, -1, -1):
    reversed_items.append(items[i])

# ✅ Pythônico
reversed_items = list(reversed(items))

# ❌ Forma iniciante para ordenar
sorted_items = items.copy()
sorted_items.sort()

# ✅ Pythônico (não modifica original)
sorted_items = sorted(items)

# ===== WALRUS OPERATOR (Python 3.8+) =====

# ❌ Avaliação dupla
data = fetch_data()
if len(data) > 10:
    print(f"Processing {len(data)} items")

# ✅ Pythônico com walrus
if (n := len(data)) > 10:
    print(f"Processing {n} items")

# Útil em list comprehensions
# ❌ Calcula duas vezes
results = [expensive_func(x) for x in data if expensive_func(x) > 0]

# ✅ Calcula uma vez
results = [y for x in data if (y := expensive_func(x)) > 0]
```

---

## 15. Now is better than never

### Exemplos de Ação vs Procrastinação

```python
# ===== REFATORAÇÃO =====

# ❌ Deixar para depois (técnica: deixa comentário TODO)
def process_order(order):
    # TODO: Refatorar isso aqui, está confuso
    # TODO: Extrair validação
    # TODO: Adicionar logging
    if order['status'] == 'pending' and order['verified']:
        # 50 linhas de código confuso
        pass

# ✅ Refatorar agora (quando vê o problema)
def process_order(order: Order) -> OrderResult:
    """Processa um pedido pendente."""
    validate_order(order)
    log_order_processing(order)
    return execute_order(order)

# ===== DOCUMENTAÇÃO =====

# ❌ Código sem documentação ("vou documentar depois")
def calc(x, y, z):
    return x * y + z if x > 0 else y * z + x

# ✅ Documenta enquanto escreve
def calculate_value(x: float, y: float, z: float) -> float:
    """
    Calcula valor baseado em x, y e z.
    
    Se x é positivo: x * y + z
    Caso contrário: y * z + x
    
    Args:
        x: Primeiro valor
        y: Segundo valor
        z: Terceiro valor
    
    Returns:
        Valor calculado
    """
    if x > 0:
        return x * y + z
    return y * z + x

# ===== TESTES =====

# ❌ "Vou escrever testes depois"
def divide(a, b):
    return a / b
# (Sem testes, bug de divisão por zero não detectado)

# ✅ Escreve teste agora (TDD)
def divide(a: float, b: float) -> float:
    """Divide a por b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Teste
import pytest

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    with pytest.raises(ValueError):
        divide(10, 0)

# ===== TRATAMENTO DE ERRO =====

# ❌ "Vou adicionar tratamento depois"
def load_config():
    with open('config.json') as f:
        return json.load(f)
# (Pode crashear em produção)

# ✅ Adiciona tratamento agora
def load_config() -> dict:
    """Carrega configuração do arquivo JSON."""
    try:
        with open('config.json') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning("Config file not found, using defaults")
        return DEFAULT_CONFIG
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in config: {e}")
        raise ConfigurationError("Invalid configuration file") from e

# ===== CÓDIGO DUPLICADO =====

# ❌ Duplicação ("vou extrair depois")
def process_user_data(data):
    if not data.get('name'):
        raise ValueError("Name required")
    if not data.get('email'):
        raise ValueError("Email required")
    if not data.get('age'):
        raise ValueError("Age required")
    # ... mais código

def process_admin_data(data):
    if not data.get('name'):
        raise ValueError("Name required")
    if not data.get('email'):
        raise ValueError("Email required")
    if not data.get('age'):
        raise ValueError("Age required")
    # ... código diferente

# ✅ Extrai agora (DRY - Don't Repeat Yourself)
def validate_required_fields(data: dict, fields: list[str]):
    """Valida que campos obrigatórios estão presentes."""
    for field in fields:
        if not data.get(field):
            raise ValueError(f"{field.title()} is required")

def process_user_data(data: dict):
    validate_required_fields(data, ['name', 'email', 'age'])
    # ... mais código

def process_admin_data(data: dict):
    validate_required_fields(data, ['name', 'email', 'age'])
    # ... código diferente
```

**Princípio: Regra do Escoteiro**

```python
# "Deixe o código melhor do que encontrou"

# Encontrou isso:
def get_user(id):
    return db.query("SELECT * FROM users WHERE id="+str(id))

# Melhorou (SQL injection fix, naming, type hints):
def get_user(user_id: int) -> Optional[User]:
    """Busca usuário por ID."""
    query = "SELECT * FROM users WHERE id = ?"
    result = db.query(query, (user_id,))
    return User.from_db(result) if result else None
```

---

## 16. Although never is often better than *right* now

### Exemplos de quando NÃO fazer (ainda)

```python
# ===== YAGNI (You Aren't Gonna Need It) =====

# ❌ Over-engineering "por precaução"
class User:
    def __init__(self, name):
        self.name = name
        self.email = None  # "Vamos precisar disso"
        self.phone = None  # "Talvez precise"
        self.address = None  # "Por via das dúvidas"
        self.backup_email = None  # "Pode ser útil"
        self.preferences = {}  # "Eventualmente"
        self.metadata = {}  # "Para extensibilidade"

# ✅ Adicione apenas o que precisa AGORA
class User:
    def __init__(self, name: str):
        self.name = name

# Adicione outros campos quando REALMENTE precisar

# ===== OTIMIZAÇÃO PREMATURA =====

# ❌ Otimização antes de medir
def process_items(items):
    # Usando cache complexo "para performance"
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

# ✅ Comece simples, otimize se necessário
def process_items(items):
    """Processa items."""
    return [expensive_operation(item) for item in items]

# Se profiling mostrar que é gargalo, então otimize:
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_operation(item):
    # ... operação custosa
    pass

# ===== ABSTRAÇÃO PREMATURA =====

# ❌ Abstração sem necessidade clara
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

# ✅ Comece concreto
def process_data(data):
    """Dobra valores em data."""
    return [x * 2 for x in data]

# Adicione abstração quando tiver MÚLTIPLAS implementações reais

# ===== FEATURES ESPECULATIVAS =====

# ❌ Implementar feature "que podem pedir"
class Report:
    def generate(self):
        # Gera relatório básico
        pass
    
    def export_to_pdf(self):
        # "Talvez queiram PDF"
        pass
    
    def export_to_excel(self):
        # "Ou Excel"
        pass
    
    def export_to_csv(self):
        # "CSV também"
        pass
    
    def send_by_email(self):
        # "Pode ser útil"
        pass
    
    def schedule_generation(self):
        # "No futuro talvez"
        pass

# ✅ Implemente apenas o solicitado
class Report:
    def generate(self):
        """Gera relatório."""
        # Implementa apenas o que foi pedido
        pass

# Adicione export/email/schedule quando REALMENTE pedirem

# ===== CÓDIGO SOB PRESSÃO =====

# Situação: Bug crítico em produção, pressão para resolver "JÁ"

# ❌ Fix rápido e sujo
def process_payment(amount):
    # Quick fix: ignora validação para "resolver rápido"
    # TODO: Adicionar validação depois
    charge_card(amount)
    return True

# ✅ Melhor esperar e fazer direito (ou fazer quick fix temporário + task para corrigir)
def process_payment(amount: float) -> bool:
    """Processa pagamento com validação."""
    validate_amount(amount)
    
    try:
        charge_card(amount)
        return True
    except PaymentError as e:
        logger.error(f"Payment failed: {e}")
        raise

# Se REALMENTE precisa de fix emergencial:
def process_payment_emergency(amount):
    """
    TEMPORARY: Emergency fix for production issue.
    
    TODO: Replace with proper implementation (TICKET-123)
    REMOVE BY: 2025-03-01
    """
    # Quick fix aqui, mas documentado e agendado para remoção
    pass

# ===== FRAMEWORKS E BIBLIOTECAS =====

# ❌ Adicionar biblioteca na primeira dúvida
# Problema: Preciso formatar data
import arrow  # Biblioteca completa só para formatar data
import pendulum  # Outra biblioteca
from datetime import datetime

# ✅ Use stdlib primeiro
from datetime import datetime

def format_date(date: datetime) -> str:
    """Formata data no padrão brasileiro."""
    return date.strftime('%d/%m/%Y')

# Adicione biblioteca externa apenas se stdlib for insuficiente
```

**Decisão: Agora vs Nunca vs Depois**

```python
# Framework para decidir:

def should_implement_now(feature):
    """
    Critérios para implementar agora:
    - [ ] Foi solicitado/requerido
    - [ ] Tem caso de uso claro
    - [ ] Custo de implementação é baixo
    - [ ] Risco de não ter é alto
    """
    pass

def should_never_implement(feature):
    """
    Nunca implemente se:
    - [ ] Especulativo sem evidência
    - [ ] Complexidade > Benefício
    - [ ] Solução mais simples existe
    - [ ] Viola YAGNI
    """
    pass

def should_implement_later(feature):
    """
    Implemente depois se:
    - [ ] Precisa de mais pesquisa
    - [ ] Requer design cuidadoso
    - [ ] Dependências não resolvidas
    - [ ] Pode aprender mais esperando
    """
    pass
```

---

## 17. If the implementation is hard to explain, it's a bad idea

### Exemplos de Difícil vs Fácil de Explicar

```python
# ===== ALGORITMO CONFUSO =====

# ❌ Difícil de explicar
def mystery_func(lst):
    return [i for i, x in enumerate(lst) if x == lst[i::-1][0]]

# Tente explicar: "Retorna índices onde... hmm... quando o elemento é igual a... 
# o primeiro elemento da sublista reversa a partir daquele índice?"

# ✅ Fácil de explicar
def find_palindrome_centers(text: str) -> list[int]:
    """
    Encontra índices que são centros de palíndromos.
    
    Retorna lista de índices onde o caractere é igual ao caractere
    na mesma posição contando do início da string.
    """
    centers = []
    for index, char in enumerate(text):
        if char == text[-(index + 1)]:
            centers.append(index)
    return centers

# ===== LÓGICA COMPLEXA =====

# ❌ Difícil de explicar
def calc(a, b, c=None, d=None, mode='x'):
    if mode == 'x':
        return (a * b) + (c or 0) - (d or 0)
    elif mode == 'y':
        return (a + b) * (c or 1) / (d or 1)
    else:
        return ((a if c else b) * (d if d else c if c else 1))

# ✅ Fácil de explicar
def calculate_total(base: float, multiplier: float, 
                   addition: float = 0, subtraction: float = 0) -> float:
    """
    Calcula: (base * multiplier) + addition - subtraction
    
    Args:
        base: Valor base
        multiplier: Multiplicador
        addition: Valor a adicionar (padrão 0)
        subtraction: Valor a subtrair (padrão 0)
    
    Returns:
        Resultado do cálculo
    """
    return (base * multiplier) + addition - subtraction

def calculate_ratio(numerator: float, denominator: float,
                   numerator_factor: float = 1,
                   denominator_factor: float = 1) -> float:
    """
    Calcula: (numerator + denominator) * numerator_factor / denominator_factor
    """
    return (numerator + denominator) * numerator_factor / denominator_factor

# ===== ESTRUTURA DE DADOS CONFUSA =====

# ❌ Difícil de explicar
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

# ✅ Fácil de explicar
from dataclasses import dataclass

@dataclass
class Address:
    """Endereço do usuário."""
    city: str
    state: str

@dataclass
class User:
    """Informações do usuário."""
    name: str
    age: int
    address: Address

user = User(
    name='John',
    age=30,
    address=Address(city='NYC', state='NY')
)

# ===== FUNÇÃO COM EFEITOS COLATERAIS OCULTOS =====

# ❌ Difícil de explicar comportamento completo
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

# Tente explicar: "Processa data, mas também incrementa contador global,
# usa cache, mas limpa cache a cada 100 chamadas, e multiplica resultado
# pelo contador..."

# ✅ Fácil de explicar
class DataProcessor:
    """Processa dados com cache e contagem."""
    
    def __init__(self, cache_limit: int = 100):
        self.call_count = 0
        self.cache = {}
        self.cache_limit = cache_limit
    
    def process(self, data):
        """
        Processa dados, usando cache quando possível.
        
        Cache é limpo automaticamente após cache_limit chamadas.
        """
        self.call_count += 1
        
        if self.call_count > self.cache_limit:
            self.clear_cache()
        
        if data not in self.cache:
            self.cache[data] = expensive_operation(data)
        
        return self.cache[data] * self.call_count
    
    def clear_cache(self):
        """Limpa cache e reseta contador."""
        self.cache.clear()
        self.call_count = 0
```

**Teste da explicação:**

```python
# Se você não consegue explicar em 2-3 frases simples, reconsidere o design

# ❌ Difícil
def complex_function(x, y, z, mode=None, *args, **kwargs):
    # Tenta fazer muitas coisas
    # Comportamento muda baseado em kwargs
    # Efeitos colaterais escondidos
    pass

# ✅ Fácil
def calculate_average(numbers: list[float]) -> float:
    """Calcula a média de uma lista de números."""
    return sum(numbers) / len(numbers)
```

---

## 18. If the implementation is easy to explain, it may be a good idea

### "May be" - Facilidade de Explicação Não Garante Qualidade

```python
# ===== FÁCIL DE EXPLICAR, MAS RUIM =====

# ❌ Fácil de explicar: "Apenas ignora o erro"
def divide(a, b):
    try:
        return a / b
    except:
        pass  # Ignora erro - simples!
# Problema: Esconde bugs

# ❌ Fácil de explicar: "Usa variável global"
total = 0

def add_to_total(value):
    global total
    total += value  # Adiciona ao total global
# Problema: Estado global, difícil testar

# ❌ Fácil de explicar: "Copia e cola o código"
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
# Problema: Duplicação

# ===== FÁCIL DE EXPLICAR E BOM =====

# ✅ Fácil de explicar: "Dobra cada número"
def double_numbers(numbers: list[int]) -> list[int]:
    """Dobra cada número na lista."""
    return [n * 2 for n in numbers]

# ✅ Fácil de explicar: "Busca usuário por ID"
def get_user_by_id(user_id: int) -> Optional[User]:
    """
    Busca usuário no banco de dados por ID.
    
    Returns None se usuário não for encontrado.
    """
    return db.query(User).filter(User.id == user_id).first()

# ✅ Fácil de explicar: "Valida email"
import re

def is_valid_email(email: str) -> bool:
    """Verifica se email tem formato válido."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# ===== CHECKLIST ALÉM DA EXPLICABILIDADE =====

def evaluate_solution(solution):
    """
    Checklists para avaliar solução além de ser fácil de explicar:
    
    ✓ Fácil de explicar
    ✓ Resolve o problema corretamente
    ✓ Seguro (sem vulnerabilidades)
    ✓ Eficiente (performance aceitável)
    ✓ Manutenível
    ✓ Testável
    ✓ Sem efeitos colaterais inesperados
    ✓ Segue princípios SOLID
    """
    pass

# Exemplo: Solução que passa em todos critérios

class UserService:
    """Serviço para operações de usuário."""
    
    def __init__(self, db_session, email_service):
        self.db = db_session
        self.email = email_service
    
    def create_user(self, name: str, email: str) -> User:
        """
        Cria novo usuário.
        
        1. Valida email
        2. Verifica se email já existe
        3. Cria usuário no banco
        4. Envia email de boas-vindas
        
        Raises:
            ValueError: Se email for inválido
            UserExistsError: Se email já estiver cadastrado
        """
        # Fácil de explicar: valida
        if not self._is_valid_email(email):
            raise ValueError(f"Email inválido: {email}")
        
        # Fácil de explicar: verifica duplicata
        if self._email_exists(email):
            raise UserExistsError(f"Email já cadastrado: {email}")
        
        # Fácil de explicar: cria usuário
        user = User(name=name, email=email)
        self.db.add(user)
        self.db.commit()
        
        # Fácil de explicar: envia boas-vindas
        self.email.send_welcome(user)
        
        return user
    
    def _is_valid_email(self, email: str) -> bool:
        """Valida formato de email."""
        return '@' in email and '.' in email
    
    def _email_exists(self, email: str) -> bool:
        """Verifica se email já está cadastrado."""
        return self.db.query(User).filter(User.email == email).exists()
```

---

## 19. Namespaces are one honking great idea -- let's do more of those!

### Uso Efetivo de Namespaces

```python
# ===== MÓDULOS COMO NAMESPACES =====

# ❌ Polui namespace global
from math import *
from statistics import *

result1 = sqrt(16)  # De onde vem?
result2 = mean([1, 2, 3])  # De onde vem?

# ✅ Namespace explícito
import math
import statistics

result1 = math.sqrt(16)  # Claramente do módulo math
result2 = statistics.mean([1, 2, 3])  # Claramente do statistics

# ✅ Import específico quando não há conflito
from math import sqrt, pi
from statistics import mean, median

# ===== PACOTES PARA ORGANIZAÇÃO =====

# Estrutura de projeto com namespaces claros
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

# Uso com namespaces claros
from myproject.models.user import User
from myproject.models.product import Product
from myproject.services.user_service import UserService
from myproject.utils.validators import validate_email

# ===== CLASSES COMO NAMESPACES =====

# ❌ Funções globais relacionadas
def validate_user_email(email):
    pass

def validate_user_age(age):
    pass

def validate_user_password(password):
    pass

def format_user_name(name):
    pass

# ✅ Agrupadas em classe/namespace
class UserValidator:
    """Namespace para validações de usuário."""
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Valida email do usuário."""
        return '@' in email
    
    @staticmethod
    def validate_age(age: int) -> bool:
        """Valida idade do usuário."""
        return 0 < age < 150
    
    @staticmethod
    def validate_password(password: str) -> bool:
        """Valida senha do usuário."""
        return len(password) >= 8

class UserFormatter:
    """Namespace para formatação de usuário."""
    
    @staticmethod
    def format_name(name: str) -> str:
        """Formata nome do usuário."""
        return name.title()
    
    @staticmethod
    def format_phone(phone: str) -> str:
        """Formata telefone do usuário."""
        return f"({phone[:2]}) {phone[2:7]}-{phone[7:]}"

# Uso
if UserValidator.validate_email(email):
    formatted_name = UserFormatter.format_name(name)

# ===== ENUM COMO NAMESPACE =====

# ❌ Constantes globais
USER_STATUS_ACTIVE = 'active'
USER_STATUS_INACTIVE = 'inactive'
USER_STATUS_SUSPENDED = 'suspended'

ORDER_STATUS_PENDING = 'pending'
ORDER_STATUS_PROCESSING = 'processing'

# ✅ Enum namespace
from enum import Enum

class UserStatus(Enum):
    """Status possíveis de usuário."""
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    SUSPENDED = 'suspended'

class OrderStatus(Enum):
    """Status possíveis de pedido."""
    PENDING = 'pending'
    PROCESSING = 'processing'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

# Uso claro
user.status = UserStatus.ACTIVE
order.status = OrderStatus.PENDING

# ===== DATACLASS/NAMEDTUPLE COMO NAMESPACE =====

# ❌ Dict com strings mágicas
config = {
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'mydb'
}

host = config['db_host']  # Propenso a typos

# ✅ Dataclass namespace
from dataclasses import dataclass

@dataclass
class DatabaseConfig:
    """Configuração de banco de dados."""
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

# Acesso com autocomplete e type checking
host = config.host

# ===== CONTEXTO DE NAMESPACE =====

# ❌ Variável global acessível de qualquer lugar
current_user = None

def process_order():
    global current_user
    # Usa current_user
    pass

# ✅ Namespace de contexto (threading.local ou contextvars)
from contextvars import ContextVar

current_user: ContextVar[User] = ContextVar('current_user')

def process_order():
    user = current_user.get()
    # Usa user do contexto, não global

# ===== HIERARQUIA DE NAMESPACES =====

# Python usa LEGB para resolução de nomes:
# Local -> Enclosing -> Global -> Built-in

x = "global"  # Global namespace

def outer():
    x = "enclosing"  # Enclosing namespace
    
    def inner():
        x = "local"  # Local namespace
        print(x)  # Imprime "local"
    
    inner()
    print(x)  # Imprime "enclosing"

outer()
print(x)  # Imprime "global"

# Built-in
len([1, 2, 3])  # len vem do namespace built-in

# ===== BOAS PRÁTICAS COM NAMESPACES =====

# ✅ Use imports específicos para clareza
from collections import Counter, defaultdict
from typing import List, Dict, Optional

# ✅ Agrupe imports por tipo
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from myproject.models import User
from myproject.services import UserService

# ✅ Use alias quando nomes conflitam
from myproject.models import User as UserModel
from external_lib import User as ExternalUser

# ✅ Use __all__ para controlar namespace de módulo
# mymodule.py
__all__ = ['public_function', 'PublicClass']

def public_function():
    pass

def _private_function():
    pass

class PublicClass:
    pass

# ✅ Use _ para indicar nomes privados
class MyClass:
    def __init__(self):
        self.public_attr = "público"
        self._private_attr = "privado (convenção)"
        self.__very_private = "privado (name mangling)"
    
    def public_method(self):
        pass
    
    def _private_method(self):
        pass

# ===== ANTI-PADRÕES COM NAMESPACES =====

# ❌ from module import *
from os import *  # Polui namespace com dezenas de nomes

# ❌ Nomes muito genéricos em global
data = []  # Nome muito genérico
result = None
temp = ""

# ✅ Nomes descritivos
user_data = []
calculation_result = None
temp_file_path = ""

# ❌ Modificar namespace de outro módulo
import math
math.sqrt = lambda x: x ** 0.5  # NÃO faça isso!

# ✅ Crie sua própria função
def my_sqrt(x):
    return x ** 0.5
```

**Benefícios dos Namespaces:**

```python
# 1. EVITA CONFLITOS
# Sem namespace
def process():  # Qual process?
    pass

# Com namespace
class UserProcessor:
    def process(self):  # Claramente processa usuário
        pass

class OrderProcessor:
    def process(self):  # Claramente processa pedido
        pass

# 2. ORGANIZAÇÃO
# Funções relacionadas agrupadas
class StringUtils:
    @staticmethod
    def reverse(s): ...
    
    @staticmethod
    def capitalize_words(s): ...
    
    @staticmethod
    def remove_special_chars(s): ...

# 3. EXPLICITAÇÃO
import requests
response = requests.get(url)  # Claro que é do requests

# 4. MODULARIZAÇÃO
from myapp.auth import authenticate
from myapp.db import save_to_database
from myapp.email import send_email
# Cada módulo é um namespace claro
```

---

## Conclusão Prática

O Zen of Python não são regras absolutas, mas **princípios guia**. A prática de programação Python eficaz vem de:

1. **Conhecer os princípios** (este documento)
2. **Praticar aplicação** (escrever código)
3. **Receber feedback** (code reviews)
4. **Estudar código pythônico** (projetos open source)
5. **Refletir sobre trade-offs** (discussões técnicas)

Com o tempo, esses princípios se tornam **intuição natural**, e você escreverá código pythônico sem pensar conscientemente sobre cada princípio.

**Lembre-se**: Python é sobre **legibilidade**, **simplicidade** e **praticidade**. Quando em dúvida, escolha a solução que um colega entenderia mais facilmente.

---

## Próximos Passos

- [← Voltar à Parte 1 (Princípios 1-12)](pratica_parte1.md)
- [← Aprofundar na Teoria](teoria.md)
- [→ Aplicar em Otimização de Código](../otimizacao/guia_completo.md)
- [→ Referência Rápida de Otimização](../otimizacao/referencia_rapida.md)
- [→ Executar Exemplos Práticos](https://github.com/DougFelipe/zen-python/blob/main/src/zen_python_exemplos.py)

