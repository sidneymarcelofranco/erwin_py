import win32com.client
from tabulate import tabulate


def inicializar_erwin(caminho_modelo):
    ObjApi = win32com.client.Dispatch('AllFusionERwin.SCAPI')
    objPropertyBag = win32com.client.Dispatch('AllFusionERwin.SCAPI.PropertyBag')
    objPropertyBag.Add("Model_Type", "Combined")

    ObjPU = ObjApi.PersistenceUnits.Create(objPropertyBag)
    ObjPU = ObjApi.PersistenceUnits.Add(caminho_modelo, "RDO=No")

    if ObjApi.Sessions.Count > 0:
        ObjApi.Sessions.Clear()

    sessao = ObjApi.Sessions.Add()
    sessao.Open(ObjPU, 0)

    return ObjApi, ObjPU, sessao


def criar_atributo(sessao, entidade_nome, nome_logico, nome_fisico, definicao, tipo_dado):
    root = sessao.ModelObjects.Root
    entidades = sessao.ModelObjects.Collect(root, "Entity", 1)

    for entidade in entidades:
        if entidade.Name == entidade_nome:
            print(f"Entidade encontrada: {entidade.Name}")

            atributos = sessao.ModelObjects.Collect(entidade, "Attribute", 1)
            for atributo in atributos:
                if atributo.Properties["Name"].Value == nome_logico:
                    print(f"Atributo '{nome_logico}' já existe. Cancelando criação.")
                    return False

            trans_id = sessao.BeginNamedTransaction(f"Adicionar atributo {nome_logico}")
            novo_atributo = sessao.ModelObjects.Collect(entidade, "Attribute", 1).Add("Attribute")
            novo_atributo.Properties["Name"].Value = nome_logico
            novo_atributo.Properties["Physical_Name"].Value = nome_fisico
            novo_atributo.Properties["Definition"].Value = definicao
            novo_atributo.Properties["Physical_Data_Type"].Value = tipo_dado
            sessao.CommitTransaction(trans_id)

            print(f"Atributo '{nome_logico}' criado com sucesso.")
            return True

    print(f"Entidade '{entidade_nome}' não encontrada.")
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
    nome_logico = "Novo_Atributo"
    nome_fisico = "novo_atributo"
    definicao = "Criado via Python"
    tipo_dado = "INTEGER"

    ObjApi, ObjPU, sessao = inicializar_erwin(caminho_modelo)

    sucesso = criar_atributo(sessao, entidade_nome, nome_logico, nome_fisico, definicao, tipo_dado)

    if sucesso:
        ObjPU.Save(caminho_modelo, "RDO=NO; OVM=YES ; OVF=YES; DGM=YES")
        print("Modelo salvo com sucesso.")

    listar_atributos(sessao, entidade_nome)


if __name__ == "__main__":
    main()
