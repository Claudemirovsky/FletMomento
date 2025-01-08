import flet as ft
import time

class Criar(ft.Button):
    def __init__(self, on_click):
        super().__init__()
        self.text="Criar horário"
        self.on_click=on_click

class Horario(ft.Column):
    def __init__(self, cancel, confirm):
        super().__init__()
        self.controls = [
            ft.Text(value="Adicionar horário", color=ft.Colors.BLACK, size=20),
            ft.Row([
                ft.Text(value="Nome: ", width=60, color=ft.Colors.BLACK),
                ft.TextField()
            ]),
            ft.Row([
                ft.Text(value="Horário:", width=60, color=ft.Colors.BLACK),
                ft.Dropdown(
                    options=[ft.dropdown.Option(x) for x in range(1,13)],
                    width=50,
                    color=ft.Colors.BLACK),
                ft.Text(value = ":", color=ft.Colors.BLACK),
                ft.Dropdown(
                    options=[ft.dropdown.Option(x) for x in range(60)],
                    width=50,
                    color=ft.colors.BLACK)
            ]),
            ft.Row([
                ft.Button(text="Cancelar", on_click=cancel),
                ft.Button(text="Confirmar")
            ])
        ]


def main(page: ft.Page):

    def scheduleCreate(horario: "Horario"):
        page.remove_at(-1)
        page.add(ft.Container(
            content=Horario(cancel, confirm),
            bgcolor=ft.Colors.WHITE,
            alignment=ft.alignment.center,
            margin=10,
            padding=20,
            width=450,
            height=250,
            border_radius=16)
        )
    
    def cancel(criar: "Criar"):
        page.remove_at(-1)
        page.add(Criar(on_click=scheduleCreate))

    def confirm(e):
        pass

    page.add(Criar(on_click=scheduleCreate))

ft.app(main)