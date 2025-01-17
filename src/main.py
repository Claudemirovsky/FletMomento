import flet as ft
from views import login_view, main_view


def main(page: ft.Page):
    def route_change(route):
        page.views.clear()
        page.views.append(login_view)
        if route.route == "main":
            page.views.append(main_view)
        page.update()

    def view_pop(view):
        print(f"View -> {view}")
        page.views.pop()
        top_view = page.views[-1]
        if top_view.route is not None:
            page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    # page.go(page.route)
    page.theme = ft.Theme(
        floating_action_button_theme=ft.FloatingActionButtonTheme(
            size_constraints=ft.BoxConstraints(90, 90, 90, 90),
        )
    )
    page.go("/")


ft.app(main, assets_dir="assets")
