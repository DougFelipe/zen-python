# 🚀 Guia de Referência Rápida - Otimização Python

> **Navegação:** [← Voltar ao Início](../index.md) | [← Guia Completo](guia_completo.md) | [Zen do Python →](../zen/teoria.md)

## 📋 Cheat Sheet de Substituições

### Busca e Verificação
```python
# ❌ Evite                          # ✅ Use
if x in lista:                      if x in set_items:
[x for x in lista if x == valor]   next((x for x in lista if x == valor), None)
```

### Strings
```python
# ❌ Evite                          # ✅ Use
s = s + "texto"                     partes = []; partes.append("texto"); s = "".join(partes)
resultado = ""                      resultado = " ".join(lista_palavras)
for p in palavras: s += p
```

### Listas
```python
# ❌ Evite                          # ✅ Use
r = []                              r = [x**2 for x in range(100)]
for i in range(100):
    r.append(i**2)

unicos = []                         unicos = list(set(lista))
for x in lista:                     # ou
    if x not in unicos:             unicos = list(dict.fromkeys(lista))  # preserva ordem
        unicos.append(x)
```

### Agregações
```python
# ❌ Evite                          # ✅ Use
total = 0                           total = sum(numeros)
for n in numeros:
    total += n

maior = numeros[0]                  maior = max(numeros)
for n in numeros:                   menor = min(numeros)
    if n > maior:
        maior = n
```

### Iteração
```python
# ❌ Evite                          # ✅ Use
for i in range(len(lista)):        for i, item in enumerate(lista):
    print(i, lista[i])                  print(i, item)

for i in range(len(l1)):           for a, b in zip(l1, l2):
    print(l1[i], l2[i])                 print(a, b)

tem_pos = False                     tem_pos = any(n > 0 for n in nums)
for n in nums:                      todos_pos = all(n > 0 for n in nums)
    if n > 0:
        tem_pos = True
```

### Conjuntos
```python
# ❌ Evite                          # ✅ Use
comuns = []                         comuns = list(set(l1) & set(l2))
for x in l1:                        todos = list(set(l1) | set(l2))
    if x in l2:                     diff = list(set(l1) - set(l2))
        comuns.append(x)
```

### Contagem
```python
# ❌ Evite                          # ✅ Use
cont = {}                           from collections import Counter
for item in lista:                  cont = Counter(lista)
    if item in cont:                cont.most_common(3)
        cont[item] += 1
    else:
        cont[item] = 1
```

### Agrupamento
```python
# ❌ Evite                          # ✅ Use
grupos = {}                         from collections import defaultdict
for item in lista:                  grupos = defaultdict(list)
    cat = item['cat']               for item in lista:
    if cat not in grupos:               grupos[item['cat']].append(item)
        grupos[cat] = []
    grupos[cat].append(item)
```

---

## 🎯 Quando Usar Cada Estrutura

| Necessidade | Use | Complexidade | Memória |
|-------------|-----|--------------|---------|
| Busca rápida | `set` ou `dict` | O(1) | Alta |
| Ordem + busca | `list` | O(n) | Baixa |
| Ordem + busca rápida | `dict` (Python 3.7+) | O(1) | Alta |
| Contagem | `Counter` | O(1) lookup | Média |
| Valores padrão | `defaultdict` | O(1) | Média |
| Fila (FIFO) | `deque` | O(1) | Baixa |
| Pilha (LIFO) | `list` (append/pop) | O(1) | Baixa |

---

## ⚡ Módulos Essenciais

### itertools
```python
from itertools import (
    product,        # Produto cartesiano: product([1,2], ['a','b']) → (1,'a'), (1,'b'), (2,'a'), (2,'b')
    combinations,   # Combinações: combinations([1,2,3], 2) → (1,2), (1,3), (2,3)
    permutations,   # Permutações: permutations([1,2,3], 2) → (1,2), (1,3), (2,1), (2,3), (3,1), (3,2)
    chain,          # Concatenar: chain([1,2], [3,4]) → 1, 2, 3, 4
    groupby,        # Agrupar: groupby(sorted_list, key=func)
    accumulate,     # Acumulado: accumulate([1,2,3,4]) → 1, 3, 6, 10
    islice,         # Slice: islice(range(100), 10, 20) → 10...19
    takewhile,      # Enquanto: takewhile(lambda x: x<5, [1,4,6,3]) → 1, 4
    compress,       # Filtrar: compress([1,2,3], [1,0,1]) → 1, 3
)
```

### collections
```python
from collections import (
    Counter,        # Contagem: Counter(['a','b','a']) → {'a': 2, 'b': 1}
    defaultdict,    # Dict com default: defaultdict(list)
    deque,          # Fila dupla: deque.append(), deque.popleft()
    OrderedDict,    # Dict ordenado (< Python 3.7)
    namedtuple,     # Tuple nomeada: Point = namedtuple('Point', ['x', 'y'])
    ChainMap,       # Múltiplos dicts: ChainMap(dict1, dict2)
)
```

### functools
```python
from functools import (
    reduce,         # Reduzir: reduce(lambda x,y: x+y, [1,2,3,4]) → 10
    lru_cache,      # Cache: @lru_cache(maxsize=128)
    partial,        # Aplicação parcial: add5 = partial(add, 5)
    wraps,          # Decoradores: @wraps(func)
)
```

