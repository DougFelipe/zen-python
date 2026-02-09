"""
🚀 Exemplos Práticos de Otimização em Python

Este script demonstra técnicas de otimização com benchmarks reais.
Cada exemplo compara diferentes abordagens e mede a performance.

Executar: python exemplos_otimizacao.py
Tempo estimado: 2-5 minutos (dependendo do hardware)

Autor: Repositório Zen Python
Licença: MIT
"""

import timeit
import sys
from itertools import product, groupby, chain, combinations
from collections import Counter, defaultdict
from operator import itemgetter
import random

# Configurações para os benchmarks
BENCHMARK_CONFIG = {
    'tamanho_teste': 10000,
    'repeticoes': 1000,
    'seeds': 42  # Para reprodutibilidade
}

# ============================================================================
# EXEMPLO 1: BUSCA EM COLEÇÕES
# ============================================================================

def benchmark_busca():
    print("\n" + "="*70)
    print("EXEMPLO 1: BUSCA EM COLEÇÕES")
    print("="*70)
    
    # Criar dados de teste
    tamanho = BENCHMARK_CONFIG['tamanho_teste']
    repeticoes = BENCHMARK_CONFIG['repeticoes']
    lista = list(range(tamanho))
    conjunto = set(lista)
    valor_buscar = tamanho - 1  # Pior caso: último elemento
    
    # Método 1: Loop em lista
    def busca_lista():
        for item in lista:
            if item == valor_buscar:
                return True
        return False
    
    # Método 2: Operador in em lista
    def busca_lista_in():
        return valor_buscar in lista
    
    # Método 3: Operador in em set
    def busca_set():
        return valor_buscar in conjunto
    
    # Benchmarks
    tempo_loop = timeit.timeit(busca_lista, number=repeticoes)
    tempo_lista_in = timeit.timeit(busca_lista_in, number=repeticoes)
    tempo_set = timeit.timeit(busca_set, number=repeticoes)
    
    print(f"\n📊 Buscar elemento em coleção de {tamanho:,} elementos:")
    print(f"   Loop manual:        {tempo_loop:.6f}s")
    print(f"   'in' com lista:     {tempo_lista_in:.6f}s  ({tempo_loop/tempo_lista_in:.1f}x mais rápido)")
    print(f"   'in' com set:       {tempo_set:.6f}s  ({tempo_loop/tempo_set:.1f}x mais rápido) ⚡")
    print(f"\n💡 Set é {tempo_lista_in/tempo_set:.0f}x mais rápido que lista!")


# ============================================================================
# EXEMPLO 2: CONCATENAÇÃO DE STRINGS
# ============================================================================

def benchmark_strings():
    print("\n" + "="*70)
    print("EXEMPLO 2: CONCATENAÇÃO DE STRINGS")
    print("="*70)
    
    palavras = ['palavra'] * 1000
    
    # Método 1: Concatenação com +
    def concat_plus():
        resultado = ""
        for palavra in palavras:
            resultado = resultado + palavra + " "
        return resultado
    
    # Método 2: Join
    def concat_join():
        return " ".join(palavras)
    
    # Método 3: List append + join
    def concat_list_join():
        partes = []
        for palavra in palavras:
            partes.append(palavra)
        return " ".join(partes)
    
    tempo_plus = timeit.timeit(concat_plus, number=100)
    tempo_join = timeit.timeit(concat_join, number=100)
    tempo_list_join = timeit.timeit(concat_list_join, number=100)
    
    print(f"\n📊 Concatenar {len(palavras)} strings:")
    print(f"   Operador +:         {tempo_plus:.6f}s")
    print(f"   List + join:        {tempo_list_join:.6f}s  ({tempo_plus/tempo_list_join:.1f}x mais rápido)")
    print(f"   Join direto:        {tempo_join:.6f}s  ({tempo_plus/tempo_join:.1f}x mais rápido) ⚡")
    print(f"\n💡 Join é {tempo_plus/tempo_join:.0f}x mais rápido que concatenação com +!")


# ============================================================================
# EXEMPLO 3: REMOÇÃO DE DUPLICATAS
# ============================================================================

