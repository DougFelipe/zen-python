"""
Zen of Python - Exemplos Executáveis
Demonstra cada princípio com código que roda

Execute: python zen_python_exemplos.py
"""

import timeit
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Optional
import json


def mostrar_zen():
    """Mostra o Zen of Python."""
    print("\n" + "=" * 70)
    print("THE ZEN OF PYTHON")
    print("=" * 70)
    import this
    print()


# =================================================================
# 1. Beautiful is better than ugly
# =================================================================

def exemplo_1_beautiful():
    print("\n" + "=" * 70)
    print("1. BEAUTIFUL IS BETTER THAN UGLY")
    print("=" * 70)
    
    # Código feio
    print("\n❌ Código feio:")
    print("""
def f(x,y):
    z=x+y
    if z>10:r=z*2
    else:r=z+5
    return r
    """)
    
    # Código bonito
    print("\n✅ Código bonito:")
    print("""
def calculate_result(base: int, addition: int) -> int:
    \"\"\"Calcula resultado baseado em soma.\"\"\"
    total = base + addition
    
    if total > 10:
        result = total * 2
    else:
        result = total + 5
    
    return result
    """)


# =================================================================
# 2. Explicit is better than implicit
# =================================================================

def exemplo_2_explicit():
    print("\n" + "=" * 70)
    print("2. EXPLICIT IS BETTER THAN IMPLICIT")
    print("=" * 70)
    
    # Implícito
    print("\n❌ Implícito - from math import *")
    print("   result = sqrt(16)  # De onde vem sqrt?")
    
    # Explícito
    print("\n✅ Explícito:")
    import math
    result = math.sqrt(16)
    print(f"   import math")
    print(f"   result = math.sqrt(16)  # Claramente do módulo math")
    print(f"   Result: {result}")


# =================================================================
# 3. Simple is better than complex
# =================================================================

def exemplo_3_simple():
    print("\n" + "=" * 70)
    print("3. SIMPLE IS BETTER THAN COMPLEX")
    print("=" * 70)
    
    numbers = [1, 2, 3, 4, 5]
    
    # Complexo
    print("\n❌ Complexo:")
    print("""
class NumberProcessor:
    def process(self, nums):
        result = []
        for n in nums:
            result.append(n * 2)
        return result

processor = NumberProcessor()
doubled = processor.process(numbers)
    """)
    
    # Simples
    print("\n✅ Simples:")
    doubled = [n * 2 for n in numbers]
    print(f"   doubled = [n * 2 for n in numbers]")
    print(f"   Result: {doubled}")


# =================================================================
# 4. Complex is better than complicated
# =================================================================

def exemplo_4_complex():
    print("\n" + "=" * 70)
    print("4. COMPLEX IS BETTER THAN COMPLICATED")
    print("=" * 70)
    
    print("\n❌ Complicado (tudo misturado):")
    print("""
def process(order):
    if order['status'] == 'pending':
        if order['payment']['method'] == 'credit':
            if order['payment']['verified']:
                # ... 50 linhas de lógica entrelaçada
    """)
    
    print("\n✅ Complexo (bem organizado):")
    print("""
class OrderValidator:
    def validate_status(self, order): ...
    def validate_payment(self, order): ...

class OrderProcessor:
    def __init__(self):
        self.validator = OrderValidator()
    
    def process(self, order):
        self.validator.validate_status(order)
        self.validator.validate_payment(order)
        # Lógica clara e modular
    """)


# =================================================================
# 5. Flat is better than nested
# =================================================================

def exemplo_5_flat():
    print("\n" + "=" * 70)
    print("5. FLAT IS BETTER THAN NESTED")
    print("=" * 70)
    
    data = [1, 2, 3, None, 5]
    
    # Aninhado
    print("\n❌ Muito aninhado:")
    print("""
def process(data):
    if data:
        if len(data) > 0:
            for item in data:
                if item:
                    if item > 0:
                        print(item * 2)
    """)
    
    # Plano
    print("\n✅ Plano (flat):")
    print("""
def process(data):
    if not data:
        return
    
    for item in data:
        if item and item > 0:
            print(item * 2)
    """)
    
    print("\n   Executando versão plana:")
    for item in data:
        if item and item > 0:
            print(f"   {item} * 2 = {item * 2}")


