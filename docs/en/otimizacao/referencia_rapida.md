# 🚀 Quick Reference Guide - Python Optimization

> **Navigation:** [← Back to Home](../index.md) | [← Complete Guide](guia_completo.md) | [Zen of Python →](../zen/teoria.md)

## 📋 Substitution Cheat Sheet

### Search and Verification
```python
# ❌ Avoid                            # ✅ Use
if x in lista:                      if x in set_items:
[x for x in lista if x == valor]   next((x for x in lista if x == valor), None)
```

### Strings
```python
# ❌ Avoid                            # ✅ Use
s = s + "texto"                     partes = []; partes.append("texto"); s = "".join(partes)
resultado = ""                      resultado = " ".join(lista_palavras)
for p in palavras: s += p
```

### Lists
```python
# ❌ Avoid                            # ✅ Use
r = []                              r = [x**2 for x in range(100)]
for i in range(100):
    r.append(i**2)

unicos = []                         unicos = list(set(lista))
for x in lista:                     # or
    if x not in unicos:             unicos = list(dict.fromkeys(lista))  # preserves order
        unicos.append(x)
```

### Aggregations
```python
# ❌ Avoid                            # ✅ Use
total = 0                           total = sum(numeros)
for n in numeros:
    total += n

maior = numeros[0]                  maior = max(numeros)
for n in numeros:                   menor = min(numeros)
    if n > maior:
        maior = n
```

### Iteration
```python
# ❌ Avoid                            # ✅ Use
for i in range(len(lista)):        for i, item in enumerate(lista):
    print(i, lista[i])                  print(i, item)

for i in range(len(l1)):           for a, b in zip(l1, l2):
    print(l1[i], l2[i])                 print(a, b)

tem_pos = False                     tem_pos = any(n > 0 for n in nums)
for n in nums:                      todos_pos = all(n > 0 for n in nums)
    if n > 0:
        tem_pos = True
```

### Sets
```python
# ❌ Avoid                            # ✅ Use
comuns = []                         comuns = list(set(l1) & set(l2))
for x in l1:                        todos = list(set(l1) | set(l2))
    if x in l2:                     diff = list(set(l1) - set(l2))
        comuns.append(x)
```

### Counting
```python
# ❌ Avoid                            # ✅ Use
cont = {}                           from collections import Counter
for item in lista:                  cont = Counter(lista)
    if item in cont:                cont.most_common(3)
        cont[item] += 1
    else:
        cont[item] = 1
```

### Grouping
```python
# ❌ Avoid                            # ✅ Use
grupos = {}                         from collections import defaultdict
for item in lista:                  grupos = defaultdict(list)
    cat = item['cat']               for item in lista:
    if cat not in grupos:               grupos[item['cat']].append(item)
        grupos[cat] = []
    grupos[cat].append(item)
```

---

## 🎯 When to Use Each Structure

| Need | Use | Complexity | Memory |
|------|-----|------------|--------|
| Fast lookup | `set` or `dict` | O(1) | High |
| Order + lookup | `list` | O(n) | Low |
| Order + fast lookup | `dict` (Python 3.7+) | O(1) | High |
| Counting | `Counter` | O(1) lookup | Medium |
| Default values | `defaultdict` | O(1) | Medium |
| Queue (FIFO) | `deque` | O(1) | Low |
| Stack (LIFO) | `list` (append/pop) | O(1) | Low |

---

## ⚡ Essential Modules

### itertools
```python
from itertools import (
    product,        # Cartesian product: product([1,2], ['a','b']) → (1,'a'), (1,'b'), (2,'a'), (2,'b')
    combinations,   # Combinations: combinations([1,2,3], 2) → (1,2), (1,3), (2,3)
    permutations,   # Permutations: permutations([1,2,3], 2) → (1,2), (1,3), (2,1), (2,3), (3,1), (3,2)
    chain,          # Concatenate: chain([1,2], [3,4]) → 1, 2, 3, 4
    groupby,        # Group: groupby(sorted_list, key=func)
    accumulate,     # Accumulate: accumulate([1,2,3,4]) → 1, 3, 6, 10
    islice,         # Slice: islice(range(100), 10, 20) → 10...19
    takewhile,      # While: takewhile(lambda x: x<5, [1,4,6,3]) → 1, 4
    compress,       # Filter: compress([1,2,3], [1,0,1]) → 1, 3
)
```

### collections
```python
from collections import (
    Counter,        # Counting: Counter(['a','b','a']) → {'a': 2, 'b': 1}
    defaultdict,    # Dict with default: defaultdict(list)
    deque,          # Double-ended queue: deque.append(), deque.popleft()
    OrderedDict,    # Ordered dict (< Python 3.7)
    namedtuple,     # Named tuple: Point = namedtuple('Point', ['x', 'y'])
    ChainMap,       # Multiple dicts: ChainMap(dict1, dict2)
)
```

### functools
```python
from functools import (
    reduce,         # Reduce: reduce(lambda x,y: x+y, [1,2,3,4]) → 10
    lru_cache,      # Cache: @lru_cache(maxsize=128)
    partial,        # Partial application: add5 = partial(add, 5)
    wraps,          # Decorators: @wraps(func)
)
```

