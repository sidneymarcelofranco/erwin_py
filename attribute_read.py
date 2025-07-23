import win32com.client
from tabulate import tabulate


def inicializar_erwin(caminho_modelo):
    ObjApi = win32com.client.Dispatch('AllFusionERwin.SCAPI')
    objPropertyBag = win32com.client.Dispatch('AllFusionERwin.SCAPI.PropertyBag')
    objPropertyBag.Add("Model_Type", "Combined")

    ObjPU = ObjApi.PersistenceUnits.Create(objPropertyBag)
    ObjPU = ObjApi.PersistenceUnits.Add(caminho_modelo, "RDO=Yes")

    if ObjApi.Sessions.Count > 0:
        ObjApi.Sessions.Clear()

    sessao = ObjApi.Sessions.Add()
    sessao.Open(ObjPU, 0)

    return ObjApi, ObjPU, sessao


def listar_atributos(sessao, entidade_nome):
    root = sessao.ModelObjects.Root
    entidades = sessao.ModelObjects.Collect(root, "Entity", 1)

    dados_atributos = []
    for entidade in entidades:
        if entidade.Name == entidade_nome:
            atributos = sessao.ModelObjects.Collect(entidade, "Attribute", 1)
            for idx, atributo in enumerate(atributos, start=1):
                linha = [
                    idx,
                    entidade.Name,
                    atributo.Properties["Name"].Value,
                    atributo.Properties["Physical_Name"].Value,
                    atributo.Properties["Definition"].Value,
                    atributo.Properties["Comment"].Value if "Comment" in atributo.Properties else "",
                ]
                dados_atributos.append(linha)

    cabecalhos = [
        "Cod_Icr",
        "Ent_Name",
        "Atr_Name_Logico",
        "Atr_Name_Fisico",
        "Atr_Definition",
        "Atr_Comment",
        "A", "B", "C", "D", "E", "F", "G"
    ]

    print(tabulate(dados_atributos, headers=cabecalhos, tablefmt="grid"))


def main():
    caminho_modelo = "C:\\temp\\eMovies.erwin"
    entidade_nome = "Entidade_Created"

    ObjApi, ObjPU, sessao = inicializar_erwin(caminho_modelo)
    listar_atributos(sessao, entidade_nome)


if __name__ == "__main__":
    main()