# =================================================================
# 7. Readability counts
# =================================================================

def exemplo_7_readability():
    print("\n" + "=" * 70)
    print("7. READABILITY COUNTS")
    print("=" * 70)
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Pouco legível
    print("\n❌ Pouco legível:")
    print("   r=[x*2 for x in n if x%2==0]")
    
    # Legível
    print("\n✅ Legível:")
    even_numbers = [num for num in numbers if num % 2 == 0]
    doubled = [num * 2 for num in even_numbers]
    print(f"   even_numbers = [num for num in numbers if num % 2 == 0]")
    print(f"   doubled = [num * 2 for num in even_numbers]")
    print(f"   Result: {doubled}")


# =================================================================
# 10. Errors should never pass silently
# =================================================================

def exemplo_10_errors():
    print("\n" + "=" * 70)
    print("10. ERRORS SHOULD NEVER PASS SILENTLY")
    print("=" * 70)
    
    # Erro silencioso
    print("\n❌ Erro passa silenciosamente:")
    print("""
def divide(a, b):
    try:
        return a / b
    except:
        pass  # NUNCA faça isso!
    """)
    
    # Erro explícito
    print("\n✅ Erro explícito:")
    print("""
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
    """)
    
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    print("\n   Exemplos:")
    print(f"   divide(10, 2) = {divide(10, 2)}")
    try:
        divide(10, 0)
    except ValueError as e:
        print(f"   divide(10, 0) levanta ValueError: {e}")


# =================================================================
# 13. There should be one obvious way to do it
# =================================================================

def exemplo_13_one_way():
    print("\n" + "=" * 70)
    print("13. THERE SHOULD BE ONE OBVIOUS WAY TO DO IT")
    print("=" * 70)
    
    fruits = ['apple', 'banana', 'orange']
    
    print("\n   Iteração sobre lista:")
    print("\n   ✅ Forma óbvia (pythônica):")
    print("   for fruit in fruits:")
    print("       print(fruit)")
    
    for fruit in fruits:
        print(f"   {fruit}")
    
    print("\n   ❌ Possível, mas não idiomático:")
    print("   for i in range(len(fruits)):")
    print("       print(fruits[i])")


# =================================================================
# 15 & 16. Now vs Never
# =================================================================

def exemplo_15_16_timing():
    print("\n" + "=" * 70)
    print("15. NOW IS BETTER THAN NEVER")
    print("16. ALTHOUGH NEVER IS OFTEN BETTER THAN RIGHT NOW")
    print("=" * 70)
    
    print("\n   Equilíbrio entre ação e reflexão:")
    print("\n   ✅ NOW - Refatore quando vir código confuso")
    print("   ✅ NEVER - Não adicione features especulativas (YAGNI)")
    print("   ✅ LATER - Design complexo precisa pesquisa")
    
    print("\n   Exemplo de YAGNI:")
    print("""
   ❌ Over-engineering:
   class User:
       def __init__(self):
           self.backup_email = None  # "Pode precisar"
           self.preferences = {}     # "Eventualmente"
   
   ✅ Adicione apenas o necessário AGORA:
   class User:
       def __init__(self, name):
           self.name = name
   """)


# =================================================================
# 19. Namespaces
# =================================================================

def exemplo_19_namespaces():
    print("\n" + "=" * 70)
    print("19. NAMESPACES ARE ONE HONKING GREAT IDEA")
    print("=" * 70)
    
    print("\n   ❌ Poluição de namespace:")
    print("   from math import *")
    print("   result = sqrt(16)  # De onde vem?")
    
    print("\n   ✅ Namespace explícito:")
    import math
    import statistics
    
    print("   import math")
    print("   import statistics")
    print(f"   math.sqrt(16) = {math.sqrt(16)}")
    print(f"   statistics.mean([1,2,3]) = {statistics.mean([1,2,3])}")
    
    print("\n   📦 Organização com namespaces:")
    print("""
   myproject/
       models/
           user.py
           product.py
       services/
           user_service.py
       utils/
           validators.py
   
   from myproject.models.user import User
   from myproject.services.user_service import UserService
   """)


