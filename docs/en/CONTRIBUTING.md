# 🤝 Contributing to Zen Python

> **Navigation:** [← Back to Home](index.md) | [Changelog →](CHANGELOG.md)

Thank you for considering contributing to the **Zen Python** project! This is an educational project that aims to teach the fundamental principles of Python and optimization techniques.

## 📋 Table of Contents

- [Types of Contribution](#types-of-contribution)
- [Getting Started](#getting-started)
- [Code Guidelines](#code-guidelines)
- [Submitting a Contribution](#submitting-a-contribution)
- [Reporting Bugs](#reporting-bugs)
- [Requesting Features](#requesting-features)

## 🎯 Types of Contribution

### 📚 Documentation
- Improve explanations of the Zen principles
- Add more practical examples
- Fix language errors
- Translate content to other languages

### 💻 Code
- Add new optimization examples
- Improve existing benchmarks
- Fix bugs in scripts
- Add new use cases

### 🐛 Tests
- Add automated tests
- Verify compatibility with different Python versions
- Test on different operating systems

### 🎨 Design
- Improve documentation formatting
- Create graphical visualizations
- Enhance the presentation of results

## 🚀 Getting Started

### Prerequisites

1. **Python 3.7+** installed
2. **Git** for version control
3. Basic knowledge of Python

### Environment Setup

```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork
git clone https://github.com/seu-usuario/zen-python.git
cd zen-python

# 3. Verify everything works
python src/setup_check.py

# 4. Test the examples
python src/demo_rapido.py
```

### Project Structure

```
zen-python/
├── README.md                          # Main documentation
├── LICENSE                            # MIT License
├── src/                               # 🐍 Python Code
│   ├── zen_python_exemplos.py           # Zen executable scripts
│   ├── exemplos_otimizacao.py           # Benchmark scripts
│   ├── demo_rapido.py                   # Quick demo
│   └── setup_check.py                   # Environment verification
├── docs/                              # 📚 Documentation
│   ├── zen/                           # Zen of Python
│   │   ├── teoria.md                    # Principles theory
│   │   ├── pratica_parte1.md            # Practical examples (1-12)
│   │   └── pratica_parte2.md            # Practical examples (13-19)
│   ├── otimizacao/                    # Optimization
│   │   ├── guia_completo.md             # Optimization guide
│   │   └── referencia_rapida.md         # Cheat sheet
│   ├── CONTRIBUTING.md                  # This file
│   └── CHANGELOG.md                     # Version history
└── config/                            # ⚙️ Configuration
    └── pyproject.toml                   # Project configuration
```

## 📝 Code Guidelines

### Python Code Style

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some adaptations:

```python
# ✅ Good
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

# ❌ Avoid
def fib(n):
    if n<=1:return n
    return fib(n-1)+fib(n-2)
```

### Documentation

- Use docstrings in all functions
- Comment complex code
- Keep comments up to date
- Use emojis to make documentation more visual

### Benchmarks

When adding new benchmarks:

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

## 🔄 Submitting a Contribution

### Pull Request Process

1. **Create a branch for your feature:**
   ```bash
   git checkout -b feature/minha-nova-feature
   ```

2. **Make your changes following the guidelines**

3. **Test your changes:**
   ```bash
   python src/setup_check.py
   python src/exemplos_otimizacao.py  # If you changed benchmarks
   python src/zen_python_exemplos.py  # If you changed Zen examples
   ```

4. **Commit your changes:**
   ```bash
   git add .
   git commit -m "feat: adiciona exemplo de otimização com sets

   - Novo benchmark comparando busca em lista vs set
   - Documentação explicando complexidade O(n) vs O(1)
   - Casos de uso práticos incluídos"
   ```

5. **Push to your fork:**
   ```bash
   git push origin feature/minha-nova-feature
   ```

6. **Open a Pull Request** on GitHub

### Commit Format

We follow the [Conventional Commits](https://www.conventionalcommits.org/) standard:

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `refactor:` - Code refactoring
- `test:` - Add or modify tests
- `chore:` - Maintenance tasks

### What to Include in a PR

- **Clear title** explaining the change
- **Detailed description** of what was changed and why
- **Screenshots** if applicable (for visual changes)
- **Tests** to verify it works as expected
- **Documentation** updated if necessary

## 🐛 Reporting Bugs

### How to Report

1. **Check if the bug has already been reported** in Issues
2. **Use the bug report template**
3. **Include detailed information:**
   - Python version
   - Operating system
   - Steps to reproduce
   - Expected result vs. actual result
   - Logs or error messages

### Report Example

```markdown
**Bug Description**
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

## 🆕 Requesting Features

### Guidelines for Requests

- **Explain the use case** - why is it needed?
- **Describe the proposed solution** - how should it work?
- **Consider alternatives** - are there other approaches?
- **Think about maintainability** - is it sustainable in the long run?

### Types of Desired Features

- ✅ New optimization examples
- ✅ Real-world practical use cases
- ✅ Computational complexity analyses
- ✅ Comparisons with other languages
- ✅ Graphical performance visualizations
- ❌ Features that add unnecessary complexity
- ❌ Heavy external dependencies


## 🙏 Acknowledgments

Contributors will be recognized:

- **README.md** - list of contributors
- **CHANGELOG.md** - credits in releases
- **Issues and PRs** - mentions and thanks

## 📞 Contact

- **Issues**: For bugs and feature requests
- **Discussions**: For general questions
