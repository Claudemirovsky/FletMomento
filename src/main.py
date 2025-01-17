import flet as ft
import random


class Horario(ft.Card):
    def __init__(self, color, name, start, end):
        super().__init__()
        self.margin = 0
        self.content = ft.Container(
            border_radius=10,
            bgcolor=color,
            padding=10,
            content=ft.Column(
                [
                    ft.Text(value=name, color="#F5FFF5",
                            size=10, weight=ft.FontWeight.BOLD),
                    ft.Text(f"{start}-{end}", color="#F5FFF5",
                            size=7, weight=ft.FontWeight.BOLD)
                ],
                width=45,
                height=60,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        )


def horarioAleatorio(dia):
    cores = ["#FBBC4D", "#42CA62", "#F54A4A"]
    cadeiras = ["Cálculo II", "Lógica Matemá.", "Libras", "Mat. Discreta",
                "Ética e Filosofia", "Pro. Orie. a Objetos", "Arq. de Compu.", "Banco de Dados"]
    dia = [ft.Text(value=dia, color="#F5FFF5",
                   size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)]
    for i in range(12, random.randrange(13, 18)):
        dia.append(Horario(color=random.choice(cores), name=random.choice(
            cadeiras), start=f"{i}:00", end=f"{i+1}:00"))
    return dia


def main(page: ft.Page):

    YELLOW = "#FEC562"
    BLUE = "#4A92FF"
    GREY = "#F5FFF5"
    DARK_BLUE = "#0B2E4F"

    login = ft.View(
        route="login",
        bgcolor=ft.Colors.TRANSPARENT,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        decoration=ft.BoxDecoration(
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[BLUE, "#2C5899"],
                stops=[0.0, 0.86]
            )
        ),
        controls=[
            ft.SafeArea(
                content=ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                # Titulo
                                ft.Column(
                                    [
                                        ft.Row(
                                            [
                                                ft.Text(
                                                    value="TIME", color=BLUE, weight=ft.FontWeight.BOLD, size=40),
                                                ft.Text(value="WISE", color=YELLOW,
                                                        weight=ft.FontWeight.BOLD, size=40)
                                            ],
                                            spacing=0,
                                            alignment=ft.MainAxisAlignment.CENTER
                                        ),
                                        ft.Text(
                                            "Organize, estude, conquiste!", weight=ft.FontWeight.BOLD, size=16, color=DARK_BLUE)
                                    ],
                                    spacing=0,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                ),

                                # Email
                                ft.Column(
                                    [
                                        ft.Text(value=" Email", color=DARK_BLUE,
                                                weight=ft.FontWeight.BOLD, size=16),
                                        ft.TextField(
                                            color=BLUE,
                                            hint_text="seuemail@email.com.br",
                                            width=330,
                                            border_color=BLUE,
                                            border_radius=10,
                                            hint_style=ft.TextStyle(color=BLUE))
                                    ],
                                    spacing=4
                                ),

                                # Senha
                                ft.Column(
                                    [
                                        ft.Text(value=" Senha", color=DARK_BLUE,
                                                weight=ft.FontWeight.BOLD, size=16,),
                                        ft.TextField(
                                            color=BLUE,
                                            hint_text="•••••••",
                                            width=330,
                                            border_color=BLUE,
                                            border_radius=10,
                                            hint_style=ft.TextStyle(
                                                color=BLUE),
                                            password=True)
                                    ],
                                    spacing=4
                                ),

                                # Lembre-se
                                ft.Row(
                                    [
                                        ft.Checkbox(
                                            label="Lembre-se de mim", label_style=ft.TextStyle(color=DARK_BLUE, size=12)),
                                        ft.TextButton(content=ft.Text(value="Esqueceu sua senha?", text_align=ft.TextAlign.RIGHT, style=ft.TextStyle(
                                            decoration=ft.TextDecoration.UNDERLINE, size=12), color=DARK_BLUE))
                                    ],
                                    width=330,
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),

                                # Entrar
                                ft.ElevatedButton(content=ft.Text(value="ENTRAR", color=ft.Colors.WHITE, size=16, weight=ft.FontWeight.BOLD),
                                                  bgcolor=YELLOW, width=330, height=48, on_click=lambda _: page.go("main")),

                                # Não tem conta ainda
                                ft.Row(
                                    [
                                        ft.Text(
                                            value="Não tem conta?", color=DARK_BLUE, weight=ft.FontWeight.BOLD, size=16),
                                        ft.TextButton(content=ft.Text(value="Crie agora", text_align=ft.TextAlign.RIGHT, style=ft.TextStyle(
                                            decoration=ft.TextDecoration.UNDERLINE, size=16), color=BLUE), on_click=lambda _: page.go("register"))
                                    ],
                                    spacing=0,
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),

                                ft.Divider(height=10, color=DARK_BLUE),

                                # Ou entre com
                                ft.Text(value="Ou entre com", color=DARK_BLUE,
                                        size=20, weight=ft.FontWeight.BOLD),

                                # Icones
                                ft.Row(
                                    [
                                        ft.Container(
                                            content=ft.Image(
                                                src=f"social.png", fit=ft.ImageFit.COVER),
                                            margin=10,
                                            padding=10,
                                            bgcolor=BLUE,
                                            width=80,
                                            height=80,
                                            border_radius=16
                                        ),
                                        ft.Container(
                                            content=ft.Image(
                                                src=f"instagram.png", fit=ft.ImageFit.COVER),
                                            margin=10,
                                            padding=10,
                                            bgcolor=BLUE,
                                            width=80,
                                            height=80,
                                            border_radius=16
                                        ),
                                        ft.Container(
                                            content=ft.Image(
                                                src=f"twitter.png", fit=ft.ImageFit.COVER),
                                            margin=10,
                                            padding=10,
                                            bgcolor=BLUE,
                                            width=80,
                                            height=80,
                                            border_radius=16
                                        )

                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                                )
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        alignment=ft.alignment.center,
                        padding=20
                    ),
                    width=400,
                    height=700,
                    color=GREY,
                )
            )
        ]
    )

    register = ft.View(
        route="register",
        bgcolor=ft.Colors.TRANSPARENT,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        decoration=ft.BoxDecoration(
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[BLUE, "#2C5899"],
                stops=[0.0, 0.86]
            )
        ),
        controls=[
            ft.SafeArea(
                content=ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                # Titulo
                                ft.Column(
                                    [
                                        ft.Row(
                                            [
                                                ft.Text(
                                                    value="TIME", color=BLUE, weight=ft.FontWeight.BOLD, size=40),
                                                ft.Text(value="WISE", color=YELLOW,
                                                        weight=ft.FontWeight.BOLD, size=40)
                                            ],
                                            spacing=0,
                                            alignment=ft.MainAxisAlignment.CENTER
                                        ),
                                        ft.Text(
                                            "Organize, estude, conquiste!", weight=ft.FontWeight.BOLD, size=16, color=DARK_BLUE)
                                    ],
                                    spacing=0,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                ),

                                # Nome
                                ft.Column(
                                    [
                                        ft.Text(value=" Nome", color=DARK_BLUE,
                                                weight=ft.FontWeight.BOLD, size=16),
                                        ft.TextField(
                                            color=BLUE,
                                            hint_text="Nome de usuário",
                                            width=330,
                                            border_color=BLUE,
                                            border_radius=10,
                                            hint_style=ft.TextStyle(color=BLUE))
                                    ],
                                    spacing=4
                                ),

                                # Email
                                ft.Column(
                                    [
                                        ft.Text(value=" Email", color=DARK_BLUE,
                                                weight=ft.FontWeight.BOLD, size=16),
                                        ft.TextField(
                                            color=BLUE,
                                            hint_text="seuemail@email.com.br",
                                            width=330,
                                            border_color=BLUE,
                                            border_radius=10,
                                            hint_style=ft.TextStyle(color=BLUE))
                                    ],
                                    spacing=4
                                ),

                                # Senha
                                ft.Column(
                                    [
                                        ft.Text(value=" Senha", color=DARK_BLUE,
                                                weight=ft.FontWeight.BOLD, size=16,),
                                        ft.TextField(
                                            color=BLUE,
                                            hint_text="•••••••",
                                            width=330,
                                            border_color=BLUE,
                                            border_radius=10,
                                            hint_style=ft.TextStyle(
                                                color=BLUE),
                                            password=True)
                                    ],
                                    spacing=4
                                ),

                                # Entrar
                                ft.ElevatedButton(content=ft.Text(value="CONFIRMAR", color=ft.Colors.WHITE, size=16, weight=ft.FontWeight.BOLD),
                                                  bgcolor=YELLOW, width=330, height=48, on_click=lambda _: page.go("main")),

                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        alignment=ft.alignment.center,
                        padding=20
                    ),
                    width=400,
                    height=700,
                    color=GREY,
                )
            )
        ]
    )

    main = ft.View(
        route="main",
        bgcolor=ft.Colors.TRANSPARENT,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        decoration=ft.BoxDecoration(
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[BLUE, "#2C5899"]
            )
        ),
        floating_action_button = ft.FloatingActionButton(icon=ft.Icons.ADD, shape=ft.CircleBorder(), bgcolor=YELLOW, foreground_color=GREY),
        floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED,
        controls=[
            ft.AppBar(
                bgcolor=GREY,
                leading=ft.Container(
                    content=ft.Row(
                        [
                            ft.Row(
                                [
                                    ft.Text(value="TIME", color=BLUE,
                                            weight=ft.FontWeight.BOLD, size=30),
                                    ft.Text(value="WISE", color=YELLOW,
                                            weight=ft.FontWeight.BOLD, size=30)
                                ],
                                spacing=0,
                                alignment=ft.MainAxisAlignment.CENTER

                            ),
                            ft.Text(value="Bem vindo, usuário!", color=DARK_BLUE,
                                    size=20, weight=ft.FontWeight.BOLD)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    padding=ft.padding.symmetric(horizontal=8)
                )
            ),

            ft.Container(
                content=ft.Text("Semana: 13/01-17/01", color=DARK_BLUE,
                                size=30, weight=ft.FontWeight.BOLD),
                padding=ft.padding.symmetric(horizontal=30, vertical=10),
                border_radius=16,
                bgcolor=GREY
            ),

            ft.Row(
                [
                    ft.Column(horarioAleatorio("SEG"),
                              alignment=ft.MainAxisAlignment.CENTER),
                    ft.Column(horarioAleatorio("TER"),
                              alignment=ft.MainAxisAlignment.CENTER),
                    ft.Column(horarioAleatorio("QUA"),
                              alignment=ft.MainAxisAlignment.CENTER),
                    ft.Column(horarioAleatorio("QUI"),
                              alignment=ft.MainAxisAlignment.CENTER),
                    ft.Column(horarioAleatorio("SEX"),
                              alignment=ft.MainAxisAlignment.CENTER)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.START
            ),
            ft.BottomAppBar(
                bgcolor=GREY,
                shape=ft.NotchShape.CIRCULAR,
                content=ft.Row(
                    [
                        ft.IconButton(icon=ft.Icons.PERSON, icon_color=DARK_BLUE, icon_size=60),
                        ft.Container(expand=True),
                        ft.IconButton(icon=ft.Icons.SETTINGS, icon_color=DARK_BLUE, icon_size=60),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                ),
                padding=ft.padding.symmetric(horizontal=50)
            ),
        ]
    )

    def route_change(route):
        page.views.clear()
        page.views.append(login)
        if page.route == "main":
            page.views.append(main)
        if page.route == "register":
            page.views.append(register)
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(main, assets_dir="assets")