# =================================================================
# Comparação de Performance
# =================================================================

def benchmark_exemplos():
    print("\n" + "=" * 70)
    print("BENCHMARKS - DEMONSTRANDO DIFERENÇAS DE PERFORMANCE")
    print("=" * 70)
    
    # List comprehension vs loop
    print("\n   Transformação de lista:")
    
    def com_loop():
        result = []
        for i in range(1000):
            result.append(i * 2)
        return result
    
    def com_comprehension():
        return [i * 2 for i in range(1000)]
    
    tempo_loop = timeit.timeit(com_loop, number=1000)
    tempo_comp = timeit.timeit(com_comprehension, number=1000)
    
    print(f"   Loop com append: {tempo_loop:.6f}s")
    print(f"   List comprehension: {tempo_comp:.6f}s")
    print(f"   Comprehension é {tempo_loop/tempo_comp:.1f}x mais rápida")


# =================================================================
# Exemplo Prático Completo
# =================================================================

@dataclass
class User:
    """Exemplo seguindo os princípios do Zen."""
    name: str
    email: str
    age: int
    
    def __post_init__(self):
        """Valida dados após inicialização."""
        if not self.name:
            raise ValueError("Name cannot be empty")
        if '@' not in self.email:
            raise ValueError("Invalid email")
        if self.age < 0:
            raise ValueError("Age cannot be negative")


def exemplo_pratico_completo():
    print("\n" + "=" * 70)
    print("EXEMPLO PRÁTICO COMPLETO")
    print("=" * 70)
    
    print("\n   Aplicando múltiplos princípios do Zen:")
    
    # Beautiful, Explicit, Simple
    user = User(name="Alice", email="alice@example.com", age=30)
    print(f"\n   ✅ Criado: {user}")
    
    # Errors should never pass silently
    print("\n   ❌ Tentando criar usuário inválido:")
    try:
        invalid_user = User(name="", email="invalid", age=-5)
    except ValueError as e:
        print(f"   Erro capturado: {e}")
    
    # Readability counts
    users = [
        User("Alice", "alice@example.com", 30),
        User("Bob", "bob@example.com", 25),
        User("Charlie", "charlie@example.com", 35),
    ]
    
    # One obvious way - list comprehension
    adults = [u for u in users if u.age >= 18]
    print(f"\n   Usuários adultos: {len(adults)}")
    
    # Namespaces - Counter
    ages = [u.age for u in users]
    age_distribution = Counter(ages)
    print(f"   Distribuição de idades: {dict(age_distribution)}")


# =================================================================
# MAIN
# =================================================================

def main():
    print("\n" + "=" * 70)
    print("🐍 ZEN OF PYTHON - EXEMPLOS PRÁTICOS E EXECUTÁVEIS")
    print("=" * 70)
    
    mostrar_zen()
    
    exemplo_1_beautiful()
    exemplo_2_explicit()
    exemplo_3_simple()
    exemplo_4_complex()
    exemplo_5_flat()
    exemplo_7_readability()
    exemplo_10_errors()
    exemplo_13_one_way()
    exemplo_15_16_timing()
    exemplo_19_namespaces()
    
    benchmark_exemplos()
    exemplo_pratico_completo()
    
    print("\n" + "=" * 70)
    print("✅ PRINCÍPIOS CHAVE DO ZEN OF PYTHON")
    print("=" * 70)
    print("""
    1. Priorize BELEZA e LEGIBILIDADE
    2. Seja EXPLÍCITO, não confie em magia
    3. Prefira SIMPLES sobre complexo
    4. Use FLAT, evite aninhamento profundo
    5. ERROS devem ser visíveis, não silenciosos
    6. Deve haver UMA FORMA ÓBVIA de fazer
    7. Use NAMESPACES para organização
    8. Balance AÇÃO (now) com REFLEXÃO (never vs right now)
    
    💡 Esses princípios se tornam INTUIÇÃO com prática!
    """)
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
