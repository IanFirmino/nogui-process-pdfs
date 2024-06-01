import json

def load_db():
    with open('database.json', 'r') as json_file:
        return json.load(json_file)

def save_bd(data):
    with open('database.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

def change_save_path():
    print('WARINIG: O caminho do arquivo não deve conter caracteres especiais.')
    new_path = input("Nova pasta para salvamento dos PDFs: ").strip()
    bd = load_db()
    if 'save_path' in bd['paths']:
        bd['paths']['save_path'] = new_path.replace("\\", "/")
        save_bd(bd)
    else:
        print(f"O caminho save_path não existe.")
    print('save_path Alterado com sucesso!')

def change_holerite_path():
    print('WARINIG: O caminho do arquivo não deve conter caracteres especiais.')
    new_path = input("Nova caminho do arquivo Holerites: ").strip()
    bd = load_db()
    if 'holerite_path' in bd['paths']:
        bd['paths']['holerite_path'] = new_path.replace("\\", "/")
        save_bd(bd)
    else:
        print(f"O caminho holerite_path não existe.")
    print('holerite_path Alterado com sucesso!')

def change_pagamento_path():
    print('WARINIG: O caminho do arquivo não deve conter caracteres especiais.')
    new_path = input("Nova caminho do arquivo Pagamentos: ").strip()
    bd = load_db()
    if 'pagamento_path' in bd['paths']:
        bd['paths']['pagamento_path'] = new_path.replace("\\", "/")
        save_bd(bd)
    else:
        print(f"O caminho pagamento_path não existe.")
    print('pagamento_path Alterado com sucesso!')

def add_colaborador():
    colaborador = input("Adicionar colaborador: ").strip()
    bd = load_db()
    bd['colaboradores'].append(colaborador)
    save_bd(bd)
    print('Colaborador salvo com sucesso!')

def remove_colaborador():
    colaborador = input("Remover colaborador: ").strip()
    bd = load_db()
    if colaborador in bd['colaboradores']:
        bd['colaboradores'].remove(colaborador)
        save_bd(bd)
        print('Colaborador removido com sucesso!')
    else:
        print(f"O colaborador '{colaborador}' não está na lista.")

def get_all_colaboradores():
    db = load_db()
    return db.get('colaboradores', [])

def list_colaboradores():
    bd = load_db()
    colaboradores = bd['colaboradores']
    print("Lista de Colaboradores:")
    for colaborador in colaboradores:
        print(colaborador)

def list_paths():
    bd = load_db()
    paths = bd['paths']
    print("Lista de Paths:")
    for path_name, path_value in paths.items():
        print(f"{path_name}: {path_value}")

def get_paths():
    db = load_db()
    return db.get('paths', {})