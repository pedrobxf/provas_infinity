import flet as ft

mensagens = []

def main(page: ft.Page):
    page.title = "Agenda de contatos"

    def enviar(e):
        dict_contato = {
            "nome": nome.value,
            "email": email.value,
            "mensagem": mensagem.value
        }
        mensagens.append(dict_contato)
        page.add(sucesso)
        nome.value = ""
        email.value = ""
        mensagem.value = ""
        print(mensagens)
        page.update()
    
    nome = ft.TextField(label="Nome")
    email = ft.TextField(label="Email")
    mensagem = ft.TextField(label="Mensagem")
    botao =  ft.ElevatedButton(on_click= enviar, text="Enviar")
    sucesso = ft.Text("Mensagem enviada com sucesso!")


    page.add(nome, email, mensagem, botao)

if __name__ == "__main__":
    ft.app(target=main)

