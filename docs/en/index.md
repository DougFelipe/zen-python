# Zen Python - Educational Repository

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

> **A theoretical and practical guide on Python's fundamental principles and code optimization techniques.**

This repository is a resource for consolidating essential Python concepts, from the philosophical principles of the "Zen of Python" to performance optimization techniques.

## 📋 Table of Contents

- [🎯 About the Project](#about-the-project)
- [📚 Repository Content](#repository-content)
- [🚀 How to Use](#how-to-use)
- [📖 Study Guides](#study-guides)
- [⚡ Quick Start](#quick-start)
- [💻 Runnable Examples](#runnable-examples)
- [🔧 Requirements](#requirements)
- [📈 Benchmarks](#benchmarks)
- [🤝 Contributing](#contributing)

## 🎯 About the Project

This repository was created to:

- ✅ **Understand** the principles of the Zen of Python (PEP 20)
- ✅ **Apply optimization techniques** for more efficient code
- ✅ **Develop Pythonic code** following best practices
- ✅ **Compare performance** between different approaches
- ✅ **Have a practical reference** for quick lookups

## 📚 Repository Content

### 🧘 Zen of Python

> *Understand the philosophy that makes Python unique*

**📚 Theory**

Start here to understand the fundamentals:

- [**Complete Theoretical Analysis**](zen/teoria.md)
- The 19 principles explained in depth

**💡 Practice**

See the principles applied in real code:

- [**Examples Part 1**](zen/pratica_parte1.md) — Principles 1-12
- [**Examples Part 2**](zen/pratica_parte2.md) — Principles 13-19
- [**▶️ Runnable Code**](https://github.com/DougFelipe/zen-python/blob/main/src/zen_python_exemplos.py)

### ⚡ Performance Optimization

> *Write Python code up to 1000x faster*

**📚 Learn**

Complete guides with detailed explanations:

- [**Complete Guide**](otimizacao/guia_completo.md)
- Step-by-step optimization techniques

**📋 Reference**

Quick references for everyday use:

- [**Cheat Sheet**](otimizacao/referencia_rapida.md) — Optimized replacements
- [**▶️ Benchmarks**](https://github.com/DougFelipe/zen-python/blob/main/src/exemplos_otimizacao.py) — Test it yourself

## 📖 Study Guides

### Zen of Python Track

1. [Complete Theory](zen/teoria.md)
2. [Practice Part 1](zen/pratica_parte1.md)
3. [Practice Part 2](zen/pratica_parte2.md)

### Optimization Track

1. [Complete Guide](otimizacao/guia_completo.md)
2. [Quick Reference](otimizacao/referencia_rapida.md)

## 💻 Runnable Examples

- [Zen of Python - practical examples](https://github.com/DougFelipe/zen-python/blob/main/src/zen_python_exemplos.py)
- [Optimization benchmarks](https://github.com/DougFelipe/zen-python/blob/main/src/exemplos_otimizacao.py)
- [Quick demo](https://github.com/DougFelipe/zen-python/blob/main/src/demo_rapido.py)
- [Environment validation](https://github.com/DougFelipe/zen-python/blob/main/src/setup_check.py)

## 🚀 How to Use

### 📖 Study

1. [Zen Theory](zen/teoria.md)
2. [Practical Examples](zen/pratica_parte1.md)

### 💻 Run

```bash
python src/zen_python_exemplos.py
python src/exemplos_otimizacao.py
```

### 📋 Reference

[Cheat Sheet](otimizacao/referencia_rapida.md)

## ⚡ Quick Start

> *Get started in less than 5 minutes*

```bash
python src/setup_check.py             # 1. Check environment
python src/demo_rapido.py             # 2. Quick demo (2-3 min)
python src/zen_python_exemplos.py     # 3. Zen examples
python src/exemplos_otimizacao.py     # 4. Full benchmarks
```

## 🔧 Requirements

### Python Version

- **Python 3.7+** (3.8+ recommended)

### Internal Dependencies

All examples use only the Python **standard library**:

- `timeit` - For performance benchmarks
- `itertools` - For advanced iteration operations
- `collections` - For specialized data structures
- `operator` - For operator functions
- `random` - For test data generation

### Installation

```bash
# No additional installation required!
# Just Python 3.7+ is enough
python --version  # Check your version
```

## 📈 Benchmarks

### 🔍 Key Findings

| Operation | Slow Approach | Fast Approach | Speedup |
|-----------|---------------|---------------|---------|
| Search | Loop over list | `in` with set | **1000-10000x** |
| Concatenation | Repeated `+` | `str.join()` | **100-1000x** |
| Transformation | Loop + append | List comprehension | **30-50%** |
| Duplicates | Manual loop | `set()` or `dict.fromkeys()` | **100-500x** |

## 🎯 Key Takeaways

### 🧘 From the Zen of Python

1. **Beautiful is better than ugly** - Clean code is easier to maintain
2. **Explicit is better than implicit** - Clarity reduces bugs
3. **Simple is better than complex** - Simplicity is elegance
4. **Readability counts** - Code is read more often than written
5. **There should be one obvious way to do it** - Consistency facilitates collaboration

### ⚡ From Optimization

1. **Use `set` for lookups** - 100-10000x faster than lists
2. **Use `str.join()` for concatenation** - 100-1000x faster than `+`
3. **Use list comprehensions** - Cleaner and 30-50% faster
4. **Use `itertools`** - Powerful tools for complex iterations
5. **Use `Counter`** - Simpler and more efficient for counting
6. **Use generators** - Save memory with large datasets
7. **Use built-in functions** - `any()`, `all()`, `sum()`, `max()`, `min()`

## 🏗️ Project Structure

```text
zen-python/
├── README.md
├── LICENSE
├── .gitignore
├── src/
│   ├── zen_python_exemplos.py
│   ├── exemplos_otimizacao.py
│   ├── demo_rapido.py
│   └── setup_check.py
├── docs/
│   ├── zen/
│   │   ├── teoria.md
│   │   ├── pratica_parte1.md
│   │   └── pratica_parte2.md
│   ├── otimizacao/
│   │   ├── guia_completo.md
│   │   └── referencia_rapida.md
│   ├── CONTRIBUTING.md
│   └── CHANGELOG.md
└── config/
    └── pyproject.toml
```

## 🎓 For Structured Teaching

### 📚 Features

- ✅ Integrated Theory + Practice
- ✅ Progression from basic to advanced
- ✅ Benchmarks with real metrics
- ✅ Real-world examples

### 🎯 Usage Suggestions

| Activity | Material |
|----------|----------|
| Introductory lecture | [Theory](zen/teoria.md) |
| Lab session | [▶️ Zen Examples](https://github.com/DougFelipe/zen-python/blob/main/src/zen_python_exemplos.py) |
| Workshop | [▶️ Benchmarks](https://github.com/DougFelipe/zen-python/blob/main/src/exemplos_otimizacao.py) |
| Reference | [Cheat Sheet](otimizacao/referencia_rapida.md) |

## 🤝 Contributing

> *Contributions are welcome!*

### 💻 Development

- New examples
- Improve benchmarks
- Fix bugs

### 📚 Documentation

- Improve explanations
- New use cases
- Translations

### 🐛 Feedback

- Report issues
- Suggest improvements
- Test on different systems

📜 [**Contributing Guide**](CONTRIBUTING.md) · 📋 [**Changelog**](CHANGELOG.md)

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🙏 Acknowledgments

- **Tim Peters** - Creator of the Zen of Python (PEP 20)
- **Guido van Rossum** - Creator of Python
- **Python Community** - For the principles and best practices

## 🔗 Useful Links

[PEP 20 - Zen of Python](https://www.python.org/dev/peps/pep-0020/) · [PEP 8 - Style Guide](https://www.python.org/dev/peps/pep-0008/) · [Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips) · [Python Docs](https://docs.python.org/)

---

> **💡 "Simple is better than complex. Complex is better than complicated."**
> *— The Zen of Python*
