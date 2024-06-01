import PyPDF2
import os
import re
import sys
from db import add_colaborador, remove_colaborador, list_colaboradores, list_paths, get_all_colaboradores, get_paths, change_save_path, change_holerite_path, change_pagamento_path

paths = get_paths()
holerite_path = paths.get('holerite_path', '')
pagamento_path = paths.get('pagamento_path', '')
save_path = paths.get('save_path', '')

def run_all_colaboradores():
    colaboradores = get_all_colaboradores()
    print("Script iniciado!")
    for colaborador in colaboradores:
        if colaborador is None or colaborador == '':
            continue
        result = run_by_colaborador(colaborador, holerite_path, pagamento_path, save_path)
        print(result)
    print("Script finalizado!")

def run():
    colaborador = input("Digite o nome do colaborador: ").strip()
    result = run_by_colaborador(colaborador, holerite_path, pagamento_path, save_path)
    print(result)

def run_by_colaborador(colaborador, holerite_path, pagamento_path, save_path):
    output_file_with_colab = os.path.join(save_path, f'holerite_e_pagamento_com_colab_{colaborador}.pdf')

    if os.path.isfile(holerite_path) and os.path.isfile(pagamento_path):
        with open(holerite_path, 'rb') as holerite_file, open(pagamento_path, 'rb') as pagamento_file:
            holerite_pdf = PyPDF2.PdfReader(holerite_file)
            pagamento_pdf = PyPDF2.PdfReader(pagamento_file)

            holerite_top_half, holerite_bottom_half = extract_relevant_part(holerite_pdf, colaborador)
            pagamento_top_half, pagamento_bottom_half = extract_relevant_part(pagamento_pdf, colaborador)
        
            if holerite_top_half is None and pagamento_top_half is not None:
                return f"{colaborador}: não encontrado no arquivo Holerite"

            if pagamento_top_half is None and holerite_top_half is not None:
                return f"{colaborador}: não encontrado no arquivo Pagamento"

            if holerite_top_half is None and pagamento_top_half is None:
                return f"{colaborador}: não encontrado no arquivo Holerite e Pagamento"

            #create_distinct_parts(holerite_top_half, holerite_bottom_half, pagamento_top_half, pagamento_bottom_half, save_path)
            result = extract_and_merge(holerite_top_half, holerite_bottom_half, pagamento_top_half, pagamento_bottom_half, colaborador, output_file_with_colab)
    else:
        return "Arquivos PDF não encontrados."
    return f"{colaborador}: {result}"

def find_colaborador_page(pdf, colaborador):
    colaborador = re.sub(r'\s+', ' ', colaborador.strip())
    colaborador_pattern = re.compile(re.escape(colaborador), re.IGNORECASE)
    for page_num, page in enumerate(pdf.pages):
        text = page.extract_text()
        text = re.sub(r'\s+', ' ', text.strip())
        if colaborador_pattern.search(text):
            return page_num 
    return None

def extract_relevant_part(pdf, colaborador, colaborador_page = None):
    if colaborador_page == None:
        colaborador_page = find_colaborador_page(pdf, colaborador)
        
    if colaborador_page is not None:
        page = pdf.pages[colaborador_page]
        (w, h) = page.mediabox.upper_right
        mid = h / 2

        top_half = PyPDF2.PageObject.create_blank_page(width=w, height=h)
        bottom_half = PyPDF2.PageObject.create_blank_page(width=w, height=h)

        top_half.merge_page(page)
        bottom_half.merge_page(page)

        top_half.cropbox.lower_left = (0, mid)
        top_half.cropbox.upper_right = (w, h)

        bottom_half.cropbox.lower_left = (0, 0)
        bottom_half.cropbox.upper_right = (w, mid)

        return top_half, bottom_half
    return None, None

def create_pdf_with_parts(parts, output_file):
    with PyPDF2.PdfWriter() as pdf_writer:
        for part in parts:
            if part:
                pdf_writer.add_page(part)
        with open(output_file, 'wb') as output:
            pdf_writer.write(output)
    return f"PDF criado com sucesso em: {output_file}"

