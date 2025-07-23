import win32com.client
from tabulate import tabulate
ObjApi = win32com.client.Dispatch('AllFusionERwin.SCAPI')
objPropertyBag = win32com.client.Dispatch('AllFusionERwin.SCAPI.PropertyBag')
objPropertyBag.Add("Model_Type", "Combined")
conexao_arquivo = "C:\\temp\\eMovies.erwin"
ObjPU = ObjApi.PersistenceUnits.Create(objPropertyBag)
ObjPU = ObjApi.PersistenceUnits.Add(conexao_arquivo, "RDO=No")

# Verifica se a sessão já existe e limpa
if ObjApi.Sessions.Count > 0:
    ObjApi.Sessions.Clear()

# Cria duas sessões para o mesmo arquivo
sessao_M0 = ObjApi.Sessions.Add()
# sessao_M1 = ObjApi.Sessions.Add()
intRetOper =  sessao_M0.Open(ObjPU,0 )
# intRetOper =  sessao_M1.Open(ObjPU,1 )

# Coleto os dados do modelo   
root = sessao_M0.ModelObjects.Root


 
# Codigo funcionando

# Coleta os dados das entidades
# as entidades são objetos do modelo
# e podem ser coletadas usando o método Collect
entities = sessao_M0.ModelObjects.Collect(root, "Entity", 1)


# Imprime a quantidade de entidades encontradas
print("Quantidade de Entidades Encontradas: " + str(entities.count))

# =======================
# TABELA 1 - DADOS LÓGICOS
# =======================
dados_logicos = []

for idx, e in enumerate(entities, start=1):
    linha = [
        idx,
        # e.Name,
        e.Properties["Name"].Value,
        e.Properties["Definition"].Value,
        # e.Properties["Long_Id"].Value,
    ]
    dados_logicos.append(linha)

cab1 = ["Cod", "ent_nome", "ent_def"]
print("\n=== Entidades (Lógicas) ===")
print(tabulate(dados_logicos, headers=cab1, tablefmt="grid"))



# =======================
# TABELA 2 - DADOS FÍSICOS
# =======================
dados_fisicos = []

for idx, e in enumerate(entities, start=1):
    linha = [
        idx,
        e.Properties["Physical_Name"].Value,
        e.Properties["Comment"].Value
    ]
    dados_fisicos.append(linha)

cab2 = ["Cod", "tab_nome", "tab_def","long_id"]
print("\n=== Entidades (Físicas) ===")
print(tabulate(dados_fisicos, headers=cab2, tablefmt="grid"))

              
              