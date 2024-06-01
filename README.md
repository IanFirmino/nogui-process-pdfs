# Processar e juntar PDFs de Holerite e Pagamento

## Instalação

### Pré-requisitos
- Python 3.x

## Uso
*Execute pelo terminal utilizando o executavel em /dist
*database.json deve estar no mesmo caminho do main.exe

- Executar para um Colaborador:
- 
```main.exe run```

Isso executará o script para um colaborador específico.

- Executar para Todos os Colaboradores:

```main.exe run_all```

Isso executará o script para todos os colaboradores listados em colaboradores.

- Adicionar um Novo Colaborador:
- 
```main.exe add_colaborador```

Isso permitirá adicionar um novo colaborador à lista de colaboradores.

- Remover um Colaborador Existente:
  
```main.exe remove_colaborador```

Isso removerá um colaborador existente da lista de colaboradores.

- Listar Todos os Colaboradores:
  
```main.exe list_colaboradores```

Isso exibirá uma lista de todos os colaboradores atualmente cadastrados.

- Alterar Caminho Onde os Arquivos são Salvos:
  
```main.exe change_save_path```

Isso alterará a pasta onde os PDFs devem ser salvos.

- Alterar o Arquivo dos Holerites:
  
```main.exe change_holerite_path```

Isso alterará o arquivo que estão os holerites.

- Alterar o Arquivo dos Pagamentos:
  
```main.exe change_pagamento_path```

Isso alterará a arquivo que estão os pagamentos.

- Listar o caminho de configurações:
  
```main.exe list_paths```

Isso listará o caminho do holerite, pagamento e da pasta onde deve ser salvo os arquivos.
