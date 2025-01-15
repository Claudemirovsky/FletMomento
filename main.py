import flet as ft

class Horario(ft.Container):
    def __init__(self, color, name, start, end):
        super().__init__()
        self.width=60,
        self.height=60,
        self.border_radius=20
        self.bgcolor=color
        self.content=ft.Row(
            [
                ft.Text(value=name, color="#F5FFF5", size=12, weight=ft.FontWeight.BOLD),
                ft.Text(f"{start}-{end}")
            ]
        )

def main(page: ft.Page):

    YELLOW="#FEC562"
    BLUE="#4A92FF"
    GREY="#F5FFF5"
    DARK_BLUE="#0B2E4F"

    login = ft.View(
        route="login",
        bgcolor=ft.Colors.TRANSPARENT,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        decoration=ft.BoxDecoration(
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[BLUE, DARK_BLUE]
            )
        ),
        controls=[
            ft.SafeArea(
                content=ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                #Titulo
                                ft.Column(
                                    [
                                        ft.Row(
                                            [
                                                ft.Text(value="TIME", color=BLUE, weight=ft.FontWeight.BOLD, size=40),
                                                ft.Text(value= "WISE", color=YELLOW,
                                                weight=ft.FontWeight.BOLD, size=40)
                                            ],
                                            spacing=0,
                                            alignment=ft.MainAxisAlignment.CENTER
                                        ),
                                        ft.Text("Organize, estude, conquiste!", weight=ft.FontWeight.BOLD, size=16, color=DARK_BLUE)
                                    ],
                                    spacing=0,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                ),

                                #Email
                                ft.Column(
                                    [
                                        ft.Text(value=" Email", color=DARK_BLUE, weight=ft.FontWeight.BOLD, size=16),
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

                                #Senha
                                ft.Column(
                                    [
                                        ft.Text(value=" Senha", color=DARK_BLUE, weight=ft.FontWeight.BOLD, size=16,),
                                        ft.TextField(
                                            color=BLUE,
                                            hint_text="•••••••", 
                                            width=330, 
                                            border_color=BLUE, 
                                            border_radius=10, 
                                            hint_style=ft.TextStyle(color=BLUE),
                                            password=True)
                                    ],
                                    spacing=4
                                ),

                                #Lembre-se
                                ft.Row(
                                    [
                                        ft.Checkbox(label="Lembre-se de mim", label_style=ft.TextStyle(color=DARK_BLUE, size=12)),
                                        ft.TextButton(content=ft.Text(value="Esqueceu sua senha?", text_align=ft.TextAlign.RIGHT, style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, size=12), color=DARK_BLUE))
                                    ],
                                    width=330,
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),

                                #Entrar
                                ft.ElevatedButton(content=ft.Text(value="ENTRAR", color=ft.Colors.WHITE, size=16, weight=ft.FontWeight.BOLD), bgcolor=YELLOW, width=330, height=48, on_click=lambda _: page.go("main")),

                                #Não tem conta ainda
                                ft.Row(
                                    [
                                        ft.Text(value="Não tem conta?", color=DARK_BLUE, weight=ft.FontWeight.BOLD, size=16),
                                        ft.TextButton(content=ft.Text(value="Crie agora", text_align=ft.TextAlign.RIGHT, style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, size=16), color=BLUE))
                                    ],
                                    spacing=0,
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),

                                ft.Divider(height=10, color=DARK_BLUE),

                                #Ou entre com
                                ft.Text(value="Ou entre com", color=DARK_BLUE, size=20, weight=ft.FontWeight.BOLD),

                                #Icones
                                ft.Row(
                                    [
                                        ft.Container(
                                            content=ft.Text("Facebook"),
                                            margin=10,
                                            padding=10,
                                            bgcolor=BLUE,
                                            width=80,
                                            height=80,
                                            border_radius=16
                                        ),
                                        ft.Container(
                                            content=ft.Text("Instagram"),
                                            margin=10,
                                            padding=10,
                                            bgcolor=BLUE,
                                            width=80,
                                            height=80,
                                            border_radius=16
                                        ),
                                        ft.Container(
                                            content=ft.Text("Twitter"),
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

    main = ft.View(
        route="main",
        bgcolor=ft.Colors.TRANSPARENT,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        decoration=ft.BoxDecoration(
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[BLUE, DARK_BLUE]
            )
        ),
        controls=[
            ft.AppBar(
                bgcolor=GREY,
                leading=ft.Container(
                    content=ft.Row(
                        [
                            ft.Row(
                                    [
                                        ft.Text(value="TIME", color=BLUE, weight=ft.FontWeight.BOLD, size=30),
                                        ft.Text(value= "WISE", color=YELLOW, weight=ft.FontWeight.BOLD, size=30)
                                    ],
                                    spacing=0,
                                    alignment=ft.MainAxisAlignment.CENTER
                    
                            ),
                            ft.Text(value="Bem vindo, usuário!", color=DARK_BLUE, size=20, weight=ft.FontWeight.BOLD)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    padding=ft.padding.symmetric(horizontal=8)
                )
            )
        ]
    )

    def route_change(route):
        page.views.clear()
        page.views.append(login)
        if page.route=="main":
            page.views.append(main)
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view=page.views[-1]
        page.go(top_view.route)

    page.on_route_change=route_change
    page.on_view_pop=view_pop
    page.go(page.route)

ft.app(main)
