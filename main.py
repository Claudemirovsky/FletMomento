import flet as ft

def main(page: ft.Page):

    YELLOW="#FEC562"
    BLUE="#4A92FF"
    GREY="#F5FFF5"
    DARK_BLUE="#0B2E4F"

    login = ft.Card(
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
                            ]
                    ),

                    #Entrar
                    ft.ElevatedButton(content=ft.Text(value="ENTRAR", color=ft.Colors.WHITE, size=16, weight=ft.FontWeight.BOLD), bgcolor=YELLOW, width=330, height=48),

                    #Não tem conta ainda
                    ft.Row(
                        [
                            ft.Text(value="Não tem conta?", color=DARK_BLUE, weight=ft.FontWeight.BOLD, size=16),
                            ft.TextButton(content=ft.Text(value="Crie agora", text_align=ft.TextAlign.RIGHT, style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, size=16), color=BLUE))
                        ],
                        spacing=0,
                        alignment=ft.MainAxisAlignment.CENTER
                    ),

                    #Ou entre com
                    ft.Text(value="Ou entre com", color=DARK_BLUE, size=20, weight=ft.FontWeight.BOLD)

                    #Icones

                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
            padding=20
        ),
        width=400,
        height=600,
        color=GREY
    )


    '''page.add(
        ft.Container(
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[ft.colors.GREEN, BLUE]
            ),
            content=ft.Text("Vão se foderem")
        )
    )'''
    page.bgcolor = BLUE
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.add(ft.SafeArea(content=login))

ft.app(main)
