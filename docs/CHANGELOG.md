# 📝 Changelog

> **Navegação:** [← Voltar ao README](../README.md) | [Guia de Contribuição →](CONTRIBUTING.md)

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-02-08

### 🎉 Lançamento Inicial

#### ✨ Adicionado
- **Zen of Python - Análise Teórica Completa** ([docs/zen/teoria.md](zen/teoria.md))
  - Análise filosófica detalhada dos 19 princípios
  - Contexto histórico e relevância atual
  - Conflitos e paradoxos entre princípios
  - Material didático para professores

- **Zen of Python - Exemplos Práticos**
  - [docs/zen/pratica_parte1.md](zen/pratica_parte1.md) - Princípios 1-12 com exemplos de código
  - [docs/zen/pratica_parte2.md](zen/pratica_parte2.md) - Princípios 13-19 com casos avançados
  - [src/zen_python_exemplos.py](../src/zen_python_exemplos.py) - Scripts executáveis demonstrando cada princípio

- **Otimização de Performance**
  - [docs/otimizacao/guia_completo.md](otimizacao/guia_completo.md) - Guia completo de técnicas de otimização
  - [src/exemplos_otimizacao.py](../src/exemplos_otimizacao.py) - 10 exemplos executáveis com benchmarks reais
  - Comparações de performance cientificamente medidas
  - Análise de complexidade computacional

- **Material de Referência**
  - [docs/otimizacao/referencia_rapida.md](otimizacao/referencia_rapida.md) - Cheat sheet de otimizações comuns
  - [README.md](../README.md) - Documentação principal e índice navegável
  - [src/demo_rapido.py](../src/demo_rapido.py) - Demonstração de 3 minutos dos conceitos principais

- **Infraestrutura do Projeto**
  - [src/setup_check.py](../src/setup_check.py) - Verificação automática de ambiente e dependências
  - [config/pyproject.toml](../config/pyproject.toml) - Configuração profissional do projeto
  - [docs/CONTRIBUTING.md](CONTRIBUTING.md) - Guia detalhado para contribuidores
  - [LICENSE](../LICENSE) - Licença MIT para uso educativo
  - [.gitignore](../.gitignore) - Configuração apropriada para projetos Python

#### 📊 Benchmarks Inclusos

1. **Busca em Coleções**
   - Lista vs Set: demonstra diferença O(n) vs O(1)
   - Speedup típico: 1000-10000x

2. **Concatenação de Strings**  
   - Operador `+` vs `str.join()`
   - Speedup típico: 100-1000x

3. **Remoção de Duplicatas**
   - Loop manual vs `set()` vs `dict.fromkeys()`
   - Speedup típico: 100-500x

4. **Transformação de Listas**
   - Loop+append vs List comprehension vs Map+filter
   - Speedup típico: 30-50%

5. **Operações de Conjunto**
   - Demonstração de união, interseção, diferença
   - Casos práticos com dados reais

6. **Ferramentas Itertools**
   - `product()`, `combinations()`, `chain()`, `groupby()`
   - Exemplos práticos de uso

7. **Collections Especializadas**
   - `Counter` para contagem eficiente
   - `defaultdict` para agrupamento automático

8. **Funções Built-in**
   - `any()`, `all()`, `sum()`, `max()`, `min()`
   - `enumerate()`, `zip()` para iteração eficiente

9. **Generator vs List**
   - Comparação de uso de memória
   - Quando usar cada abordagem

10. **Casos Práticos**
    - Processamento de dados do mundo real
    - Análise de carrinho de compras
    - Mesclagem de informações

#### ⚙️ Características Técnicas

- **Compatibilidade**: Python 3.7+
- **Dependências**: Apenas biblioteca padrão do Python
- **Portabilidade**: Funciona em Windows, Linux, macOS
- **Performance**: Benchmarks otimizados para reprodutibilidade
- **Documentação**: Comentários extensivos em português

#### 📚 Estrutura do Conteúdo

```
zen-python/
├── 📋 README.md                          (Índice e apresentação)
├── 📄 LICENSE                            (Licença MIT)
├── 📂 src/                               🐍 CÓDIGO PYTHON
│   ├── zen_python_exemplos.py              (Scripts do Zen)
│   ├── exemplos_otimizacao.py              (Benchmarks)
│   ├── demo_rapido.py                      (Demo de 3 min)
│   └── setup_check.py                      (Verificação de ambiente)
├── 📂 docs/                              📚 DOCUMENTAÇÃO
│   ├── zen/                              🧘‍♂️ Zen of Python
│   │   ├── teoria.md                       (Análise teórica)
│   │   ├── pratica_parte1.md               (Exemplos 1-12)
│   │   └── pratica_parte2.md               (Exemplos 13-19)
│   ├── otimizacao/                       ⚡ Otimização
│   │   ├── guia_completo.md                (Guia de otimização)
│   │   └── referencia_rapida.md            (Cheat sheet)
│   ├── CONTRIBUTING.md                     (Guia de contribuição)
│   └── CHANGELOG.md                        (Este arquivo)
└── 📂 config/                            ⚙️ CONFIGURAÇÃO
    └── pyproject.toml                      (Config do projeto)
```

## 🤝 Contribuidores

### Versão 1.0.0
- **Core** - Desenvolvimento inicial e documentação

*Para contribuir com o projeto, consulte [CONTRIBUTING.md](./CONTRIBUTING.md).*
