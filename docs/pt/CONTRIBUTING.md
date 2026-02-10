# 🤝 Contribuindo para o Zen Python

> **Navegação:** [← Voltar ao Início](index.md) | [Changelog →](CHANGELOG.md)

Obrigado por considerar contribuir para o projeto **Zen Python**! Este é um projeto educativo que busca ensinar os princípios fundamentais do Python e técnicas de otimização.

## 📋 Índice

- [Tipos de Contribuição](#tipos-de-contribuicao)
- [Como Começar](#como-comecar)
- [Diretrizes de Código](#diretrizes-de-codigo)
- [Enviando uma Contribuição](#enviando-uma-contribuicao)
- [Reportando Bugs](#reportando-bugs)
- [Solicitando Features](#solicitando-features)

## 🎯 Tipos de Contribuição

### 📚 Documentação
- Melhorar explicações dos princípios do Zen
- Adicionar mais exemplos práticos
- Corrigir erros de português
- Traduzir conteúdo para outros idiomas

### 💻 Código
- Adicionar novos exemplos de otimização
- Melhorar benchmarks existentes
- Corrigir bugs nos scripts
- Adicionar novos casos de uso

### 🐛 Testes
- Adicionar testes automatizados
- Verificar compatibilidade com diferentes versões do Python
- Testar em diferentes sistemas operacionais

### 🎨 Design
- Melhorar formatação da documentação
- Criar visualizações gráficas
- Aprimorar a apresentação dos resultados

## 🚀 Como Começar

### Pré-requisitos

1. **Python 3.7+** instalado
2. **Git** para controle de versão
3. Conhecimento básico de Python

### Configuração do Ambiente

```bash
# 1. Fork o repositório no GitHub
# 2. Clone seu fork
git clone https://github.com/seu-usuario/zen-python.git
cd zen-python

# 3. Verifique se tudo funciona
python src/setup_check.py

# 4. Teste os exemplos
python src/demo_rapido.py
```

### Estrutura do Projeto

```
zen-python/
├── README.md                          # Documentação principal
├── LICENSE                            # Licença MIT
├── src/                               # 🐍 Código Python
│   ├── zen_python_exemplos.py           # Scripts executáveis do Zen
│   ├── exemplos_otimizacao.py           # Scripts de benchmark
│   ├── demo_rapido.py                   # Demo rápido
│   └── setup_check.py                   # Verificação de ambiente
├── docs/                              # 📚 Documentação
│   ├── zen/                           # Zen of Python
│   │   ├── teoria.md                    # Teoria dos princípios
│   │   ├── pratica_parte1.md            # Exemplos práticos (1-12)
│   │   └── pratica_parte2.md            # Exemplos práticos (13-19)
│   ├── otimizacao/                    # Otimização
│   │   ├── guia_completo.md             # Guia de otimização
│   │   └── referencia_rapida.md         # Cheat sheet
│   ├── CONTRIBUTING.md                  # Este arquivo
│   └── CHANGELOG.md                     # Histórico de versões
└── config/                            # ⚙️ Configuração
    └── pyproject.toml                   # Configuração do projeto
```

## 📝 Diretrizes de Código

### Estilo de Código Python

Seguimos o [PEP 8](https://www.python.org/dev/peps/pep-0008/) com algumas adaptações:

```python
# ✅ Bom
def calculate_fibonacci(number: int) -> int:
    """
    Calcula o n-ésimo número da sequência de Fibonacci.
    
    Args:
        number: Posição na sequência (deve ser >= 0)
        
    Returns:
        O número de Fibonacci correspondente
    """
    if number <= 1:
        return number
    return calculate_fibonacci(number - 1) + calculate_fibonacci(number - 2)

# ❌ Evite
def fib(n):
    if n<=1:return n
    return fib(n-1)+fib(n-2)
```

### Documentação

- Use docstrings em todas as funções
- Comente código complexo
- Mantenha comentários atualizados
- Use emojis para tornar a documentação mais visual

### Benchmarks

Ao adicionar novos benchmarks:

```python
def benchmark_nova_funcao():
    print("\n" + "="*70)
    print("EXEMPLO X: DESCRIÇÃO CLARA")
    print("="*70)
    
    # Configuração dos dados de teste
    dados = preparar_dados_teste()
    
    # Método tradicional
    def metodo_tradicional():
        # implementação...
        pass
    
    # Método otimizado
    def metodo_otimizado():
        # implementação...
        pass
    
    # Medições
    tempo_tradicional = timeit.timeit(metodo_tradicional, number=1000)
    tempo_otimizado = timeit.timeit(metodo_otimizado, number=1000)
    
    # Resultados
    print(f"\n📊 Descrição do teste:")
    print(f"   Método tradicional: {tempo_tradicional:.6f}s")
    print(f"   Método otimizado:   {tempo_otimizado:.6f}s")
    print(f"   Speedup: {tempo_tradicional/tempo_otimizado:.1f}x mais rápido ⚡")
```

## 🔄 Enviando uma Contribuição

### Processo de Pull Request

1. **Crie uma branch para sua feature:**
   ```bash
   git checkout -b feature/minha-nova-feature
   ```

2. **Faça suas alterações seguindo as diretrizes**

3. **Teste suas alterações:**
   ```bash
   python src/setup_check.py
   python src/exemplos_otimizacao.py  # Se alterou benchmarks
   python src/zen_python_exemplos.py  # Se alterou exemplos do Zen
   ```

4. **Commit suas alterações:**
   ```bash
   git add .
   git commit -m "feat: adiciona exemplo de otimização com sets
   
   - Novo benchmark comparando busca em lista vs set
   - Documentação explicando complexidade O(n) vs O(1)
   - Casos de uso práticos incluídos"
   ```

5. **Push para seu fork:**
   ```bash
   git push origin feature/minha-nova-feature
   ```

6. **Abra um Pull Request** no GitHub

### Formato de Commits

Seguimos o padrão [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Mudanças na documentação
- `refactor:` - Refatoração de código
- `test:` - Adicionar ou modificar testes
- `chore:` - Tarefas de manutenção

### O que Incluir no PR

- **Título claro** explicando a mudança
- **Descrição detalhada** do que foi alterado e por quê
- **Screenshots** se aplicável (para mudanças visuais)
- **Testes** para verificar que funciona como esperado
- **Documentação** atualizada se necessário

## 🐛 Reportando Bugs

### Como Reportar

1. **Verifique se o bug já foi reportado** nos Issues
2. **Use o template de bug report**
3. **Inclua informações detalhadas:**
   - Versão do Python
   - Sistema operacional
   - Passos para reproduzir
   - Resultado esperado vs. obtido
   - Logs ou mensagens de erro

### Exemplo de Report

```markdown
**Descrição do Bug**
O benchmark de concatenação de strings falha com listas muito grandes.

**Para Reproduzir**
1. Execute `python exemplos_otimizacao.py`
2. Aguarde chegar no Exemplo 2
3. Erro ocorre com MemoryError

**Ambiente**
- Python: 3.9.7
- OS: Windows 10
- RAM: 4GB

**Resultado Esperado**
Benchmark deveria completar normalmente.

**Resultado Obtido**

- MemoryError: Unable to allocate 2.1GB for an array


```

## 🆕 Solicitando Features

### Diretrizes para Requests

- **Explique o caso de uso** - por que é necessário?
- **Descreva a solução proposta** - como deveria funcionar?
- **Considere alternativas** - existem outras abordagens?
- **Pense na manutenibilidade** - é sustentável a longo prazo?

### Tipos de Features Desejadas

- ✅ Novos exemplos de otimização
- ✅ Casos de uso práticos do mundo real  
- ✅ Análises de complexidade computacional
- ✅ Comparações com outras linguagens
- ✅ Visualizações gráficas de performance
- ❌ Features que complexificam desnecessariamente
- ❌ Dependências externas pesadas


## 🙏 Reconhecimentos

Contribuidores serão reconhecidos:

- **README.md** - lista de contribuidores
- **CHANGELOG.md** - créditos nas releases
- **Issues e PRs** - menções e agradecimentos

## 📞 Contato

- **Issues**: Para bugs e feature requests
- **Discussions**: Para perguntas gerais

