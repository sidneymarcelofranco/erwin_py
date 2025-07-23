import win32com.client


def inicializar_erwin(caminho_modelo):
    ObjApi = win32com.client.Dispatch('AllFusionERwin.SCAPI')
    objPropertyBag = win32com.client.Dispatch('AllFusionERwin.SCAPI.PropertyBag')
    objPropertyBag.Add("Model_Type", "Combined")

    ObjPU = ObjApi.PersistenceUnits.Create(objPropertyBag)
    ObjPU = ObjApi.PersistenceUnits.Add(caminho_modelo, "RDO=No")

    if ObjApi.Sessions.Count > 0:
        ObjApi.Sessions.Clear()

    sessao_M0 = ObjApi.Sessions.Add()
    sessao_M1 = ObjApi.Sessions.Add()

    sessao_M0.Open(ObjPU, 0)
    sessao_M1.Open(ObjPU, 1)

    return ObjApi, ObjPU, sessao_M0, sessao_M1


def criar_entidade(sessao, nome_entidade, comentario="", definicao=""):
    root = sessao.ModelObjects.Root
    trans_id = sessao.BeginNamedTransaction("Create Entity")
    nova_entidade = sessao.ModelObjects.Collect(root).Add("Entity")
    nova_entidade.Properties["Name"].Value = nome_entidade
    nova_entidade.Properties["Comment"].Value = comentario
    nova_entidade.Properties["Definition"].Value = definicao
    sessao.CommitTransaction(trans_id)
    print(f"Entidade '{nome_entidade}' criada com sucesso.")


def salvar_modelo(ObjPU, caminho_modelo):
    ObjPU.Save(caminho_modelo, "RDO=NO; OVM=YES ; OVF=Yes; DGM=YES")
    print("Modelo salvo com sucesso.")


def main():
    caminho_modelo = "C:\\temp\\eMovies.erwin"
    nome_entidade = "Entidade_Created"
    comentario = "from Python"
    definicao = "from Python"

    ObjApi, ObjPU, sessao_M0, sessao_M1 = inicializar_erwin(caminho_modelo)

    criar_entidade(sessao_M0, nome_entidade, comentario, definicao)

    salvar_modelo(ObjPU, caminho_modelo)


if __name__ == "__main__":
    main()
