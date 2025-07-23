# ERWIN_PY

Estrutura do projeto Python para integração com erwin Data Modeler.

## Estrutura de Diretórios

erwin_py/
│
├── attributes/               # Operações com atributos
│   ├── attribute_alter.py    # Modificação de atributos
│   ├── attribute_created.py  # Criação de atributos
│   ├── attribute_deleted.py  # Exclusão de atributos (versão atual)
│   ├── attribute_deleted_Old.py  # Versão legada
│   └── attribute_read.py     # Leitura de atributos
│
├── entities/                 # Operações com entidades
│   ├── entity_alter.py       # Modificação de entidades
│   ├── entity_created.py     # Criação de entidades
│   ├── entity_deleted.py     # Exclusão de entidades
│   └── entity_read.py        # Leitura de entidades
│
├── __pycache__/              # Cache Python (ignorar)
├── venv/                     # Ambiente virtual
│
├── .gitattributes            # Configurações do Git
├── .gitignore                # Arquivos ignorados
├── .python-version           # Versão Python
├── LICENSE                   # Licença MIT
├── pyproject.toml            # Dependências
├── README.md                 # Documentação
└── uv.lock                   # Lock file do UV

## Instalação

1. Clone o repositório:
   git clone https://github.com/sidneymarcelofranco/erwin_py.git
   cd erwin_py

2. Configure o ambiente virtual:
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

3. Instale as dependências:
   pip install -r requirements.txt

## Utilização

Para sincronizar com UV:
uv sync

## Licença
MIT License - Consulte LICENSE para detalhes.

## Contato
Sidney Marcelo Franco
Email: sidneymarcelofranco@hotmail.com
GitHub: https://github.com/sidneymarcelofranco/erwin_py