def extract_and_merge(holerite_top_half, holerite_bottom_half, pagamento_top_half, pagamento_bottom_half, colaborador, output_file_with_colab):
    parts_with_colab = []
    colaborador = colaborador.lower()
    
    #print(holerite_top_half.extract_text())
    #holerite_top = re.search(colaborador, holerite_top_half.extract_text(), re.IGNORECASE)
    holerite_parts = holerite_bottom_half.extract_text().split('_____/_____/__________ Assinatura:')
    holerite_top = holerite_parts[0].strip().lower()
    holerite_top = re.sub(r'\s+', ' ', holerite_top.strip())
    if colaborador in holerite_top:
        parts_with_colab.append(holerite_top_half)
    else:
        parts_with_colab.append(holerite_bottom_half)

    #pagamento_top = re.search(colaborador, pagamento_top_half.extract_text(), re.IGNORECASE)
    pagamento_parts = pagamento_bottom_half.extract_text().split('Cortar  aqui')
    pagamento_top = pagamento_parts[0].strip().lower()
    pagamento_top = re.sub(r'\s+', ' ', pagamento_top.strip())
    if colaborador in pagamento_top:
        parts_with_colab.append(pagamento_top_half)
    else:
        parts_with_colab.append(pagamento_bottom_half)

    return create_pdf_with_parts(parts_with_colab, output_file_with_colab)

def create_distinct_parts(holerite_top_half, holerite_bottom_half, pagamento_top_half, pagamento_bottom_half, save_path):
    holerite_top_temp_file = os.path.join(save_path, 'holerite_top_temp.pdf')
    with open(holerite_top_temp_file, 'wb') as holerite_top_temp:
        holerite_top_writer = PyPDF2.PdfWriter()
        holerite_top_writer.add_page(holerite_top_half)
        holerite_top_writer.write(holerite_top_temp)
    holerite_bottom_temp_file = os.path.join(save_path, 'holerite_bottom_temp.pdf')
    with open(holerite_bottom_temp_file, 'wb') as holerite_bottom_temp:
        holerite_bottom_writer = PyPDF2.PdfWriter()
        holerite_bottom_writer.add_page(holerite_bottom_half)
        holerite_bottom_writer.write(holerite_bottom_temp)

    pagamento_top_temp_file = os.path.join(save_path, 'pagamento_top_temp.pdf')
    with open(pagamento_top_temp_file, 'wb') as pagamento_top_temp:
        pagamento_top_writer = PyPDF2.PdfWriter()
        pagamento_top_writer.add_page(pagamento_top_half)
        pagamento_top_writer.write(pagamento_top_temp)
    pagamento_bottom_temp_file = os.path.join(save_path, 'pagamento_bottom_temp.pdf')
    with open(pagamento_bottom_temp_file, 'wb') as pagamento_bottom_temp:
        pagamento_bottom_writer = PyPDF2.PdfWriter()
        pagamento_bottom_writer.add_page(pagamento_bottom_half)
        pagamento_bottom_writer.write(pagamento_bottom_temp)

def help_command():
    print("Comandos disponíveis: *pre-fix main.exe*")
    help_functions = {
        'run' : 'Isso executará o script para um colaborador específico.',
        'run_all' : 'Isso executará o script para todos os colaboradores listados em colaboradores.',
        'add_colaborador' : 'Isso permitirá adicionar um novo colaborador à lista de colaboradores.',
        'remove_colaborador' : 'Isso removerá um colaborador existente da lista de colaboradores.',
        'list_colaboradores' : 'Isso exibirá uma lista de todos os colaboradores atualmente cadastrados.',
        'change_save_path' : 'Isso alterará a pasta onde os PDFs devem ser salvos.',
        'change_holerite_path' : 'Isso alterará o arquivo que estão os Holerites.',
        'change_pagamento_path' : 'Isso alterará a arquivo que estão os Pagamentos.',
        'list_paths' : 'Isso listará o caminho do holerite, pagamento e da pasta onde deve ser salvo os arquivos.',
        'help' : 'Isso listará todos os comandos disponíveis.'
    }
    for command, description in help_functions.items():
        print(f"- {command}: {description}")

functions = {
    'run': run,
    'run_all': run_all_colaboradores,
    'add_colaborador': add_colaborador,
    'remove_colaborador': remove_colaborador,
    'list_colaboradores': list_colaboradores,
    'change_save_path': change_save_path,
    'change_holerite_path': change_holerite_path,
    'change_pagamento_path': change_pagamento_path,
    'list_paths': list_paths,
    'help': help_command
}

if __name__ == "__main__":
    function_name = sys.argv[1] 
    
    if len(sys.argv) >= 3:
        args = sys.argv[2:]
    else:
        args = []

    if function_name in functions:
        function = functions[function_name]
        function(*args)
    else:
        print(f"função '{function_name}' não existe.")