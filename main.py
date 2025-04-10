import flet as ft
from views.home import home_view
from views.login import login_view

def main(page: ft.Page):
    page.title = "App Flet"
    page.window_width = 400
    page.window_height = 700
    page.window_resizable = False
    page.on_route_change = route_change
    page.go("/")

def route_change(route):
    page = route.page  # importante para acessar a página
    page.views.clear()

    if page.route == "/":
        page.views.append(login_view(page))
    elif page.route == "/home":
        page.views.append(home_view(page))

ft.app(target=main)