#!/usr/bin/env python3
"""
Script de Verificação e Configuração
Execute: python setup_check.py
"""

import sys
import os
import importlib
from pathlib import Path

def verificar_python():
    """Verifica se a versão do Python é adequada."""
    print("🔍 Verificando versão do Python...")
    version = sys.version_info
    
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print(f"❌ Python {version.major}.{version.minor} não é suportado")
        print("   Versão mínima: Python 3.7")
        return False
    else:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True

def verificar_modulos():
    """Verifica se todos os módulos necessários estão disponíveis."""
    print("\n🔍 Verificando módulos necessários...")
    
    modulos_necessarios = [
        'timeit',
        'itertools', 
        'collections',
        'operator',
        'random',
        'json',
        'dataclasses',
        'typing'
    ]
    
    erros = []
    
    for modulo in modulos_necessarios:
        try:
            importlib.import_module(modulo)
            print(f"✅ {modulo} - OK")
        except ImportError:
            print(f"❌ {modulo} - ERRO")
            erros.append(modulo)
    
    return len(erros) == 0

def verificar_arquivos():
    """Verifica se todos os arquivos necessários estão presentes."""
    print("\n🔍 Verificando arquivos do repositório...")
    
    # Usar o diretório pai (raiz do projeto) como referência
    projeto_raiz = Path(__file__).parent.parent
    
    arquivos_necessarios = [
        'README.md',
        'LICENSE',
        'src/zen_python_exemplos.py',
        'src/exemplos_otimizacao.py',
        'src/demo_rapido.py', 
        'src/setup_check.py',
        'docs/zen/teoria.md',
        'docs/zen/pratica_parte1.md',
        'docs/zen/pratica_parte2.md',
        'docs/otimizacao/guia_completo.md',
        'docs/otimizacao/referencia_rapida.md',
        'docs/CONTRIBUTING.md',
        'docs/CHANGELOG.md',
        'config/pyproject.toml',
        '.gitignore'
    ]
    
    erros = []
    
    for arquivo in arquivos_necessarios:
        caminho_completo = projeto_raiz / arquivo
        if caminho_completo.exists():
            print(f"✅ {arquivo} - OK")
        else:
            print(f"❌ {arquivo} - AUSENTE")
            erros.append(arquivo)
    
    return len(erros) == 0

def teste_import_scripts():
    """Testa se os scripts Python podem ser importados sem erro."""
    print("\n🔍 Testando importação dos scripts...")
    
    # Adiciona o diretório src ao path
    projeto_raiz = Path(__file__).parent.parent
    src_dir = projeto_raiz / 'src'
    
    scripts = [
        'zen_python_exemplos',
        'exemplos_otimizacao', 
        'demo_rapido'
    ]
    
    erros = []
    
    for script in scripts:
        try:
            # Adiciona o diretório src ao path temporariamente
            sys.path.insert(0, str(src_dir))
            importlib.import_module(script)
            print(f"✅ {script}.py - OK")
        except Exception as e:
            print(f"❌ {script}.py - ERRO: {str(e)[:50]}...")
            erros.append(script)
        finally:
            # Remove o diretório do path
            if str(src_dir) in sys.path:
                sys.path.remove(str(src_dir))
    
    return len(erros) == 0

def mostrar_info_sistema():
    """Mostra informações do sistema."""
    print("\n📊 INFORMAÇÕES DO SISTEMA")
    print("-" * 50)
    print(f"Python: {sys.version}")
    print(f"Plataforma: {sys.platform}")
    print(f"Diretório: {os.getcwd()}")

def mostrar_comandos_uteis():
    """Mostra comandos úteis para uso do repositório."""
    print("\n🎯 COMANDOS ÚTEIS")
    print("-" * 50)
    print("""
# Demo rápido (2-3 minutos):
python src/demo_rapido.py

# Exemplos completos do Zen of Python:
python src/zen_python_exemplos.py

# Benchmarks de otimização (pode levar alguns minutos):
python src/exemplos_otimizacao.py

# Visualizar documentação:
# Windows:
type README.md
type docs\\zen\\teoria.md

# Linux/Mac:
cat README.md
cat docs/zen/teoria.md
    """)

def main():
    print("="*60)
    print("🐍 ZEN PYTHON - VERIFICAÇÃO DE CONFIGURAÇÃO")
    print("="*60)
    
    tudo_ok = True
    
    # Verificações
    if not verificar_python():
        tudo_ok = False
    
    if not verificar_modulos():
        tudo_ok = False
    
    if not verificar_arquivos():
        tudo_ok = False
    
    if not teste_import_scripts():
        tudo_ok = False
    
    # Informações do sistema
    mostrar_info_sistema()
    
    # Resultado final
    print("\n" + "="*60)
    if tudo_ok:
        print("✅ TUDO CONFIGURADO CORRETAMENTE!")
        print("   Você pode executar todos os exemplos sem problemas.")
        mostrar_comandos_uteis()
    else:
        print("❌ ALGUNS PROBLEMAS FORAM ENCONTRADOS")
        print("   Verifique os erros acima antes de continuar.")
    print("="*60)

if __name__ == "__main__":
    main()