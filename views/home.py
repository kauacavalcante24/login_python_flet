import flet as ft

USER_EMAIL = 'admin'
USER_PASSWORD = 'ADMIN'

def home_view(page: ft.Page):
   
   welcome_text = ft.Container(
                    ft.Text('Olá, Admin!',
                            size=25,
                            weight=ft.FontWeight.W_100),
                alignment=ft.alignment.center)

   text = ft.Container(
            ft.Text('Você está logado! Clique no botão abaixo para sair da sua conta.'),
            alignment=ft.alignment.center
            )

   button = ft.Container(
                ft.ElevatedButton("Sair da conta",
                                    on_click=lambda e: page.go("/"),
                                    width=200,
                                    height=50),
            alignment=ft.alignment.center, margin=ft.margin.only(top=15))
   
   return ft.View(
        route="/home",
        controls=[
            welcome_text,
            text,
            button,
        ]
    )