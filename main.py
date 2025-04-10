import flet as ft
from views.profile import profile_view
from views.login import login_view

def main(page: ft.Page):
    page.title = "App Flet"
    page.window_width = 400
    page.window_height = 700
    page.window_resizable = False
    page.on_route_change = route_change
    page.go("/")

def route_change(route):
    page = route.page
    page.views.clear()

    if page.route == "/":
        page.views.append(login_view(page))
    elif page.route == "/profile":
        page.views.append(profile_view(page))

ft.app(target=main, assets_dir="assets") 