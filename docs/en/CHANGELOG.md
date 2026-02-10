# 📝 Changelog

> **Navigation:** [← Back to Home](index.md) | [Contributing Guide →](CONTRIBUTING.md)

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0-alpha] - 2026-02-10

### 🎉 Alpha Pre-Release

#### ✨ Added

##### Zen of Python - Complete Theoretical Analysis

- Main file: [zen/teoria.md](zen/teoria.md)
- Detailed philosophical analysis of the 19 principles
- Historical context and current relevance
- Conflicts and paradoxes between principles
- Teaching material for instructors

##### Zen of Python - Practical Examples

- [zen/pratica_parte1.md](zen/pratica_parte1.md) - Principles 1-12 with code examples
- [zen/pratica_parte2.md](zen/pratica_parte2.md) - Principles 13-19 with advanced cases
- [src/zen_python_exemplos.py](https://github.com/DougFelipe/zen-python/blob/main/src/zen_python_exemplos.py) - Executable scripts demonstrating each principle

##### Performance Optimization

- [otimizacao/guia_completo.md](otimizacao/guia_completo.md) - Complete guide to optimization techniques
- [src/exemplos_otimizacao.py](https://github.com/DougFelipe/zen-python/blob/main/src/exemplos_otimizacao.py) - 10 executable examples with real benchmarks
- Scientifically measured performance comparisons
- Computational complexity analysis

##### Reference Material

- [otimizacao/referencia_rapida.md](otimizacao/referencia_rapida.md) - Common optimizations cheat sheet
- [index.md](index.md) - Main documentation and navigable index
- [src/demo_rapido.py](https://github.com/DougFelipe/zen-python/blob/main/src/demo_rapido.py) - 3-minute demonstration of the main concepts

##### Project Infrastructure

- [src/setup_check.py](https://github.com/DougFelipe/zen-python/blob/main/src/setup_check.py) - Automatic environment and dependency verification
- [config/pyproject.toml](https://github.com/DougFelipe/zen-python/blob/main/config/pyproject.toml) - Professional project configuration
- [CONTRIBUTING.md](CONTRIBUTING.md) - Detailed guide for contributors
- [LICENSE](https://github.com/DougFelipe/zen-python/blob/main/LICENSE) - MIT License for educational use
- [.gitignore](https://github.com/DougFelipe/zen-python/blob/main/.gitignore) - Appropriate configuration for Python projects

##### GitHub Pages Publishing CI/CD

- [`.github/workflows/pages.yml`](https://github.com/DougFelipe/zen-python/blob/main/.github/workflows/pages.yml) created for the documentation build and deploy pipeline.
- Automatic execution on `push` to `main`, validation on `pull_request` to `main`, and manual execution via `workflow_dispatch`.
- Build step with Python 3.12 and `mkdocs build --strict`.
- Documentation dependencies installed directly from [`config/pyproject.toml`](https://github.com/DougFelipe/zen-python/blob/main/config/pyproject.toml) (`project.optional-dependencies.docs` group).
- Automated publishing with `actions/configure-pages`, `actions/upload-pages-artifact`, and `actions/deploy-pages`.
- Deploy conditioned to `push` on `main` to prevent publishing from PRs.

#### 📊 Included Benchmarks

1. **Collection Search**: List vs Set, demonstrating O(n) vs O(1) difference. Typical speedup: 1000-10000x.
2. **String Concatenation**: `+` operator vs `str.join()`. Typical speedup: 100-1000x.
3. **Duplicate Removal**: Manual loop vs `set()` vs `dict.fromkeys()`. Typical speedup: 100-500x.
4. **List Transformation**: Loop+append vs List comprehension vs Map+filter. Typical speedup: 30-50%.
5. **Set Operations**: Demonstration of union, intersection, and difference with practical cases.
6. **Itertools Utilities**: `product()`, `combinations()`, `chain()`, `groupby()` with usage examples.
7. **Specialized Collections**: `Counter` for efficient counting and `defaultdict` for automatic grouping.
8. **Built-in Functions**: `any()`, `all()`, `sum()`, `max()`, `min()`, plus `enumerate()` and `zip()`.
9. **Generator vs List**: Memory usage comparison and criteria for when to use each approach.
10. **Practical Cases**: Real-world data processing, cart analysis, and information merging.

#### ⚙️ Technical Characteristics

- **Compatibility**: Python 3.7+
- **Dependencies**: Python standard library only
- **Portability**: Works on Windows, Linux, macOS
- **Performance**: Benchmarks optimized for reproducibility
- **Documentation**: Extensive comments in Portuguese

#### 📚 Content Structure

```text
zen-python/
├── README.md
├── LICENSE
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

## 🤝 Contributors

### Version 1.0.0-alpha

- **Core** - Initial development and documentation

*To contribute to the project, see [CONTRIBUTING.md](CONTRIBUTING.md).*
