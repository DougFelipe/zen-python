# 📝 Changelog

> **Navegação:** [← Voltar ao Início](index.md) | [Guia de Contribuição →](CONTRIBUTING.md)

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0-alpha] - 2026-02-10

### 🎉 Pré-Lançamento Alpha

#### ✨ Adicionado

##### Zen of Python - Análise Teórica Completa

- Arquivo principal: [zen/teoria.md](zen/teoria.md)
- Análise filosófica detalhada dos 19 princípios
- Contexto histórico e relevância atual
- Conflitos e paradoxos entre princípios
- Material didático para professores

##### Zen of Python - Exemplos Práticos

- [zen/pratica_parte1.md](zen/pratica_parte1.md) - Princípios 1-12 com exemplos de código
- [zen/pratica_parte2.md](zen/pratica_parte2.md) - Princípios 13-19 com casos avançados
- [src/zen_python_exemplos.py](https://github.com/DougFelipe/zen-python/blob/main/src/zen_python_exemplos.py) - Scripts executáveis demonstrando cada princípio

##### Otimização de Performance

- [otimizacao/guia_completo.md](otimizacao/guia_completo.md) - Guia completo de técnicas de otimização
- [src/exemplos_otimizacao.py](https://github.com/DougFelipe/zen-python/blob/main/src/exemplos_otimizacao.py) - 10 exemplos executáveis com benchmarks reais
- Comparações de performance cientificamente medidas
- Análise de complexidade computacional

##### Material de Referência

- [otimizacao/referencia_rapida.md](otimizacao/referencia_rapida.md) - Cheat sheet de otimizações comuns
- [index.md](index.md) - Documentação principal e índice navegável
- [src/demo_rapido.py](https://github.com/DougFelipe/zen-python/blob/main/src/demo_rapido.py) - Demonstração de 3 minutos dos conceitos principais

##### Infraestrutura do Projeto

- [src/setup_check.py](https://github.com/DougFelipe/zen-python/blob/main/src/setup_check.py) - Verificação automática de ambiente e dependências
- [config/pyproject.toml](https://github.com/DougFelipe/zen-python/blob/main/config/pyproject.toml) - Configuração profissional do projeto
- [CONTRIBUTING.md](CONTRIBUTING.md) - Guia detalhado para contribuidores
- [LICENSE](https://github.com/DougFelipe/zen-python/blob/main/LICENSE) - Licença MIT para uso educativo
- [.gitignore](https://github.com/DougFelipe/zen-python/blob/main/.gitignore) - Configuração apropriada para projetos Python

##### CI/CD de Publicação no GitHub Pages

- [`.github/workflows/pages.yml`](https://github.com/DougFelipe/zen-python/blob/main/.github/workflows/pages.yml) criado para pipeline de build e deploy da documentação.
- Execução automática em `push` para `main`, validação em `pull_request` para `main` e execução manual por `workflow_dispatch`.
- Etapa de build com Python 3.12 e `mkdocs build --strict`.
- Instalação das dependências de documentação diretamente de [`config/pyproject.toml`](https://github.com/DougFelipe/zen-python/blob/main/config/pyproject.toml) (grupo `project.optional-dependencies.docs`).
- Publicação automatizada com `actions/configure-pages`, `actions/upload-pages-artifact` e `actions/deploy-pages`.
- Deploy condicionado a `push` em `main` para evitar publicação a partir de PRs.

#### 📊 Benchmarks Inclusos

1. **Busca em Coleções**: Lista vs Set, demonstrando diferença O(n) vs O(1). Speedup típico: 1000-10000x.
2. **Concatenação de Strings**: Operador `+` vs `str.join()`. Speedup típico: 100-1000x.
3. **Remoção de Duplicatas**: Loop manual vs `set()` vs `dict.fromkeys()`. Speedup típico: 100-500x.
4. **Transformação de Listas**: Loop+append vs List comprehension vs Map+filter. Speedup típico: 30-50%.
5. **Operações de Conjunto**: Demonstração de união, interseção e diferença com casos práticos.
6. **Ferramentas Itertools**: `product()`, `combinations()`, `chain()`, `groupby()` com exemplos de uso.
7. **Collections Especializadas**: `Counter` para contagem eficiente e `defaultdict` para agrupamento automático.
8. **Funções Built-in**: `any()`, `all()`, `sum()`, `max()`, `min()`, além de `enumerate()` e `zip()`.
9. **Generator vs List**: Comparação de uso de memória e critérios de quando usar cada abordagem.
10. **Casos Práticos**: Processamento de dados do mundo real, análise de carrinho e mesclagem de informações.

#### ⚙️ Características Técnicas

- **Compatibilidade**: Python 3.7+
- **Dependências**: Apenas biblioteca padrão do Python
- **Portabilidade**: Funciona em Windows, Linux, macOS
- **Performance**: Benchmarks otimizados para reprodutibilidade
- **Documentação**: Comentários extensivos em português

#### 📚 Estrutura do Conteúdo

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

## 🤝 Contribuidores

### Versão 1.0.0-alpha

- **Core** - Desenvolvimento inicial e documentação

*Para contribuir com o projeto, consulte [CONTRIBUTING.md](CONTRIBUTING.md).*