def benchmark_duplicatas():
    print("\n" + "="*70)
    print("EXEMPLO 3: REMOÇÃO DE DUPLICATAS")
    print("="*70)
    
    # Lista com duplicatas
    lista = [random.randint(0, 100) for _ in range(1000)]
    
    # Método 1: Loop com verificação
    def remove_dup_loop():
        unicos = []
        for item in lista:
            if item not in unicos:
                unicos.append(item)
        return unicos
    
    # Método 2: Set direto
    def remove_dup_set():
        return list(set(lista))
    
    # Método 3: Dict.fromkeys (preserva ordem)
    def remove_dup_dict():
        return list(dict.fromkeys(lista))
    
    tempo_loop = timeit.timeit(remove_dup_loop, number=100)
    tempo_set = timeit.timeit(remove_dup_set, number=100)
    tempo_dict = timeit.timeit(remove_dup_dict, number=100)
    
    print(f"\n📊 Remover duplicatas de lista com {len(lista)} elementos:")
    print(f"   Loop com 'in':      {tempo_loop:.6f}s")
    print(f"   Set (sem ordem):    {tempo_set:.6f}s  ({tempo_loop/tempo_set:.1f}x mais rápido) ⚡")
    print(f"   Dict (com ordem):   {tempo_dict:.6f}s  ({tempo_loop/tempo_dict:.1f}x mais rápido)")
    print(f"\n💡 Set é {tempo_loop/tempo_set:.0f}x mais rápido que loop!")


# ============================================================================
# EXEMPLO 4: OPERAÇÕES COM LISTAS
# ============================================================================

def benchmark_listas():
    print("\n" + "="*70)
    print("EXEMPLO 4: TRANSFORMAÇÃO DE LISTAS")
    print("="*70)
    
    numeros = list(range(1000))
    
    # Método 1: Loop com append
    def transform_loop():
        resultado = []
        for num in numeros:
            if num % 2 == 0:
                resultado.append(num ** 2)
        return resultado
    
    # Método 2: List comprehension
    def transform_comp():
        return [num ** 2 for num in numeros if num % 2 == 0]
    
    # Método 3: Map + filter
    def transform_map_filter():
        return list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numeros)))
    
    tempo_loop = timeit.timeit(transform_loop, number=1000)
    tempo_comp = timeit.timeit(transform_comp, number=1000)
    tempo_map = timeit.timeit(transform_map_filter, number=1000)
    
    print(f"\n📊 Transformar e filtrar lista de {len(numeros)} elementos:")
    print(f"   Loop + append:      {tempo_loop:.6f}s")
    print(f"   List comprehension: {tempo_comp:.6f}s  ({tempo_loop/tempo_comp:.1f}x mais rápido) ⚡")
    print(f"   Map + filter:       {tempo_map:.6f}s  ({tempo_loop/tempo_map:.1f}x mais rápido)")
    print(f"\n💡 List comprehension é a forma mais pythônica e eficiente!")


# ============================================================================
# EXEMPLO 5: OPERAÇÕES DE CONJUNTO
# ============================================================================

