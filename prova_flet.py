import flet as ft

def main(page: ft.Page):
    page.title = "Gerenciador de Tarefas"

    task = ft.TextField(
        label="Adicione uma tarefa: ")
    b = ft.ElevatedButton(
        text="Adicionar",
        on_click=lambda e: page.add(ft.Text(task.value))
    )


    page.add(task, b)

if __name__ == "__main__":
    ft.app(target=main)

