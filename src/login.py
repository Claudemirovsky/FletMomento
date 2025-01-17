import flet as ft
import re

from utils import CustomColors, Title, InputField


class Login(ft.Container):
    def __init__(self):
        super().__init__()
        self.bgcolor = CustomColors.GREY
        self.alignment = ft.alignment.center
        self.padding = 20
        self.border_radius = 10
        self.width = 400
        self.height = 700
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    spacing=0,
                    controls=[
                        Title(),
                        ft.Text(
                            "Organize, Estude, Conquiste!",
                            style=ft.TextStyle(
                                color=CustomColors.DARK_BLUE, weight=ft.FontWeight.W_800
                            ),
                            size=16,
                        ),
                    ],
                ),
                ft.Divider(color=ft.Colors.WHITE, height=10),
                email := InputField(
                    "Email",
                    "seuemail@exemplo.com",
                    on_blur=self.email_validator,
                ),
                password := InputField(
                    "Senha",
                    "*" * 20,
                    password=True,
                    can_reveal_password=True,
                    on_blur=self.password_validator,
                ),
                ft.Divider(color=ft.Colors.WHITE, height=4),
                ft.Row(
                    controls=[
                        ft.TextButton(
                            "Esqueceu sua senha?   ",
                            on_click=lambda _: print("QQQQQQQQQQQQQQQQ"),
                            style=ft.ButtonStyle(
                                color=CustomColors.DARK_BLUE,
                                text_style=ft.TextStyle(
                                    decoration=ft.TextDecoration.UNDERLINE,
                                    decoration_thickness=2,
                                    decoration_color=CustomColors.DARK_BLUE,
                                    weight=ft.FontWeight.W_800,
                                    color=CustomColors.DARK_BLUE,
                                ),
                            ),
                        ),
                    ],
                    spacing=0,
                    alignment=ft.MainAxisAlignment.END,
                ),
                ft.Divider(color=ft.Colors.WHITE, height=4),
                ft.ElevatedButton(
                    "Entrar",
                    style=ft.ButtonStyle(
                        bgcolor=CustomColors.YELLOW,
                        color=ft.Colors.WHITE,
                        text_style=ft.TextStyle(
                            weight=ft.FontWeight.W_900,
                            size=25,
                        ),
                        padding=20,
                        shape=ft.RoundedRectangleBorder(10),
                    ),
                    width=330,
                    on_click=lambda _: self.page.go("main"),
                ),
                ft.Divider(color=ft.Colors.WHITE, height=4),
                ft.Text(
                    "Não tem conta ainda? ",
                    color=CustomColors.DARK_BLUE,
                    style=ft.TextStyle(
                        decoration=ft.TextDecoration.UNDERLINE,
                        decoration_thickness=2,
                        decoration_color=CustomColors.DARK_BLUE,
                        weight=ft.FontWeight.W_800,
                        color=CustomColors.DARK_BLUE,
                    ),
                    spans=[
                        ft.TextSpan(
                            "Crie agora",
                            style=ft.TextStyle(
                                decoration=ft.TextDecoration.UNDERLINE,
                                decoration_thickness=1,
                                decoration_color=CustomColors.DARK_BLUE,
                                weight=ft.FontWeight.W_800,
                                color=CustomColors.YELLOW,
                            ),
                        )
                    ],
                ),
                ft.Divider(),
                ft.Text("Ou entre com", color=CustomColors.DARK_BLUE, weight=ft.FontWeight.W_800),
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Image(
                                src="facebook.png",
                                fit=ft.ImageFit.COVER,
                                color_blend_mode=ft.BlendMode.EXCLUSION,
                            ),
                            margin=10,
                            padding=10,
                            bgcolor=CustomColors.BLUE,
                            width=80,
                            height=80,
                            border_radius=16,
                        ),
                        ft.Container(
                            content=ft.Image(
                                src="instagram.png",
                                fit=ft.ImageFit.COVER,
                                color_blend_mode=ft.BlendMode.EXCLUSION,
                            ),
                            margin=10,
                            padding=10,
                            bgcolor=CustomColors.BLUE,
                            width=80,
                            height=80,
                            border_radius=16,
                        ),
                        ft.Container(
                            content=ft.Image(
                                src="twitter.png",
                                fit=ft.ImageFit.COVER,
                                color_blend_mode=ft.BlendMode.EXCLUSION,
                            ),
                            margin=10,
                            padding=10,
                            bgcolor=CustomColors.BLUE,
                            width=80,
                            height=80,
                            border_radius=16,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=0,
                ),
            ],
        )

        self.email = email
        self.password = password

    def email_validator(self, e: ft.ControlEvent):
        val = e.control.value
        if not val or Login.simple_email_validation(val):
            self.email.set_error(None)
        else:
            self.email.set_error("Email inválido!")

    def password_validator(self, e: ft.ControlEvent):
        val = e.control.value
        if not val or len(val) < 4:
            self.password.set_error("Sua senha deve ter mais de 4 caracteres!")
        else:
            self.password.set_error(None)

    valid_regex = re.compile(r"^[\w\-_.]+$")

    @staticmethod
    def simple_email_validation(email: str) -> bool:
        if (mid := email.find("@")) == -1:
            return False
        if email.find(" ") != -1:
            return False
        name = email[:mid]
        host = email[mid + 1 :]

        if (
            len(name) == 0
            or name.startswith(".")
            or name.endswith(".")
            or Login.valid_regex.match(name) is None
        ):
            return False

        return not (
            len(host) == 0
            or host.startswith(".")
            or host.endswith(".")
            or "." not in host
            or host.find("..") != -1
            or Login.valid_regex.match(host) is None
        )