### operator
```python
from operator import (
    itemgetter,     # Pegar item: sorted(lista, key=itemgetter('name'))
    attrgetter,     # Pegar atributo: sorted(objs, key=attrgetter('age'))
    methodcaller,   # Chamar método: map(methodcaller('strip'), strings)
    mul, add,       # Operadores: reduce(mul, [1,2,3,4]) → 24
)
```

---

## 📊 Complexidade de Operações

### List
| Operação | Complexidade |
|----------|--------------|
| `list[i]` | O(1) |
| `list.append(x)` | O(1) amortizado |
| `list.insert(i, x)` | O(n) |
| `list.pop()` | O(1) |
| `list.pop(i)` | O(n) |
| `x in list` | O(n) |
| `list.sort()` | O(n log n) |

### Set / Dict
| Operação | Complexidade |
|----------|--------------|
| `x in set` | O(1) |
| `set.add(x)` | O(1) |
| `set.remove(x)` | O(1) |
| `dict[key]` | O(1) |
| `dict[key] = value` | O(1) |

### Deque
| Operação | Complexidade |
|----------|--------------|
| `deque.append(x)` | O(1) |
| `deque.appendleft(x)` | O(1) |
| `deque.pop()` | O(1) |
| `deque.popleft()` | O(1) |

---

## 🔧 Ferramentas de Profiling

### Timing
```python
import timeit

# Comparar funções
t1 = timeit.timeit('sum(range(100))', number=10000)
t2 = timeit.timeit('[x for x in range(100)]', number=10000)

# Com setup
timeit.timeit('x in s', setup='s = set(range(1000)); x = 999', number=10000)
```

### cProfile
```python
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()
# código aqui
profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)
```

### memory_profiler
```bash
pip install memory_profiler

# No código
@profile
def minha_funcao():
    ...

# Executar
python -m memory_profiler script.py
```

### line_profiler
```bash
pip install line_profiler

# No código
@profile
def minha_funcao():
    ...

# Executar
kernprof -l -v script.py
```

---

## 💡 Regras de Ouro

1. **Meça antes de otimizar** - Use profilers para identificar gargalos
2. **Use a estrutura de dados certa** - Set para busca, List para ordem
3. **Prefira built-ins** - São otimizados em C
4. **Evite loops aninhados** - Use operações de conjunto
5. **Use comprehensions** - Mais rápidas que loops
6. **Join para strings** - Nunca concatene com + em loop
7. **Generator para grandes volumes** - Economiza memória
8. **Cache quando apropriado** - @lru_cache para funções puras
9. **Legibilidade primeiro** - Otimize apenas gargalos
10. **Documente trade-offs** - Explique decisões de otimização

---

## 🎨 Padrões Comuns

### Pipeline de Processamento
```python
# Processar dados em etapas
from itertools import islice

dados = carrega_dados()  # Generator
filtrados = (x for x in dados if x > 0)  # Generator
transformados = (x ** 2 for x in filtrados)  # Generator
top_10 = list(islice(transformados, 10))  # Materializa apenas 10
```

### Memoização
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### Processamento de Lote
```python
def processar_lotes(iterable, tamanho_lote=1000):
    """Processa iterável em lotes"""
    from itertools import islice
    iterator = iter(iterable)
    while True:
        lote = list(islice(iterator, tamanho_lote))
        if not lote:
            break
        yield lote

# Uso
for lote in processar_lotes(grande_lista):
    processar(lote)
```

### Defaultdict com Lambda
```python
from collections import defaultdict

# Contador aninhado
contador = defaultdict(lambda: defaultdict(int))
contador['categoria']['item'] += 1

# Lista de listas
grupos = defaultdict(list)
for item in items:
    grupos[item.categoria].append(item)
```

---

## 🚫 Anti-padrões

```python
# ❌ NUNCA faça isso
resultado = ""
for s in strings:
    resultado += s  # O(n²)

# ❌ NUNCA faça isso
for i in range(len(lista)):
    print(lista[i])  # Use enumerate

# ❌ NUNCA faça isso
if x == 'a' or x == 'b' or x == 'c':
    pass  # Use: if x in {'a', 'b', 'c'}

# ❌ NUNCA faça isso
dict = {}
dict['key'] = dict.get('key', 0) + 1  # Use Counter ou defaultdict

# ❌ NUNCA faça isso em loops
if not minha_lista:  # Verificação de vazio
    pass
# Dentro de um loop onde minha_lista não muda
```

---

## 📖 Referências

- [Python Time Complexity](https://wiki.python.org/moin/TimeComplexity)
- [itertools docs](https://docs.python.org/3/library/itertools.html)
- [collections docs](https://docs.python.org/3/library/collections.html)
- [functools docs](https://docs.python.org/3/library/functools.html)
- [Python Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)

---

## 📚 Documentos Relacionados

- [← Guia Completo de Otimização](guia_completo.md) - Explicações detalhadas com exemplos
- [→ Executar Benchmarks](https://github.com/DougFelipe/zen-python/blob/main/src/exemplos_otimizacao.py) - Código executável com métricas
- [→ Zen do Python (Teoria)](../zen/teoria.md) - Filosofia por trás das boas práticas
- [→ Zen do Python (Prática)](../zen/pratica_parte1.md) - Exemplos práticos dos princípios