### operator
```python
from operator import (
    itemgetter,     # Get item: sorted(lista, key=itemgetter('name'))
    attrgetter,     # Get attribute: sorted(objs, key=attrgetter('age'))
    methodcaller,   # Call method: map(methodcaller('strip'), strings)
    mul, add,       # Operators: reduce(mul, [1,2,3,4]) → 24
)
```

---

## 📊 Operation Complexity

### List
| Operation | Complexity |
|-----------|------------|
| `list[i]` | O(1) |
| `list.append(x)` | O(1) amortized |
| `list.insert(i, x)` | O(n) |
| `list.pop()` | O(1) |
| `list.pop(i)` | O(n) |
| `x in list` | O(n) |
| `list.sort()` | O(n log n) |

### Set / Dict
| Operation | Complexity |
|-----------|------------|
| `x in set` | O(1) |
| `set.add(x)` | O(1) |
| `set.remove(x)` | O(1) |
| `dict[key]` | O(1) |
| `dict[key] = value` | O(1) |

### Deque
| Operation | Complexity |
|-----------|------------|
| `deque.append(x)` | O(1) |
| `deque.appendleft(x)` | O(1) |
| `deque.pop()` | O(1) |
| `deque.popleft()` | O(1) |

---

## 🔧 Profiling Tools

### Timing
```python
import timeit

# Compare functions
t1 = timeit.timeit('sum(range(100))', number=10000)
t2 = timeit.timeit('[x for x in range(100)]', number=10000)

# With setup
timeit.timeit('x in s', setup='s = set(range(1000)); x = 999', number=10000)
```

### cProfile
```python
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()
# code here
profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)
```

### memory_profiler
```bash
pip install memory_profiler

# In the code
@profile
def my_function():
    ...

# Run
python -m memory_profiler script.py
```

### line_profiler
```bash
pip install line_profiler

# In the code
@profile
def my_function():
    ...

# Run
kernprof -l -v script.py
```

---

## 💡 Golden Rules

1. **Measure before optimizing** - Use profilers to identify bottlenecks
2. **Use the right data structure** - Set for lookup, List for order
3. **Prefer built-ins** - They are optimized in C
4. **Avoid nested loops** - Use set operations
5. **Use comprehensions** - Faster than loops
6. **Join for strings** - Never concatenate with + in a loop
7. **Generator for large volumes** - Saves memory
8. **Cache when appropriate** - @lru_cache for pure functions
9. **Readability first** - Optimize only bottlenecks
10. **Document trade-offs** - Explain optimization decisions

---

## 🎨 Common Patterns

### Processing Pipeline
```python
# Process data in stages
from itertools import islice

dados = carrega_dados()  # Generator
filtrados = (x for x in dados if x > 0)  # Generator
transformados = (x ** 2 for x in filtrados)  # Generator
top_10 = list(islice(transformados, 10))  # Materializes only 10
```

### Memoization
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### Batch Processing
```python
def processar_lotes(iterable, tamanho_lote=1000):
    """Processes an iterable in batches"""
    from itertools import islice
    iterator = iter(iterable)
    while True:
        lote = list(islice(iterator, tamanho_lote))
        if not lote:
            break
        yield lote

# Usage
for lote in processar_lotes(grande_lista):
    processar(lote)
```

### Defaultdict with Lambda
```python
from collections import defaultdict

# Nested counter
contador = defaultdict(lambda: defaultdict(int))
contador['categoria']['item'] += 1

# List of lists
grupos = defaultdict(list)
for item in items:
    grupos[item.categoria].append(item)
```

---

## 🚫 Anti-patterns

```python
# ❌ NEVER do this
resultado = ""
for s in strings:
    resultado += s  # O(n²)

# ❌ NEVER do this
for i in range(len(lista)):
    print(lista[i])  # Use enumerate

# ❌ NEVER do this
if x == 'a' or x == 'b' or x == 'c':
    pass  # Use: if x in {'a', 'b', 'c'}

# ❌ NEVER do this
dict = {}
dict['key'] = dict.get('key', 0) + 1  # Use Counter or defaultdict

# ❌ NEVER do this in loops
if not minha_lista:  # Empty check
    pass
# Inside a loop where minha_lista does not change
```

---

## 📖 References

- [Python Time Complexity](https://wiki.python.org/moin/TimeComplexity)
- [itertools docs](https://docs.python.org/3/library/itertools.html)
- [collections docs](https://docs.python.org/3/library/collections.html)
- [functools docs](https://docs.python.org/3/library/functools.html)
- [Python Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)

---

## 📚 Related Documents

- [← Complete Optimization Guide](guia_completo.md) - Detailed explanations with examples
- [→ Run Benchmarks](https://github.com/DougFelipe/zen-python/blob/main/src/exemplos_otimizacao.py) - Executable code with metrics
- [→ Zen of Python (Theory)](../zen/teoria.md) - Philosophy behind best practices
- [→ Zen of Python (Practice)](../zen/pratica_parte1.md) - Practical examples of the principles
