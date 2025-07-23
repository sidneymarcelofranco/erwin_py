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

entities = sessao_M0.ModelObjects.Collect(root, "Entity", 1)
# atribute = sessao_M0.ModelObjects.Collect(entities, "Atribute", 1)

# Coleta os dados dos atributos da entidade CUSTOMER
for e in entities:
    if e.Name == 'Entidade_Created':
        atributos = sessao_M0.ModelObjects.Collect(e, "Attribute", 1)
        for a in atributos:  
            Object_Id = a.Properties["Long_Id"].Value 
            trans_id = sessao_M0.BeginNamedTransaction("Deleted Atribute")
            oEntity = sessao_M0.ModelObjects.Collect(root).Remove(Object_Id)
            sessao_M0.CommitTransaction(trans_id)
            ObjPU.Save(conexao_arquivo, "RDO=NO; OVM=YES ; OVF=Yes; DGM=YES")   
            print("Atributo deletado com sucesso.") 
            
            
            

