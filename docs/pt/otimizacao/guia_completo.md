# Guia Completo: Otimização de Código Python

> **Navegação:** [← Voltar ao Início](../index.md) | [Referência Rápida →](referencia_rapida.md) | [Zen do Python →](../zen/teoria.md)

## Sumário
1. [Operações com Listas](#1-operacoes-com-listas)
2. [Busca e Verificação de Elementos](#2-busca-e-verificacao-de-elementos)
3. [Itertools para Iterações Complexas](#3-itertools-para-iteracoes-complexas)
4. [Operações de Conjunto (Sets)](#4-operacoes-de-conjunto-sets)
5. [Strings e Joins](#5-strings-e-joins)
6. [Comprehensions vs Loops](#6-comprehensions-vs-loops)
7. [Funções Built-in para Agregação](#7-funcoes-built-in-para-agregacao)
8. [Casos Especiais e Trade-offs](#8-casos-especiais-e-trade-offs)

---

## 1. Operações com Listas

### ❌ Menos Otimizado: Append em Loop
```python
# Criando lista com elementos ao quadrado
resultado = []
for i in range(1000):
    resultado.append(i ** 2)
```

### ✅ Mais Otimizado: List Comprehension
```python
resultado = [i ** 2 for i in range(1000)]
```

**Por quê é melhor?**

- List comprehension é otimizada em C no CPython
- Reduz overhead de chamadas de método `.append()`
- ~30% mais rápido em média

**Trade-offs:**

- Menos legível para operações muito complexas
- Consome memória de uma vez (considere generator expressions para grandes volumes)

**Caso de uso:** Transformações simples de listas, filtragem e mapeamento

---

### ❌ Menos Otimizado: Concatenação Repetida
```python
resultado = []
for item in lista1:
    resultado.append(item)
for item in lista2:
    resultado.append(item)
```

### ✅ Mais Otimizado: Extend ou Operador +
```python
# Opção 1: extend
resultado = []
resultado.extend(lista1)
resultado.extend(lista2)

# Opção 2: operador + (cria nova lista)
resultado = lista1 + lista2

# Opção 3: itertools.chain (lazy, não cria lista intermediária)
from itertools import chain
resultado = list(chain(lista1, lista2))
```

**Trade-offs:**

- `extend`: modifica in-place, mais eficiente em memória
- `+`: cria nova lista, mais funcional
- `chain`: melhor para iteração única sem materializar a lista

---

## 2. Busca e Verificação de Elementos

### ❌ Menos Otimizado: Busca em Lista com Loop
```python
def item_existe(lista, item):
    for elemento in lista:
        if elemento == item:
            return True
    return False

# Uso
if item_existe(minha_lista, 'valor'):
    print("Encontrado")
```

### ✅ Mais Otimizado: Operador `in` com Set
```python
# Converter para set uma vez
meu_set = set(minha_lista)

# Busca O(1) vs O(n)
if 'valor' in meu_set:
    print("Encontrado")
```

**Complexidade:**

- Lista: O(n) - precisa percorrer potencialmente todos elementos
- Set: O(1) - acesso direto via hash

**Trade-offs:**

- Set consome mais memória (~3x mais que lista)
- Set não mantém ordem (use dict se ordem importa, Python 3.7+)
- Conversão inicial tem custo O(n)

**Caso de uso:** Quando você faz múltiplas buscas na mesma coleção

---

### ❌ Menos Otimizado: Remoção de Duplicatas com Loop
```python
unicos = []
for item in lista:
    if item not in unicos:
        unicos.append(item)
```

### ✅ Mais Otimizado: Set Direto
```python
# Sem preservar ordem
unicos = list(set(lista))

# Preservando ordem (Python 3.7+)
unicos = list(dict.fromkeys(lista))
```

**Performance:**

- Loop com `in`: O(n²)
- Set: O(n)

---

## 3. Itertools para Iterações Complexas

### ❌ Menos Otimizado: Loops Aninhados para Combinações
```python
# Produto cartesiano
resultado = []
for a in lista1:
    for b in lista2:
        for c in lista3:
            resultado.append((a, b, c))
```

### ✅ Mais Otimizado: itertools.product
```python
from itertools import product

resultado = list(product(lista1, lista2, lista3))
```

**Vantagens:**

- Código mais limpo e declarativo
- Implementação otimizada em C
- Lazy evaluation (não consome memória até necessário)

---

### ❌ Menos Otimizado: Agrupamento Manual
```python
# Agrupar por categoria
grupos = {}
for item in lista:
    categoria = item['categoria']
    if categoria not in grupos:
        grupos[categoria] = []
    grupos[categoria].append(item)
```

### ✅ Mais Otimizado: itertools.groupby
```python
from itertools import groupby
from operator import itemgetter

# Importante: lista precisa estar ordenada pela chave
lista_ordenada = sorted(lista, key=itemgetter('categoria'))
grupos = {k: list(v) for k, v in groupby(lista_ordenada, key=itemgetter('categoria'))}
```

**Alternativa:** `collections.defaultdict`
```python
from collections import defaultdict

grupos = defaultdict(list)
for item in lista:
    grupos[item['categoria']].append(item)
```

**Trade-offs:**

- `groupby`: requer ordenação prévia, mais eficiente para dados já ordenados
- `defaultdict`: não requer ordenação, mais intuitivo

---

### Outras Funções Úteis do Itertools

```python
from itertools import (
    combinations,      # Combinações sem repetição
    permutations,      # Permutações
    accumulate,        # Soma/operação acumulativa
    islice,           # Fatiar iteradores
    chain,            # Concatenar iteradores
    takewhile,        # Pegar enquanto condição é verdadeira
    dropwhile,        # Descartar enquanto condição é verdadeira
    compress,         # Filtrar por seletor booleano
    zip_longest       # Zip que não para no menor
)

# Exemplos
list(combinations([1, 2, 3], 2))  # [(1,2), (1,3), (2,3)]
list(accumulate([1, 2, 3, 4]))    # [1, 3, 6, 10]
list(islice(range(100), 10, 20))  # [10, 11, ..., 19]
```

---

## 4. Operações de Conjunto (Sets)

### ❌ Menos Otimizado: Interseção com Loops
```python
comuns = []
for item in lista1:
    if item in lista2:
        if item not in comuns:
            comuns.append(item)
```

### ✅ Mais Otimizado: Operações de Set
```python
# Interseção
comuns = list(set(lista1) & set(lista2))
# ou
comuns = list(set(lista1).intersection(lista2))

# União
todos = list(set(lista1) | set(lista2))
# ou
todos = list(set(lista1).union(lista2))

# Diferença (em lista1 mas não em lista2)
diff = list(set(lista1) - set(lista2))

# Diferença simétrica (em um mas não em ambos)
diff_sim = list(set(lista1) ^ set(lista2))
```

**Performance:** O(n + m) vs O(n × m) dos loops

**Operadores de Set:**

- `&` ou `.intersection()`: elementos em ambos
- `|` ou `.union()`: elementos em qualquer um
- `-` ou `.difference()`: elementos no primeiro mas não no segundo
- `^` ou `.symmetric_difference()`: elementos em um mas não em ambos

---

### Verificações Eficientes com Sets

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Verificar se é subconjunto
set1.issubset(set2)      # False
set1 <= set2             # False

# Verificar se é superconjunto
set1.issuperset({1, 2})  # True
set1 >= {1, 2}           # True

# Verificar se são disjuntos (sem elementos comuns)
set1.isdisjoint({7, 8})  # True
```

---

## 5. Strings e Joins

### ❌ Menos Otimizado: Concatenação com +
```python
# NUNCA faça isso em loops!
resultado = ""
for palavra in lista_palavras:
    resultado = resultado + palavra + " "
```

**Por que é ruim?**

- Strings são imutáveis em Python
- Cada concatenação cria uma nova string
- Complexidade O(n²) devido a cópias repetidas

### ✅ Mais Otimizado: Join
```python
resultado = " ".join(lista_palavras)
```

**Performance:** O(n) - aloca memória uma vez e copia todos os elementos

---

### Casos Específicos de Strings

```python
# Construir string com formatação
# ❌ Menos otimizado
texto = ""
for i, item in enumerate(items):
    texto += f"{i}: {item}\n"

# ✅ Mais otimizado
texto = "\n".join(f"{i}: {item}" for i, item in enumerate(items))

# Para muitas operações: usar io.StringIO
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
# ❌ Menos otimizado
quadrados = []
for x in range(100):
    if x % 2 == 0:
        quadrados.append(x ** 2)

# ✅ Mais otimizado
quadrados = [x ** 2 for x in range(100) if x % 2 == 0]
```

### Dict Comprehension

```python
# ❌ Menos otimizado
mapa = {}
for item in items:
    mapa[item.id] = item.valor

# ✅ Mais otimizado
mapa = {item.id: item.valor for item in items}
```

### Set Comprehension

```python
# ❌ Menos otimizado
unicos = set()
for item in items:
    if item > 0:
        unicos.add(item)

# ✅ Mais otimizado
unicos = {item for item in items if item > 0}
```

### Generator Expression (Para Grandes Volumes)

```python
# List comprehension: cria lista completa na memória
quadrados = [x ** 2 for x in range(1000000)]

# Generator: calcula sob demanda
quadrados = (x ** 2 for x in range(1000000))

# Uso
for quad in quadrados:
    print(quad)  # Calcula apenas quando necessário
```

**Trade-offs:**

- Generator: memória constante O(1), não pode ser reusado
- List: memória O(n), pode iterar múltiplas vezes

---

## 7. Funções Built-in para Agregação

### ❌ Menos Otimizado: Loops para Agregações
```python
# Soma
total = 0
for num in numeros:
    total += num

# Máximo
maximo = numeros[0]
for num in numeros:
    if num > maximo:
        maximo = num

# Mínimo
minimo = numeros[0]
for num in numeros:
    if num < minimo:
        minimo = num
```

### ✅ Mais Otimizado: Built-ins
```python
total = sum(numeros)
maximo = max(numeros)
minimo = min(numeros)

# Com key function
pessoa_mais_velha = max(pessoas, key=lambda p: p.idade)

# Min e max juntos
from statistics import mean, median
menor, maior = min(numeros), max(numeros)
media = mean(numeros)
mediana = median(numeros)
```

---

### Map, Filter e Reduce

```python
# ❌ Menos otimizado
dobrados = []
for x in numeros:
    dobrados.append(x * 2)

# ✅ Opção 1: List comprehension (geralmente preferida)
dobrados = [x * 2 for x in numeros]

# ✅ Opção 2: Map (quando aplicar função existente)
dobrados = list(map(lambda x: x * 2, numeros))
# Melhor ainda com função nomeada
def dobrar(x):
    return x * 2
dobrados = list(map(dobrar, numeros))
```

```python
# Filter
# ❌ Menos otimizado
pares = []
for x in numeros:
    if x % 2 == 0:
        pares.append(x)

# ✅ Opção 1: List comprehension
pares = [x for x in numeros if x % 2 == 0]

# ✅ Opção 2: Filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
```

```python
# Reduce (para operações acumulativas complexas)
from functools import reduce

# Produto de todos elementos
produto = reduce(lambda x, y: x * y, numeros, 1)

# Alternativa mais legível para casos simples
from operator import mul
produto = reduce(mul, numeros, 1)
```

**Quando usar cada um:**

- **List comprehension**: default choice, mais pythônico
- **Map**: quando aplicar função existente complexa
- **Filter**: quando a condição é uma função nomeada complexa
- **Reduce**: operações acumulativas que não têm built-in

---

## 8. Casos Especiais e Trade-offs

### Quando NÃO Otimizar Prematuramente

```python
# Para listas pequenas (<100 elementos), a diferença é desprezível
# ❌ Over-engineering
pequena_lista = [1, 2, 3, 4, 5]
set_pequeno = set(pequena_lista)  # Overhead desnecessário

# ✅ Mais simples
if 3 in pequena_lista:
    pass
```

---

### Contadores e Frequências

```python
# ❌ Menos otimizado
contagem = {}
for item in lista:
    if item in contagem:
        contagem[item] += 1
    else:
        contagem[item] = 1

# ✅ Opção 1: get() com default
contagem = {}
for item in lista:
    contagem[item] = contagem.get(item, 0) + 1

# ✅ Opção 2: defaultdict
from collections import defaultdict
contagem = defaultdict(int)
for item in lista:
    contagem[item] += 1

# ✅ Opção 3: Counter (MELHOR para contagens)
from collections import Counter
contagem = Counter(lista)

# Métodos úteis do Counter
contagem.most_common(3)      # 3 mais comuns
contagem['item']             # Retorna 0 se não existe
contagem1 + contagem2        # Soma contadores
```

---

### Any e All (Avaliação em Curto-Circuito)

```python
# ❌ Menos otimizado
tem_positivo = False
for num in numeros:
    if num > 0:
        tem_positivo = True
        break

# ✅ Mais otimizado
tem_positivo = any(num > 0 for num in numeros)

# ❌ Menos otimizado
todos_positivos = True
for num in numeros:
    if num <= 0:
        todos_positivos = False
        break

# ✅ Mais otimizado
todos_positivos = all(num > 0 for num in numeros)
```

**Vantagem:** Para quando encontra primeiro True/False, não processa resto

---

### Enumerate em vez de Range + Index

```python
# ❌ Menos otimizado
for i in range(len(lista)):
    print(f"{i}: {lista[i]}")

# ✅ Mais otimizado
for i, item in enumerate(lista):
    print(f"{i}: {item}")

# Com índice inicial diferente
for i, item in enumerate(lista, start=1):
    print(f"{i}: {item}")
```

---

### Zip para Iteração Paralela

```python
# ❌ Menos otimizado
for i in range(len(nomes)):
    print(f"{nomes[i]}: {idades[i]}")

# ✅ Mais otimizado
for nome, idade in zip(nomes, idades):
    print(f"{nome}: {idade}")

# Para listas de tamanhos diferentes
from itertools import zip_longest
for nome, idade in zip_longest(nomes, idades, fillvalue='N/A'):
    print(f"{nome}: {idade}")
```

---

### Operador Walrus (:=) - Python 3.8+

```python
# ❌ Avaliação dupla
if len(lista) > 10:
    tamanho = len(lista)
    print(f"Lista grande: {tamanho}")

# ✅ Com walrus operator
if (tamanho := len(lista)) > 10:
    print(f"Lista grande: {tamanho}")

# Útil em list comprehensions
# ❌ Calcula duas vezes
resultado = [calcular(x) for x in dados if calcular(x) > 10]

# ✅ Calcula uma vez
resultado = [y for x in dados if (y := calcular(x)) > 10]
```

---

## Resumo de Performance

| Operação | Menos Otimizado | Mais Otimizado | Ganho Típico |
|----------|----------------|----------------|--------------|
| Busca | `for` em lista O(n) | `in` set O(1) | ~100x+ |
| Concatenação strings | `+` em loop O(n²) | `join()` O(n) | ~10-100x |
| Remoção duplicatas | loop com `in` O(n²) | `set()` O(n) | ~50x+ |
| Transformação lista | `for` + `append()` | list comprehension | ~30% |
| Interseção listas | loops aninhados O(n×m) | set operations O(n+m) | ~10-50x |
| Agregações | loops manuais | `sum()`, `max()`, etc | ~20-40% |

---

## Princípios Gerais de Otimização

### 1. Use estruturas de dados adequadas

- Busca/verificação frequente → Set/Dict
- Ordem importa → List/Deque
- Contagem → Counter
- Agrupamento → defaultdict

### 2. Prefira built-ins e stdlib

- Implementados em C, altamente otimizados
- Bem testados e mantidos

### 3. Evite trabalho desnecessário

- Use lazy evaluation (generators) quando possível
- Avaliação em curto-circuito com `any()`/`all()`
- Cache resultados quando apropriado

### 4. Legibilidade vs Performance

- Para <1000 elementos, prefira código legível
- Otimize apenas gargalos identificados (profile primeiro!)
- Use comprehensions quando melhoram legibilidade

### 5. Medição

```python
import timeit

# Medir tempo
tempo = timeit.timeit('sum(range(100))', number=10000)

# Comparar alternativas
print(timeit.timeit('[x**2 for x in range(100)]', number=10000))
print(timeit.timeit('list(map(lambda x: x**2, range(100)))', number=10000))
```

---

## Ferramentas de Profiling

```python
# cProfile para análise detalhada
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()
# seu código aqui
profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10 funções

# line_profiler para análise linha por linha
# pip install line_profiler
# @profile decorator e executar: kernprof -l -v script.py

# memory_profiler para uso de memória
# pip install memory_profiler
# @profile decorator e executar: python -m memory_profiler script.py
```

---

## Conclusão

A otimização em Python envolve conhecer as ferramentas certas para cada trabalho. As principais diretrizes são:

- **Sets** para operações de pertencimento e conjunto
- **Comprehensions** para transformações e filtragens
- **Itertools** para iterações complexas
- **Join** para concatenação de strings
- **Built-ins** para agregações
- **Generators** para grandes volumes de dados

Lembre-se: **meça antes de otimizar!** A legibilidade e manutenibilidade do código são mais importantes que micro-otimizações em código não-crítico.

---

## Próximos Passos

- [→ Referência Rápida (Cheat Sheet)](referencia_rapida.md)
- [→ Executar Benchmarks](https://github.com/DougFelipe/zen-python/blob/main/src/exemplos_otimizacao.py)
- [← Aprender Zen do Python (Teoria)](../zen/teoria.md)
- [← Exemplos Práticos do Zen](../zen/pratica_parte1.md)

