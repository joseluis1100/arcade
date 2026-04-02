#!/usr/bin/env python3
import os
import shutil
import re

base_dir = "base"
monitoria_dir = "/home/joseluis1100/Documentos/GitHub/monitoriaFUP"

if os.path.exists(base_dir):
    shutil.rmtree(base_dir)
os.makedirs(base_dir)

pdfs = [
    ("PDF 1 - Variaveis e Expressoes", "Variáveis e Expressões", "basic", "wiki/basic/README.md"),
    ("PDF 2 - Comandos Condicionais", "Comandos Condicionais", "if_else", "wiki/if_else/README.md"),
    ("PDF 3 - Comandos de Repeticao", "Comandos de Repetição", "for", "wiki/for/README.md"),
    ("PDF 4 - Vetores e Matrizes", "Vetores e Matrizes", "arrays", "wiki/arrays/README.md"),
    ("PDF 5 - Strings", "Strings", "strings", "wiki/strings/README.md"),
    ("PDF 6 - Structs", "Structs", "structs", "wiki/structs/README.md"),
    ("PDF 7 - Funcoes", "Funções", "functions", "wiki/functions/README.md"),
    ("PDF 8 - Recursao", "Recursão", "recursion", "wiki/recursion/README.md"),
    ("PDF 9 - Ponteiros", "Ponteiros", "pointers", "wiki/pointers/README.md"),
    ("PDF 10 - Alocacao Dinamica", "Alocação Dinâmica", "dynamic_mem", "wiki/dynamic_mem/README.md"),
    ("PDF 11 - Arquivos", "Arquivos", "files", "wiki/files/README.md"),
]

def get_title(ex_folder):
    """Generate short title from folder name"""
    # Clean up folder name to make it readable
    title = ex_folder.replace('_', ' ').replace('-', ' ')
    return title

seen_names = {}
name_counter = {}

def unique_name(name, pdf_idx):
    key = (name, pdf_idx)
    if key in seen_names:
        return seen_names[key]
    
    dst = os.path.join(base_dir, name)
    if os.path.exists(dst):
        if name not in name_counter:
            name_counter[name] = 1
        else:
            name_counter[name] += 1
        new_name = f"{name}_{name_counter[name]}"
        seen_names[key] = new_name
    else:
        seen_names[key] = name
    return seen_names[key]

open_exercises = {
    "leitura", "escreve", "exibe", "copiaarq", "entradasaida", "dataarq",
    "idadearq", "nomearq", "infoarq", "numeros", "merge", "palavrasarq",
    "buscaarq", "filtraarq", "registroarq", "notasarq", "linhasarq",
    "lebinario", "binarioarq", "boletimarq", "contatos", "controle",
    "banco", "processa", "relatorio", "vendasarq", "substituiarq",
    "upperarq", "maiorarq",
    "quiz", "crescente", "tabela", "lanchonete", "aumento", "faltas", "data",
    "comissao", "parking", "datalimite", "faixa", "carro", "imc",
    "aleatorio", "cadastro", "estatistica", "folha", "menu", "boletim",
    "programas", "preenche", "turma", "seriemat", "ponderada",
    "pessoa", "idadef", "horario", "turma_st", "contato", "endereco", "veiculo",
    "livros", "filmes", "voos", "telefone", "receitas", "estoque", "garagem",
    "agenda", "diasentre", "energia", "complexos", "polar", "vetor3d",
}

name_map = {}
exercise_data = []

for pdf_idx, (pdf_name, topic_name, tag, wiki_link) in enumerate(pdfs):
    pdf_path = os.path.join(monitoria_dir, pdf_name)
    exercises = [f for f in os.listdir(pdf_path) if f != 'README.md']
    
    pdf_exercises = []
    for ex in exercises:
        src = os.path.join(pdf_path, ex)
        unique_ex = unique_name(ex, pdf_idx)
        dst = os.path.join(base_dir, unique_ex)
        if not os.path.exists(dst):
            shutil.copytree(src, dst)
        
        # Get title
        title = get_title(ex)
        name_map[(ex, pdf_idx)] = (unique_ex, title)
        pdf_exercises.append((ex, unique_ex, title))
    
    exercise_data.append({
        "topic": topic_name,
        "tag": tag,
        "wiki": wiki_link,
        "exercises": pdf_exercises
    })

output = """# Monitoria FUP - Fundamentos de Programação

Repositório de exercícios de programação em linguagem C para a disciplina de Fundamentos de Programação.
Descrição do marcadores [LINK](https://github.com/senapk/tko/blob/master/wiki/Marcadores-e-Tipos.md)

"""

prev_tag = None

for i, data in enumerate(exercise_data):
    topic_name = data["topic"]
    tag = data["tag"]
    wiki_link = data["wiki"]
    exercises = data["exercises"]
    
    output += f"## {topic_name} +{tag} @{tag}"
    if prev_tag:
        output += f" !@{prev_tag}"
    output += "\n\n"
    
    output += f"- [ ] `@teoria_{tag} :1:main:user:view:free`[Teoria]({wiki_link})\n"
    
    for j, (ex, unique_ex, title) in enumerate(exercises):
        idx = j + 1
        
        if ex in open_exercises:
            marker = f":{min(idx,3)}:main:user:view:free"
        elif idx <= 5:
            marker = ":1:main:auto:edit:part"
        elif idx <= 20:
            marker = ":2:main:auto:edit:part"
        elif idx <= 40:
            marker = ":3:main:auto:edit:part"
        else:
            marker = ":3:side:auto:edit:part"
        
        output += f"- [ ] `@{unique_ex} {marker}`[{idx:02d} - {title}](base/{unique_ex}/README.md)\n"
    
    output += "\n"
    prev_tag = tag

output += "## sandbox\n"

with open("README.md", "w") as f:
    f.write(output)

total = sum(len(d["exercises"]) for d in exercise_data)
print(f"README.md generated! Total: {total} exercises")
