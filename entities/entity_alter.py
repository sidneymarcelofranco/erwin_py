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

    sessao_M0 = ObjApi.Sessions.Add()
    sessao_M1 = ObjApi.Sessions.Add()

    intRetOper0 = sessao_M0.Open(ObjPU, 0)
    intRetOper1 = sessao_M1.Open(ObjPU, 1)

    return ObjApi, ObjPU, sessao_M0, sessao_M1


def alterar_definicao_entidade(sessao, entidade_nome, nova_definicao):
    root = sessao.ModelObjects.Root
    entidades = sessao.ModelObjects.Collect(root, "Entity", 1)

    for entidade in entidades:
        if entidade.Name == entidade_nome:
            transId = sessao.BeginNamedTransaction(f"Alterar definição da entidade {entidade_nome}")
            entidade.Properties["Definition"].Value = nova_definicao
            sessao.CommitTransaction(transId)
            print(f"Definição da entidade '{entidade_nome}' alterada para:\n{nova_definicao}")
            return True

    print(f"Entidade '{entidade_nome}' não encontrada.")
    return False


def listar_entidades(sessao):
    root = sessao.ModelObjects.Root
    entidades = sessao.ModelObjects.Collect(root, "Entity", 1)

    dados_logicos = []
    for idx, entidade in enumerate(entidades, start=1):
        definicao = entidade.Properties["Definition"].Value if "Definition" in entidade.Properties else ""
        linha = [
            idx,
            entidade.Name,
            entidade.Properties["Definition"].Value
        ]
        dados_logicos.append(linha)

    cabecalhos = ["Identity", "Entidade Nome", "Entidade Definição"]

    print("\n=== Entidades (Lógicas) ===")
    print(tabulate(dados_logicos, headers=cabecalhos, tablefmt="grid"))


def main():
    caminho_modelo = "C:\\temp\\eMovies.erwin"
    entidade_alvo = "CUSTOMER"
    nova_definicao = "From Python Customer."
    # Se quiser fazer rollback, altere para a definição antiga:
    # nova_definicao = "A CUSTOMER is a person or organization who has rented a movie within the past year."

    ObjApi, ObjPU, sessao_M0, sessao_M1 = inicializar_erwin(caminho_modelo)

    alterado = alterar_definicao_entidade(sessao_M0, entidade_alvo, nova_definicao)

    if alterado:
        ObjPU.Save(caminho_modelo, "RDO=NO; OVM=YES ; OVF=Yes; DGM=YES")
        print("Modelo salvo com sucesso.")

    listar_entidades(sessao_M0)


if __name__ == "__main__":
    main()
