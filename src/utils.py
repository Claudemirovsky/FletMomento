import flet as ft


class CustomColors:
    YELLOW = "#FEC562"
    BLUE = "#4A92FF"
    GREY = "#F5FFF5"
    DARK_BLUE = "#0B2E4F"


class Title(ft.Text):
    def __init__(self, size: int = 40):
        super().__init__()
        self.weight = ft.FontWeight.W_900
        self.size = size
        self.spans = [
            ft.TextSpan("TIME", ft.TextStyle(color=CustomColors.BLUE)),
            ft.TextSpan("WISE", ft.TextStyle(color=CustomColors.YELLOW)),
        ]
        self.no_wrap = True


class InputField(ft.Column):
    def __init__(self, label: str, hint: str, **kwargs):
        super().__init__()
        self.alignment = ft.MainAxisAlignment.START
        self.spacing = 0
        self.controls = [
            ft.Text(
                f"   {label}",
                style=ft.TextStyle(color=CustomColors.DARK_BLUE, weight=ft.FontWeight.W_900),
                size=16,
            ),
            field := ft.TextField(
                hint_text=hint,
                border_radius=10,
                border_color=CustomColors.BLUE,
                width=330,
                color=CustomColors.BLUE,
                error_style=ft.TextStyle(color=ft.Colors.RED, weight=ft.FontWeight.W_600),
                hint_style=ft.TextStyle(color=CustomColors.BLUE, weight=ft.FontWeight.W_400),
                **kwargs,
            ),
        ]
        self.field = field

    def set_error(self, err: str | None):
        if err == self.field.error_text:
            return
        self.field.error_text = err
        self.field.update()
