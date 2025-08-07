import json


agenda = []

def salvar_agenda():
    with open("agenda.json", "w") as f:
        json.dump(agenda, f, indent=4)

def carregar_agenda():
    global agenda
    try:
        with open("agenda.json", "r") as f:
            agenda = json.load(f)  
    except FileNotFoundError:
        agenda = []  


def adicionar_contato():

    print("=== Adicionar Contato ===")

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Digite seu email: ")

    contato = {"nome": nome, "telefone": telefone, "email": email}
    agenda.append(contato)
    salvar_agenda()

def listar_contatos():
    print("=== Lista de Contatos ===")

    if not agenda:
        print("Agenda vazia.")
        return

    for i, contato in enumerate(agenda):
        print(f"\nContato {i + 1}:")
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"E-mail: {contato['email']}")


def buscar_contato():
    print("=== Buscar Contato ===")

    nome_busca = input("Digite o nome: ")
    encontrado = False

    for contato in agenda:
        if contato['nome'].lower() == nome_busca.lower():
            print(f"Nome: {contato['nome']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"E-mail: {contato['email']}")
            encontrado = True
            break

    if not encontrado:
        print("Esse usuário não foi cadastrado.")
        

def editar_contato():
    print("=== Editar Contato ===")
     
    nome_contato = input("Digite o nome do ctt: ")
    encontrado = False
    
    for contato in agenda:
        if contato['nome'].lower() == nome_contato.lower():
            print("Digite os novos dados.")
            novo_nome = input(f"Novo nome: ({contato['nome']}): ")
            novo_telefone = input(f"Novo telefone ({contato['telefone']}): ")
            novo_email = input(f"Novo E-mail: ({contato['email']}): ")

            if novo_nome:
                contato['nome'] = novo_nome
            if novo_telefone:
                contato['telefone'] = novo_telefone
            if novo_email:
                contato['email'] = novo_email
            salvar_agenda()
            print("Contato atualizado com sucesso!")
            encontrado = True
            break
    if not encontrado:
        print("Esse ctt não está cadastrado.")


def remover_contato():
    print("=== Remover Contato ===")

    nome_remover = input("Digite o nome que quer remover: ")
    encontrado = False

    for contato in agenda:
        if contato['nome'].lower() == nome_remover.lower():
            remover = input("Voçe deseja remover esse nome dos contatos? [s] ou [n]: ")
            if remover.lower() == 's':
                agenda.remove(contato)
                salvar_agenda()
                print("Seu ctt foi removido.")

            else:
                print("Seu ctt não foi removido.")
            encontrado = True
            break
    
    if not encontrado:
        print("Esse nome não foi cadastrado.")



def menu():

    carregar_agenda()

    while True:
        print("\n==== AGENDA DE CONTATOS ====")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Editar contato")
        print("5. Remover contato")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            buscar_contato()
        elif opcao == '4':
            editar_contato()
        elif opcao == '5':
            remover_contato()
        elif opcao == '6':
            print('Saindo da agenda...')
            break
        else:
            print("Opção invalida.")



import FreeSimpleGUI as sg

def interface_agenda():
    carregar_agenda()

    layout = [
        [sg.Text("Nome"), sg.Input(key="nome")],
        [sg.Text("Telefone"), sg.Input(key="telefone")],
        [sg.Text("Email"), sg.Input(key="email")],
        [sg.Text("Nome para remover"), sg.Input(key="remover_nome")],
        [sg.Button("Adicionar"), sg.Button("Listar"), sg.Button("Sair"), sg.Button("Remover")],
        [sg.Multiline("", size=(50, 10), key="output", disabled=True)]
    ]

    window = sg.Window("Agenda de Contatos", layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Sair":
            break

        if event == "Adicionar":
            nome = values["nome"]
            telefone = values["telefone"]
            email = values["email"]

            if nome and telefone and email:
                contato = {"nome": nome, "telefone": telefone, "email": email}
                agenda.append(contato)
                salvar_agenda()
                window["output"].update("Contato adicionado com sucesso!\n", append=True)
            else:
                window["output"].update("Preencha todos os campos!\n", append=True)

        elif event == "Listar":
            if not agenda:
                window["output"].update("Agenda vazia.\n")
            else:
                texto = ""
                for i, contato in enumerate(agenda):
                    texto += f"\nContato {i+1}:\nNome: {contato['nome']}\nTelefone: {contato['telefone']}\nE-mail: {contato['email']}\n"
                window["output"].update(texto)
        
        elif event == "Remover":
            nome_remover = values["remover_nome"]
           
            if nome_remover:  
                encontrado = False
                for contato in agenda:
                    if contato['nome'].lower() == nome_remover.lower():
                        agenda.remove(contato)
                        salvar_agenda()
                        window['output'].update("Seu contato foi removido com sucesso!\n", append=True)
                        encontrado = True
                        break
                if not encontrado:
                    window['output'].update("Contato não encontrado.\n", append=True)
            else:
                window["output"].update("Digite um nome para remover.\n", append=True)

    window.close()
    
def escolher_modo():
    print("=== Bem-vindo à Agenda de Contatos ===")
    print("Escolha o modo de uso:")
    print("[1] Terminal")
    print("[2] Interface Gráfica")

    modo = input("Digite sua escolha (1 ou 2): ")

    if modo == "1":
        menu()
    elif modo == "2":
        interface_agenda()
    else:
        print("Opção inválida. Encerrando o programa.")

if __name__ == "__main__":
    escolher_modo()