def exemplo_sets():
    print("\n" + "="*70)
    print("EXEMPLO 5: OPERAÇÕES DE CONJUNTO")
    print("="*70)
    
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
    lista2 = [5, 6, 7, 8, 9, 10, 11, 12]
    
    set1 = set(lista1)
    set2 = set(lista2)
    
    print(f"\nLista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print(f"\n🔍 Operações de Conjunto:")
    print(f"   Interseção (em ambos):           {set1 & set2}")
    print(f"   União (em qualquer):             {set1 | set2}")
    print(f"   Diferença (em 1 mas não em 2):   {set1 - set2}")
    print(f"   Diferença (em 2 mas não em 1):   {set2 - set1}")
    print(f"   Diferença simétrica (XOR):       {set1 ^ set2}")


# ============================================================================
# EXEMPLO 6: ITERTOOLS
# ============================================================================

def exemplo_itertools():
    print("\n" + "="*70)
    print("EXEMPLO 6: ITERTOOLS - FERRAMENTAS PODEROSAS")
    print("="*70)
    
    # Product - Produto cartesiano
    cores = ['vermelho', 'azul']
    tamanhos = ['P', 'M', 'G']
    print("\n🔄 product() - Produto cartesiano:")
    print(f"   Cores: {cores}")
    print(f"   Tamanhos: {tamanhos}")
    print(f"   Combinações: {list(product(cores, tamanhos))}")
    
    # Combinations
    numeros = [1, 2, 3, 4]
    print(f"\n🎲 combinations() - Combinações (ordem não importa):")
    print(f"   Números: {numeros}")
    print(f"   Pares: {list(combinations(numeros, 2))}")
    
    # Chain - Concatenar iteradores
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    lista3 = [7, 8, 9]
    print(f"\n🔗 chain() - Concatenar iteradores:")
    print(f"   Listas: {lista1}, {lista2}, {lista3}")
    print(f"   Encadeadas: {list(chain(lista1, lista2, lista3))}")
    
    # Groupby
    dados = [
        {'nome': 'Ana', 'categoria': 'A'},
        {'nome': 'Bruno', 'categoria': 'B'},
        {'nome': 'Carlos', 'categoria': 'A'},
        {'nome': 'Diana', 'categoria': 'B'},
    ]
    dados_ordenados = sorted(dados, key=itemgetter('categoria'))
    print(f"\n📦 groupby() - Agrupar por chave:")
    for categoria, grupo in groupby(dados_ordenados, key=itemgetter('categoria')):
        items = list(grupo)
        print(f"   Categoria {categoria}: {[p['nome'] for p in items]}")


# ============================================================================
# EXEMPLO 7: COUNTER E COLLECTIONS
# ============================================================================

def exemplo_collections():
    print("\n" + "="*70)
    print("EXEMPLO 7: COLLECTIONS - COUNTER E DEFAULTDICT")
    print("="*70)
    
    # Counter
    texto = "banana laranja maçã banana uva banana laranja"
    palavras = texto.split()
    
    # Método tradicional
    contagem_manual = {}
    for palavra in palavras:
        contagem_manual[palavra] = contagem_manual.get(palavra, 0) + 1
    
    # Com Counter
    contagem_counter = Counter(palavras)
    
    print(f"\n🔢 Counter - Contagem de frequências:")
    print(f"   Texto: '{texto}'")
    print(f"   Manual: {contagem_manual}")
    print(f"   Counter: {dict(contagem_counter)}")
    print(f"   Top 2: {contagem_counter.most_common(2)}")
    
    # Defaultdict
    print(f"\n📚 defaultdict - Agrupamento automático:")
    pessoas = [
        {'nome': 'Ana', 'idade': 25, 'cidade': 'SP'},
        {'nome': 'Bruno', 'idade': 30, 'cidade': 'RJ'},
        {'nome': 'Carlos', 'idade': 25, 'cidade': 'SP'},
        {'nome': 'Diana', 'idade': 30, 'cidade': 'RJ'},
    ]
    
    # Agrupar por idade
    por_idade = defaultdict(list)
    for pessoa in pessoas:
        por_idade[pessoa['idade']].append(pessoa['nome'])
    
    print(f"   Pessoas: {[p['nome'] for p in pessoas]}")
    for idade, nomes in sorted(por_idade.items()):
        print(f"   Idade {idade}: {nomes}")


# ============================================================================
# EXEMPLO 8: ANY, ALL E BUILT-INS
# ============================================================================

def exemplo_builtins():
    print("\n" + "="*70)
    print("EXEMPLO 8: ANY, ALL E FUNÇÕES BUILT-IN")
    print("="*70)
    
    numeros = [1, 2, 3, 4, 5, -1, 7, 8]
    
    print(f"\n📊 Números: {numeros}")
    print(f"\n✅ Funções de agregação:")
    print(f"   sum():      {sum(numeros)}")
    print(f"   max():      {max(numeros)}")
    print(f"   min():      {min(numeros)}")
    print(f"   len():      {len(numeros)}")
    
    print(f"\n🔍 Funções lógicas:")
    print(f"   any() - algum negativo?:  {any(n < 0 for n in numeros)}")
    print(f"   all() - todos positivos?: {all(n > 0 for n in numeros)}")
    
    # Enumerate
    print(f"\n🔢 enumerate() - índice + valor:")
    for i, num in enumerate(numeros[:5], start=1):
        print(f"   Posição {i}: {num}")
    
    # Zip
    nomes = ['Ana', 'Bruno', 'Carlos']
    idades = [25, 30, 35]
    print(f"\n🤐 zip() - combinar iteráveis:")
    print(f"   Nomes: {nomes}")
    print(f"   Idades: {idades}")
    for nome, idade in zip(nomes, idades):
        print(f"   {nome}: {idade} anos")


# ============================================================================
# EXEMPLO 9: GENERATOR vs LIST
# ============================================================================

def benchmark_generator():
    print("\n" + "="*70)
    print("EXEMPLO 9: GENERATOR vs LIST - USO DE MEMÓRIA")
    print("="*70)
    
    import sys
    
    # List comprehension
    lista = [x ** 2 for x in range(1000)]
    
    # Generator expression
    gerador = (x ** 2 for x in range(1000))
    
    print(f"\n💾 Comparação de memória:")
    print(f"   Lista:      {sys.getsizeof(lista):,} bytes")
    print(f"   Generator:  {sys.getsizeof(gerador):,} bytes")
    print(f"\n💡 Generator usa {sys.getsizeof(lista) / sys.getsizeof(gerador):.0f}x menos memória!")
    
    print(f"\n📝 Quando usar cada um:")
    print(f"   Lista:     Precisa iterar múltiplas vezes")
    print(f"   Generator: Iteração única, dados grandes, pipeline de processamento")


# ============================================================================
# EXEMPLO 10: CASOS PRÁTICOS
# ============================================================================

def exemplos_praticos():
    print("\n" + "="*70)
    print("EXEMPLO 10: CASOS PRÁTICOS DO DIA A DIA")
    print("="*70)
    
    # Caso 1: Filtrar e transformar dados
    print("\n📋 Caso 1: Processar lista de usuários")
    usuarios = [
        {'nome': 'Ana', 'idade': 17, 'ativo': True},
        {'nome': 'Bruno', 'idade': 25, 'ativo': True},
        {'nome': 'Carlos', 'idade': 30, 'ativo': False},
        {'nome': 'Diana', 'idade': 22, 'ativo': True},
    ]
    
    # Pegar nomes de usuários ativos e maiores de idade
    maiores_ativos = [
        u['nome'] 
        for u in usuarios 
        if u['idade'] >= 18 and u['ativo']
    ]
    print(f"   Usuários ativos maiores de 18: {maiores_ativos}")
    
    # Caso 2: Agrupar e contar
    print("\n🛒 Caso 2: Análise de carrinho de compras")
    carrinho = ['maçã', 'banana', 'maçã', 'laranja', 'banana', 'maçã']
    contagem = Counter(carrinho)
    print(f"   Carrinho: {carrinho}")
    print(f"   Resumo: {dict(contagem)}")
    print(f"   Item mais comprado: {contagem.most_common(1)[0]}")
    
    # Caso 3: Mesclar dados
    print("\n🔄 Caso 3: Mesclar informações de múltiplas fontes")
    ids = [1, 2, 3]
    nomes = ['Ana', 'Bruno', 'Carlos']
    emails = ['ana@email.com', 'bruno@email.com', 'carlos@email.com']
    
    usuarios_completos = [
        {'id': id_, 'nome': nome, 'email': email}
        for id_, nome, email in zip(ids, nomes, emails)
    ]
    
    print(f"   Dados mesclados:")
    for usuario in usuarios_completos:
        print(f"   {usuario}")


# ============================================================================
# MAIN
# ============================================================================

def main():
    import platform
    import time
    
    inicio = time.time()
    
    print("\n" + "="*70)
    print("🚀 EXEMPLOS PRÁTICOS DE OTIMIZAÇÃO EM PYTHON")
    print("="*70)
    
    # Informações do sistema
    print(f"📊 Sistema: {platform.system()} {platform.release()}")
    print(f"🐍 Python: {sys.version.split()[0]}")
    print(f"⚡ Processador: {platform.processor() or 'N/A'}")
    print(f"🔧 Configuração: {BENCHMARK_CONFIG}")
    
    # Definir seed para reprodutibilidade
    random.seed(BENCHMARK_CONFIG['seeds'])
    
    # Executar todos os exemplos
    benchmark_busca()
    benchmark_strings()
    benchmark_duplicatas()
    benchmark_listas()
    exemplo_sets()
    exemplo_itertools()
    exemplo_collections()
    exemplo_builtins()
    benchmark_generator()
    exemplos_praticos()
    
    # Tempo total de execução
    fim = time.time()
    tempo_total = fim - inicio
    
    print("\n" + "="*70)
    print("✅ PRINCIPAIS LIÇÕES")
    print("="*70)
    print(f"""
    1. Use SET para buscas e operações de conjunto (100x+ mais rápido)
    2. Use JOIN para concatenar strings (10-100x mais rápido)
    3. Use LIST COMPREHENSION para transformações (30% mais rápido)
    4. Use ITERTOOLS para iterações complexas (mais limpo e eficiente)
    5. Use COUNTER para contagens (mais simples e direto)
    6. Use GENERATOR para economizar memória em grandes volumes
    7. Use ANY/ALL para verificações com short-circuit
    8. Use ENUMERATE e ZIP em vez de range(len())
    
    💡 Lembre-se: MEÇA antes de otimizar!
    🕐 Tempo total de execução: {tempo_total:.2f} segundos
    """)



if __name__ == "__main__":
    main()
