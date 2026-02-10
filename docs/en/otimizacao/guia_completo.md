# Complete Guide: Python Code Optimization

> **Navigation:** [← Back to Home](../index.md) | [Quick Reference →](referencia_rapida.md) | [Zen of Python →](../zen/teoria.md)

## Table of Contents
1. [List Operations](#1-list-operations)
2. [Search and Element Verification](#2-search-and-element-verification)
3. [Itertools for Complex Iterations](#3-itertools-for-complex-iterations)
4. [Set Operations](#4-set-operations)
5. [Strings and Joins](#5-strings-and-joins)
6. [Comprehensions vs Loops](#6-comprehensions-vs-loops)
7. [Built-in Functions for Aggregation](#7-built-in-functions-for-aggregation)
8. [Special Cases and Trade-offs](#8-special-cases-and-trade-offs)

---

## 1. List Operations

### ❌ Less Optimized: Append in Loop
```python
# Creating a list with squared elements
resultado = []
for i in range(1000):
    resultado.append(i ** 2)
```

### ✅ More Optimized: List Comprehension
```python
resultado = [i ** 2 for i in range(1000)]
```

**Why is it better?**

- List comprehension is optimized in C in CPython
- Reduces overhead of `.append()` method calls
- ~30% faster on average

**Trade-offs:**

- Less readable for very complex operations
- Consumes memory all at once (consider generator expressions for large volumes)

**Use case:** Simple list transformations, filtering, and mapping

---

### ❌ Less Optimized: Repeated Concatenation
```python
resultado = []
for item in lista1:
    resultado.append(item)
for item in lista2:
    resultado.append(item)
```

### ✅ More Optimized: Extend or + Operator
```python
# Option 1: extend
resultado = []
resultado.extend(lista1)
resultado.extend(lista2)

# Option 2: + operator (creates a new list)
resultado = lista1 + lista2

# Option 3: itertools.chain (lazy, does not create an intermediate list)
from itertools import chain
resultado = list(chain(lista1, lista2))
```

**Trade-offs:**

- `extend`: modifies in-place, more memory efficient
- `+`: creates a new list, more functional
- `chain`: best for single iteration without materializing the list

---

## 2. Search and Element Verification

### ❌ Less Optimized: Search in List with Loop
```python
def item_existe(lista, item):
    for elemento in lista:
        if elemento == item:
            return True
    return False

# Usage
if item_existe(minha_lista, 'valor'):
    print("Found")
```

### ✅ More Optimized: `in` Operator with Set
```python
# Convert to set once
meu_set = set(minha_lista)

# O(1) lookup vs O(n)
if 'valor' in meu_set:
    print("Found")
```

**Complexity:**

- List: O(n) - potentially needs to traverse all elements
- Set: O(1) - direct access via hash

**Trade-offs:**

- Set consumes more memory (~3x more than list)
- Set does not maintain order (use dict if order matters, Python 3.7+)
- Initial conversion has O(n) cost

**Use case:** When you perform multiple lookups on the same collection

---

### ❌ Less Optimized: Removing Duplicates with Loop
```python
unicos = []
for item in lista:
    if item not in unicos:
        unicos.append(item)
```

### ✅ More Optimized: Direct Set
```python
# Without preserving order
unicos = list(set(lista))

# Preserving order (Python 3.7+)
unicos = list(dict.fromkeys(lista))
```

**Performance:**

- Loop with `in`: O(n²)
- Set: O(n)

---

## 3. Itertools for Complex Iterations

### ❌ Less Optimized: Nested Loops for Combinations
```python
# Cartesian product
resultado = []
for a in lista1:
    for b in lista2:
        for c in lista3:
            resultado.append((a, b, c))
```

### ✅ More Optimized: itertools.product
```python
from itertools import product

resultado = list(product(lista1, lista2, lista3))
```

**Advantages:**

- Cleaner and more declarative code
- Optimized implementation in C
- Lazy evaluation (does not consume memory until needed)

---

### ❌ Less Optimized: Manual Grouping
```python
# Group by category
grupos = {}
for item in lista:
    categoria = item['categoria']
    if categoria not in grupos:
        grupos[categoria] = []
    grupos[categoria].append(item)
```

### ✅ More Optimized: itertools.groupby
```python
from itertools import groupby
from operator import itemgetter

# Important: list must be sorted by the key
lista_ordenada = sorted(lista, key=itemgetter('categoria'))
grupos = {k: list(v) for k, v in groupby(lista_ordenada, key=itemgetter('categoria'))}
```

**Alternative:** `collections.defaultdict`
```python
from collections import defaultdict

grupos = defaultdict(list)
for item in lista:
    grupos[item['categoria']].append(item)
```

**Trade-offs:**

- `groupby`: requires prior sorting, more efficient for already sorted data
- `defaultdict`: does not require sorting, more intuitive

---

### Other Useful Itertools Functions

```python
from itertools import (
    combinations,      # Combinations without repetition
    permutations,      # Permutations
    accumulate,        # Cumulative sum/operation
    islice,           # Slice iterators
    chain,            # Concatenate iterators
    takewhile,        # Take while condition is true
    dropwhile,        # Drop while condition is true
    compress,         # Filter by boolean selector
    zip_longest       # Zip that does not stop at the shortest
)

# Examples
list(combinations([1, 2, 3], 2))  # [(1,2), (1,3), (2,3)]
list(accumulate([1, 2, 3, 4]))    # [1, 3, 6, 10]
list(islice(range(100), 10, 20))  # [10, 11, ..., 19]
```

---

## 4. Set Operations

### ❌ Less Optimized: Intersection with Loops
```python
comuns = []
for item in lista1:
    if item in lista2:
        if item not in comuns:
            comuns.append(item)
```

### ✅ More Optimized: Set Operations
```python
# Intersection
comuns = list(set(lista1) & set(lista2))
# or
comuns = list(set(lista1).intersection(lista2))

# Union
todos = list(set(lista1) | set(lista2))
# or
todos = list(set(lista1).union(lista2))

# Difference (in lista1 but not in lista2)
diff = list(set(lista1) - set(lista2))

# Symmetric difference (in one but not in both)
diff_sim = list(set(lista1) ^ set(lista2))
```

**Performance:** O(n + m) vs O(n × m) with loops

**Set Operators:**

- `&` or `.intersection()`: elements in both
- `|` or `.union()`: elements in either
- `-` or `.difference()`: elements in the first but not in the second
- `^` or `.symmetric_difference()`: elements in one but not in both

---

### Efficient Checks with Sets

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Check if it is a subset
set1.issubset(set2)      # False
set1 <= set2             # False

# Check if it is a superset
set1.issuperset({1, 2})  # True
set1 >= {1, 2}           # True

# Check if they are disjoint (no common elements)
set1.isdisjoint({7, 8})  # True
```

---

## 5. Strings and Joins

### ❌ Less Optimized: Concatenation with +
```python
# NEVER do this in loops!
resultado = ""
for palavra in lista_palavras:
    resultado = resultado + palavra + " "
```

**Why is it bad?**

- Strings are immutable in Python
- Each concatenation creates a new string
- O(n²) complexity due to repeated copies

### ✅ More Optimized: Join
```python
resultado = " ".join(lista_palavras)
```

**Performance:** O(n) - allocates memory once and copies all elements

---

### Specific String Cases

```python
# Build a string with formatting
# ❌ Less optimized
texto = ""
for i, item in enumerate(items):
    texto += f"{i}: {item}\n"

# ✅ More optimized
texto = "\n".join(f"{i}: {item}" for i, item in enumerate(items))

# For many operations: use io.StringIO
from io import StringIO

buffer = StringIO()
for item in items:
    buffer.write(f"{item}\n")
resultado = buffer.getvalue()
```

---

## 6. Comprehensions vs Loops

### List Comprehension vs Loop

```python
# ❌ Less optimized
quadrados = []
for x in range(100):
    if x % 2 == 0:
        quadrados.append(x ** 2)

# ✅ More optimized
quadrados = [x ** 2 for x in range(100) if x % 2 == 0]
```

### Dict Comprehension

```python
# ❌ Less optimized
mapa = {}
for item in items:
    mapa[item.id] = item.valor

# ✅ More optimized
mapa = {item.id: item.valor for item in items}
```

### Set Comprehension

```python
# ❌ Less optimized
unicos = set()
for item in items:
    if item > 0:
        unicos.add(item)

# ✅ More optimized
unicos = {item for item in items if item > 0}
```

### Generator Expression (For Large Volumes)

```python
# List comprehension: creates the full list in memory
quadrados = [x ** 2 for x in range(1000000)]

# Generator: computes on demand
quadrados = (x ** 2 for x in range(1000000))

# Usage
for quad in quadrados:
    print(quad)  # Computes only when needed
```

**Trade-offs:**

- Generator: constant memory O(1), cannot be reused
- List: O(n) memory, can iterate multiple times

---

## 7. Built-in Functions for Aggregation

### ❌ Less Optimized: Loops for Aggregations
```python
# Sum
total = 0
for num in numeros:
    total += num

# Maximum
maximo = numeros[0]
for num in numeros:
    if num > maximo:
        maximo = num

# Minimum
minimo = numeros[0]
for num in numeros:
    if num < minimo:
        minimo = num
```

### ✅ More Optimized: Built-ins
```python
total = sum(numeros)
maximo = max(numeros)
minimo = min(numeros)

# With key function
pessoa_mais_velha = max(pessoas, key=lambda p: p.idade)

# Min and max together
from statistics import mean, median
menor, maior = min(numeros), max(numeros)
media = mean(numeros)
mediana = median(numeros)
```

---

### Map, Filter, and Reduce

```python
# ❌ Less optimized
dobrados = []
for x in numeros:
    dobrados.append(x * 2)

# ✅ Option 1: List comprehension (generally preferred)
dobrados = [x * 2 for x in numeros]

# ✅ Option 2: Map (when applying an existing function)
dobrados = list(map(lambda x: x * 2, numeros))
# Even better with a named function
def dobrar(x):
    return x * 2
dobrados = list(map(dobrar, numeros))
```

```python
# Filter
# ❌ Less optimized
pares = []
for x in numeros:
    if x % 2 == 0:
        pares.append(x)

# ✅ Option 1: List comprehension
pares = [x for x in numeros if x % 2 == 0]

# ✅ Option 2: Filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
```

```python
# Reduce (for complex cumulative operations)
from functools import reduce

# Product of all elements
produto = reduce(lambda x, y: x * y, numeros, 1)

# More readable alternative for simple cases
from operator import mul
produto = reduce(mul, numeros, 1)
```

**When to use each:**

- **List comprehension**: default choice, most Pythonic
- **Map**: when applying an existing complex function
- **Filter**: when the condition is a complex named function
- **Reduce**: cumulative operations that have no built-in

---

## 8. Special Cases and Trade-offs

### When NOT to Optimize Prematurely

```python
# For small lists (<100 elements), the difference is negligible
# ❌ Over-engineering
pequena_lista = [1, 2, 3, 4, 5]
set_pequeno = set(pequena_lista)  # Unnecessary overhead

# ✅ Simpler
if 3 in pequena_lista:
    pass
```

---

### Counters and Frequencies

```python
# ❌ Less optimized
contagem = {}
for item in lista:
    if item in contagem:
        contagem[item] += 1
    else:
        contagem[item] = 1

# ✅ Option 1: get() with default
contagem = {}
for item in lista:
    contagem[item] = contagem.get(item, 0) + 1

# ✅ Option 2: defaultdict
from collections import defaultdict
contagem = defaultdict(int)
for item in lista:
    contagem[item] += 1

# ✅ Option 3: Counter (BEST for counting)
from collections import Counter
contagem = Counter(lista)

# Useful Counter methods
contagem.most_common(3)      # 3 most common
contagem['item']             # Returns 0 if it does not exist
contagem1 + contagem2        # Sum counters
```

---

### Any and All (Short-Circuit Evaluation)

```python
# ❌ Less optimized
tem_positivo = False
for num in numeros:
    if num > 0:
        tem_positivo = True
        break

# ✅ More optimized
tem_positivo = any(num > 0 for num in numeros)

# ❌ Less optimized
todos_positivos = True
for num in numeros:
    if num <= 0:
        todos_positivos = False
        break

# ✅ More optimized
todos_positivos = all(num > 0 for num in numeros)
```

**Advantage:** Stops when it finds the first True/False, does not process the rest

---

### Enumerate Instead of Range + Index

```python
# ❌ Less optimized
for i in range(len(lista)):
    print(f"{i}: {lista[i]}")

# ✅ More optimized
for i, item in enumerate(lista):
    print(f"{i}: {item}")

# With a different starting index
for i, item in enumerate(lista, start=1):
    print(f"{i}: {item}")
```

---

### Zip for Parallel Iteration

```python
# ❌ Less optimized
for i in range(len(nomes)):
    print(f"{nomes[i]}: {idades[i]}")

# ✅ More optimized
for nome, idade in zip(nomes, idades):
    print(f"{nome}: {idade}")

# For lists of different sizes
from itertools import zip_longest
for nome, idade in zip_longest(nomes, idades, fillvalue='N/A'):
    print(f"{nome}: {idade}")
```

---

### Walrus Operator (:=) - Python 3.8+

```python
# ❌ Double evaluation
if len(lista) > 10:
    tamanho = len(lista)
    print(f"Large list: {tamanho}")

# ✅ With walrus operator
if (tamanho := len(lista)) > 10:
    print(f"Large list: {tamanho}")

# Useful in list comprehensions
# ❌ Computes twice
resultado = [calcular(x) for x in dados if calcular(x) > 10]

# ✅ Computes once
resultado = [y for x in dados if (y := calcular(x)) > 10]
```

---

## Performance Summary

| Operation | Less Optimized | More Optimized | Typical Gain |
|-----------|---------------|----------------|--------------|
| Search | `for` in list O(n) | `in` set O(1) | ~100x+ |
| String concatenation | `+` in loop O(n²) | `join()` O(n) | ~10-100x |
| Duplicate removal | loop with `in` O(n²) | `set()` O(n) | ~50x+ |
| List transformation | `for` + `append()` | list comprehension | ~30% |
| List intersection | nested loops O(n×m) | set operations O(n+m) | ~10-50x |
| Aggregations | manual loops | `sum()`, `max()`, etc | ~20-40% |

---

## General Optimization Principles

### 1. Use appropriate data structures

- Frequent search/verification → Set/Dict
- Order matters → List/Deque
- Counting → Counter
- Grouping → defaultdict

### 2. Prefer built-ins and stdlib

- Implemented in C, highly optimized
- Well tested and maintained

### 3. Avoid unnecessary work

- Use lazy evaluation (generators) when possible
- Short-circuit evaluation with `any()`/`all()`
- Cache results when appropriate

### 4. Readability vs Performance

- For <1000 elements, prefer readable code
- Optimize only identified bottlenecks (profile first!)
- Use comprehensions when they improve readability

### 5. Measurement

```python
import timeit

# Measure time
tempo = timeit.timeit('sum(range(100))', number=10000)

# Compare alternatives
print(timeit.timeit('[x**2 for x in range(100)]', number=10000))
print(timeit.timeit('list(map(lambda x: x**2, range(100)))', number=10000))
```

---

## Profiling Tools

```python
# cProfile for detailed analysis
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()
# your code here
profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10 functions

# line_profiler for line-by-line analysis
# pip install line_profiler
# @profile decorator and run: kernprof -l -v script.py

# memory_profiler for memory usage
# pip install memory_profiler
# @profile decorator and run: python -m memory_profiler script.py
```

---

## Conclusion

Optimization in Python involves knowing the right tools for each job. The main guidelines are:

- **Sets** for membership and set operations
- **Comprehensions** for transformations and filtering
- **Itertools** for complex iterations
- **Join** for string concatenation
- **Built-ins** for aggregations
- **Generators** for large data volumes

Remember: **measure before optimizing!** Code readability and maintainability are more important than micro-optimizations in non-critical code.

---

## Next Steps

- [→ Quick Reference (Cheat Sheet)](referencia_rapida.md)
- [→ Run Benchmarks](https://github.com/DougFelipe/zen-python/blob/main/src/exemplos_otimizacao.py)
- [← Learn the Zen of Python (Theory)](../zen/teoria.md)
- [← Practical Zen Examples](../zen/pratica_parte1.md)
