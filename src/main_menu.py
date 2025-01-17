import flet as ft

from utils import CustomColors, Title
import random


class Horario(ft.Card):
    def __init__(self, color: str, name: str, start: str, end: str):
        super().__init__()
        self.margin = 0
        self.content = ft.Container(
            border_radius=10,
            bgcolor=color,
            padding=10,
            content=ft.Column(
                [
                    ft.Text(value=name, color="#F5FFF5", size=10, weight=ft.FontWeight.BOLD),
                    ft.Text(f"{start}-{end}", color="#F5FFF5", size=7, weight=ft.FontWeight.BOLD),
                ],
                width=45,
                height=60,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
        )


class MainMenu(ft.View):
    def __init__(self):
        super().__init__()
        self.route = "main"
        self.bgcolor = ft.Colors.TRANSPARENT
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.decoration = ft.BoxDecoration(
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_right,
                end=ft.alignment.bottom_left,
                colors=[CustomColors.DARK_BLUE, "#2C5899"],
            )
        )
        btn = ft.IconButton(
            icon=ft.Icons.ADD_CIRCLE_OUTLINE,
            icon_color=CustomColors.GREY,
            bgcolor=ft.Colors.TRANSPARENT,
            icon_size=60,
        )
        self.appbar = self.main_appbar
        self.bottom_appbar = self.main_bottombar
        self.floating_action_button = ft.FloatingActionButton(
            content=btn,
            shape=ft.CircleBorder(),
            bgcolor=CustomColors.YELLOW,
        )
        self.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
        self.controls = [
            ft.Row(
                [
                    ft.Column(self.horarioAleatorio(x), alignment=ft.MainAxisAlignment.CENTER)
                    for x in ["Seg", "Ter", "Qua", "Qui", "Sex"]
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
        ]

    @property
    def main_appbar(self):
        txt_style = ft.TextStyle(weight=ft.FontWeight.W_800, color=CustomColors.DARK_BLUE)
        return ft.AppBar(
            bgcolor=CustomColors.GREY,
            shape=ft.RoundedRectangleBorder(
                radius=ft.BorderRadius(top_left=0, top_right=0, bottom_left=15, bottom_right=15)
            ),
            title=ft.Container(
                content=ft.Column(
                    [
                        Title(30),
                        ft.Text(value="Bem vindo, usuário!", style=txt_style, size=17),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=0,
                ),
            ),
            actions=[
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Semana:", style=txt_style, size=20),
                            ft.Text(
                                "16/12 - 20/12",
                                style=txt_style,
                                size=20,
                                text_align=ft.TextAlign.START,
                            ),
                        ],
                        spacing=0,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    padding=10,
                )
            ],
            toolbar_height=100,
        )

    @property
    def main_bottombar(self) -> ft.BottomAppBar:
        container = ft.Container(
            bgcolor=CustomColors.GREY,
            border_radius=ft.BorderRadius(top_left=15, top_right=15, bottom_left=0, bottom_right=0),
            content=ft.Row(
                [
                    ft.IconButton(
                        icon=ft.Icons.PERSON_OUTLINE,
                        icon_color="grey",
                        icon_size=60,
                    ),
                    ft.Container(bgcolor=ft.Colors.TRANSPARENT),
                    ft.IconButton(
                        icon=ft.Icons.SETTINGS_OUTLINED,
                        icon_color="grey",
                        icon_size=60,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            ),
        )
        # return ft.BottomAppBar(bgcolor=ft.Colors.TRANSPARENT, content=container, padding=0)
        return ft.BottomAppBar(
            bgcolor=ft.Colors.TRANSPARENT,
            content=container,
            padding=0,
        )

    def horarioAleatorio(self, dia: str) -> list[ft.Control]:
        cores = ["#FBBC4D", "#42CA62", "#F54A4A"]
        cadeiras = [
            "Cálculo II",
            "Lógica Matemá.",
            "Libras",
            "Mat. Discreta",
            "Ética e Filosofia",
            "Pro. Orie. a Objetos",
            "Arq. de Compu.",
            "Banco de Dados",
        ]
        dias: list[ft.Control] = [
            ft.Text(
                value=dia,
                color=CustomColors.GREY,
                size=30,
                weight=ft.FontWeight.W_800,
                text_align=ft.TextAlign.CENTER,
            )
        ]
        for i in range(12, random.randrange(13, 18)):
            dias.append(
                Horario(
                    color=random.choice(cores),
                    name=random.choice(cadeiras),
                    start=f"{i}:00",
                    end=f"{i + 1}:00",
                )
            )
        return dias
