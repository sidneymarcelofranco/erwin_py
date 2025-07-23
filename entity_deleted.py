
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
sessao_M1 = ObjApi.Sessions.Add()
intRetOper =  sessao_M0.Open(ObjPU,0 )
intRetOper =  sessao_M1.Open(ObjPU,1 )

# Coleto os dados do modelo   
root = sessao_M0.ModelObjects.Root
# modelObjects = sessao_M0.ModelObjects
# Coleta os dados das entidades
# as entidades são objetos do modelo
entities = sessao_M0.ModelObjects.Collect(root, "Entity", 1)


for e in entities:
    if e.Name== "Entidade_Created":
        Object_Id = e.Properties["Long_Id"].Value
        # e.Properties["Long_Id"].Value,
        
# Deleted Entity
trans_id_deleted_entity = sessao_M0.BeginNamedTransaction("Deleted Entity")
oEntity = sessao_M0.ModelObjects.Collect(root).Remove(Object_Id)
sessao_M0.CommitTransaction(trans_id_deleted_entity)
ObjPU.Save(conexao_arquivo, "RDO=NO; OVM=YES ; OVF=Yes; DGM=YES")  
