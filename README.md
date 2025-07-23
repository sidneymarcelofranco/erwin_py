# ERWIN_PY

Estrutura do projeto Python para integração com o erwin Data Modeler.

---

## 📁 Estrutura de Diretórios

```
erwin_py/
├── attributes/               # Operações com atributos
│   ├── attribute_alter.py       # Modificação de atributos
│   ├── attribute_created.py     # Criação de atributos
│   ├── attribute_deleted.py     # Exclusão de atributos (versão atual)
│   ├── attribute_deleted_Old.py # Versão legada
│   └── attribute_read.py        # Leitura de atributos
│
├── entities/                 # Operações com entidades
│   ├── entity_alter.py          # Modificação de entidades
│   ├── entity_created.py        # Criação de entidades
│   ├── entity_deleted.py        # Exclusão de entidades
│   └── entity_read.py           # Leitura de entidades
│
├── __pycache__/             # Cache do Python (ignorar)
├── venv/                    # Ambiente virtual Python
│
├── .gitattributes           # Configurações do Git
├── .gitignore               # Arquivos/pastas ignoradas pelo Git
├── .python-version          # Versão Python recomendada
├── LICENSE                  # Licença MIT
├── pyproject.toml           # Gerenciador de dependências (UV/Poetry)
├── README.md                # Este arquivo
└── uv.lock                  # Lock file do UV
```

---

## 🚀 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/sidneymarcelofranco/erwin_py.git
cd erwin_py
```

2. Configure o ambiente virtual:

```bash
# Linux/Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Uso com UV

Instale o UV no Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Sincronize as dependências com UV:

```bash
uv sync
```

---

## 📄 Licença

MIT License – consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📬 Contato

**Sidney Marcelo Franco**  
📧 Email: [sidneymarcelofranco@hotmail.com](mailto:sidneymarcelofranco@hotmail.com)  
🔗 GitHub: [sidneymarcelofranco/erwin_py](https://github.com/sidneymarcelofranco/erwin_py)