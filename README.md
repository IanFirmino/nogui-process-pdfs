# Automação RH v1

## Instalação

### Pré-requisitos
- Python 3.x

### Passos para Instalar

1. **Baixar e Extrair o Projeto**:
   - Coloque os arquivos do projeto em um diretório, por exemplo, `C:\Projetos\automacao_rh_v1`.

2. **Instalar Dependências**:
   - Abra o terminal (ou Prompt de Comando no Windows).
   - Navegue até o diretório onde o projeto foi extraído:
     - cd C:\Projetos\automacao_rh_v1
   
   - Instale as dependências listadas em `requirements.txt`:
     - pip install .

## Uso

- Executar para um Colaborador:
python main.py run
Isso executará o script para um colaborador específico.

- Executar para Todos os Colaboradores:
python main.py run_all
Isso executará o script para todos os colaboradores listados em colaboradores.

- Adicionar um Novo Colaborador:
python main.py add_colaborador
Isso permitirá adicionar um novo colaborador à lista de colaboradores.

- Remover um Colaborador Existente:
python main.py remove_colaborador
Isso removerá um colaborador existente da lista de colaboradores.

- Listar Todos os Colaboradores:
python main.py list_colaboradores
Isso exibirá uma lista de todos os colaboradores atualmente cadastrados.

- Alterar Caminho Onde os Arquivos são Salvos:
python main.py change_save_path
Isso alterará a pasta onde os PDFs devem ser salvos.

- Alterar o Arquivo dos Holerites:
python main.py change_holerite_path
Isso alterará o arquivo que estão os holerites.

- Alterar o Arquivo dos Pagamentos:
python main.py change_pagamento_path
Isso alterará a arquivo que estão os pagamentos.

- Listar o caminho de configurações:
python main.py list_paths
Isso listará o caminho do holerite, pagamento e da pasta onde deve ser salvo os arquivos.