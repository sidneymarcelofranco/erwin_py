import win32com.client
from tabulate import tabulate


def inicializar_erwin(caminho_modelo):
    ObjApi = win32com.client.Dispatch("AllFusionERwin.SCAPI")
    objPropertyBag = win32com.client.Dispatch("AllFusionERwin.SCAPI.PropertyBag")
    objPropertyBag.Add("Model_Type", "Combined")

    ObjPU = ObjApi.PersistenceUnits.Create(objPropertyBag)
    ObjPU = ObjApi.PersistenceUnits.Add(caminho_modelo, "RDO=No")

    if ObjApi.Sessions.Count > 0:
        ObjApi.Sessions.Clear()

    sessao = ObjApi.Sessions.Add()
    sessao.Open(ObjPU, 0)

    return ObjApi, ObjPU, sessao


def alterar_definition_atributo(sessao, entidade_nome, atributo_nome, nova_definicao):
    root = sessao.ModelObjects.Root
    entidades = sessao.ModelObjects.Collect(root, "Entity", 1)

    for entidade in entidades:
        if entidade.Name == entidade_nome:
            atributos = sessao.ModelObjects.Collect(entidade, "Attribute", 1)

            for atributo in atributos:
                if atributo.Properties["Name"].Value == atributo_nome:
                    trans_id = sessao.BeginNamedTransaction(f"Alterar definição de {atributo_nome}")
                    atributo.Properties["Definition"].Value = nova_definicao
                    sessao.CommitTransaction(trans_id)

                    print(f"Definição do atributo '{atributo_nome}' alterada com sucesso.")
                    return True

    print(f"Atributo '{atributo_nome}' não encontrado na entidade '{entidade_nome}'.")
    return False


def listar_atributos(sessao, entidade_nome):
    root = sessao.ModelObjects.Root
    entidades = sessao.ModelObjects.Collect(root, "Entity", 1)

    dados = []
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
                dados.append(linha)

    cabecalhos = [
        "ID",
        "Entidade",
        "Nome Lógico",
        "Nome Físico",
        "Definição",
        "Comentário",
    ]
    print("\nAtributos da entidade:", entidade_nome)
    print(tabulate(dados, headers=cabecalhos, tablefmt="grid"))


def main():
    caminho_modelo = "C:\\temp\\eMovies.erwin"
    entidade_nome = "Entidade_Created"
    atributo_nome = "Novo_Atributo"
    nova_definicao = "Alterado via Python"

    ObjApi, ObjPU, sessao = inicializar_erwin(caminho_modelo)

    alterado = alterar_definition_atributo(sessao, entidade_nome, atributo_nome, nova_definicao)

    if alterado:
        ObjPU.Save(caminho_modelo, "RDO=NO; OVM=YES ; OVF=YES; DGM=YES")
        print("Modelo salvo com sucesso.")

    listar_atributos(sessao, entidade_nome)


if __name__ == "__main__":
    main()
