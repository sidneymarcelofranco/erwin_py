# ERWIN_PY

Estrutura do projeto Python para integração com erwin Data Modeler.

## 📁 Estrutura de Diretórios
erwin_py/
│
├── attributes/ # Operações com atributos
│ ├── attribute_alter.py # Modificação de atributos
│ ├── attribute_created.py # Criação de atributos
│ ├── attribute_deleted.py # Exclusão de atributos (nova versão)
│ ├── attribute_deleted_Old.py # Exclusão de atributos (versão antiga)
│ └── attribute_read.py # Consulta de atributos
│
├── entities/ # Operações com entidades
│ ├── entity_alter.py # Modificação de entidades
│ ├── entity_created.py # Criação de entidades
│ ├── entity_deleted.py # Exclusão de entidades
│ └── entity_read.py # Consulta de entidades
│
├── pycache/ # Cache Python (ignorar)
├── venv/ # Ambiente virtual (ignorar)
│
├── .gitattributes # Configurações do Git
├── .gitignore # Arquivos ignorados pelo Git
├── .python-version # Versão do Python utilizada
├── LICENSE # Licença do projeto
├── pyproject.toml # Configurações do projeto Python
├── README.md # Documentação principal
└── uv.lock # Lock file do UltraViolet (UV)



---

## 📝 Notas

- **Arquivos ignorados no versionamento**:
  - `__pycache__/`: Diretório gerado pelo Python
  - `venv/`: Ambiente virtual

- **Organização modular**:
  - Operações CRUD separadas
  - Divisão clara entre `entidades` e `atributos`

- **Configurações de projeto**:
  - `pyproject.toml`: Gerência moderna de dependências
  - `uv.lock`: Reprodutibilidade com UV

- **Histórico e versionamento**:
  - Presença de `attribute_deleted_Old.py` indica refatoração
  - `.gitattributes` e `.gitignore` garantem controle adequado

---

## 🚀 Instalação

```bash
# Clone o repositório
git clone https://github.com/sidneymarcelofranco/erwin_py.git

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Sincronize com UV
uv sync

📄 Licença
Este projeto está sob a licença MIT — veja o arquivo LICENSE para mais detalhes.

📬 Contato

Sidney Marcelo Franco📧 sidneymarcelofranco@hotmail.com🔗 Repositório no GitHub

Link do Projeto: https://github.com/sidneymarcelofranco/erwin_py
