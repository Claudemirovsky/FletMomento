import flet as ft
from main_menu import MainMenu
from utils import CustomColors
from login import Login

login_view = ft.View(
    route="login",
    bgcolor=ft.Colors.TRANSPARENT,
    decoration=ft.BoxDecoration(
        gradient=ft.LinearGradient(
            [CustomColors.BLUE, CustomColors.DARK_BLUE],
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
        )
    ),
    vertical_alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    controls=[ft.SafeArea(Login())],
)

main_view = MainMenu()
