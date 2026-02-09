#!/usr/bin/env python3
"""
Demo Rápido - Zen of Python e Otimizações
Execute: python demo_rapido.py
"""

import time
import sys
from pathlib import Path

def mostrar_cabecalho():
    print("\n" + "="*80)
    print(" 🐍 ZEN PYTHON & OTIMIZAÇÕES - DEMO RÁPIDO")
    print("="*80)

def zen_python():
    print("\n📜 O Zen of Python:")
    print("-" * 40)
    import this
    time.sleep(2)

def demo_otimizacao_rapida():
    print("\n\n⚡ DEMO: Diferença de Performance")
    print("-" * 40)
    
    # Preparar dados
    import timeit
    from collections import Counter
    
    # Demo 1: Busca em coleções
    print("\n1️⃣ Busca em Coleções")
    lista = list(range(10000))
    conjunto = set(lista)
    
    # Teste busca
    tempo_lista = timeit.timeit(lambda: 9999 in lista, number=1000)
    tempo_set = timeit.timeit(lambda: 9999 in conjunto, number=1000)
    
    print(f"   Lista:  {tempo_lista:.6f}s")
    print(f"   Set:    {tempo_set:.6f}s")
    print(f"   📊 Set é {tempo_lista/tempo_set:.0f}x mais rápido! ⚡")
    
    # Demo 2: Concatenação de strings
    print("\n2️⃣ Concatenação de Strings")
    palavras = ['python'] * 1000
    
    def concat_plus():
        result = ""
        for palavra in palavras:
            result += palavra + " "
        return result
    
    def concat_join():
        return " ".join(palavras)
    
    tempo_plus = timeit.timeit(concat_plus, number=100)
    tempo_join = timeit.timeit(concat_join, number=100)
    
    print(f"   Operador +:  {tempo_plus:.6f}s")
    print(f"   Join:        {tempo_join:.6f}s")
    print(f"   📊 Join é {tempo_plus/tempo_join:.0f}x mais rápido! ⚡")
    
    # Demo 3: Counter
    print("\n3️⃣ Contagem de Elementos")
    data = ['a', 'b', 'a', 'c', 'b', 'a'] * 100
    
    def count_manual():
        counts = {}
        for item in data:
            counts[item] = counts.get(item, 0) + 1
        return counts
    
    def count_counter():
        return dict(Counter(data))
    
    tempo_manual = timeit.timeit(count_manual, number=1000)
    tempo_counter = timeit.timeit(count_counter, number=1000)
    
    print(f"   Manual:   {tempo_manual:.6f}s")
    print(f"   Counter:  {tempo_counter:.6f}s")
    print(f"   📊 Counter é {tempo_manual/tempo_counter:.1f}x mais rápido! ⚡")


def main():
    try:
        mostrar_cabecalho()
        zen_python()
        demo_otimizacao_rapida()
        
        print("\n" + "="*80)
        print("✅ Demo concluído! Para mais exemplos, execute os outros scripts.")
        print("="*80 + "\n")
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Demo interrompido pelo usuário.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()