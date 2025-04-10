import flet as ft
import time

USER_EMAIL = 'admin'
USER_PASSWORD = 'admin'

def login_view(page: ft.Page):

    alert = ft.Container(
        visible=False,
        bgcolor='red',
        padding=6,
        border_radius=10,
        content=ft.Row([
            ft.Text('Usuário ou senha incorretos!', color='white', expand=True),
            ft.IconButton(icon=ft.icons.CLOSE, on_click=lambda e: close_alert(e))
        ]),
        alignment=ft.alignment.top_center,
    )

    def show_alert(msg):
        alert.content.controls[0].value = msg
        alert.visible = True
        page.update()

    def close_alert(e):
        alert.visible = False
        page.update()

    def is_user(e):
        if user_account.value and user_password.value:
            if user_account.value == USER_EMAIL and user_password.value == USER_PASSWORD:
                page.go('/home')
            else:
                show_alert('Usuário ou senha incorretos!')
                user_account.value = ''
                user_password.value = ''
                page.update()
        else:
            show_alert('Os campos estão vazios!')
            user_account.value = ''
            user_password.value = ''
            page.update()
 
    text = ft.Container(
        ft.Text('Conecte-se à sua conta',
                size=25,
                weight=ft.FontWeight.W_100),
        alignment=ft.alignment.center, margin=ft.margin.only(bottom=20))

    user_account_text = ft.Text('Nome de usuário ou email')
    user_account = ft.TextField(label='Ex: minha_conta@email.com', suffix_text=".com")
    user_password_text = ft.Text('Senha')
    user_password = ft.TextField(label='Digite a sua senha', password=True, can_reveal_password=True)
    forgot_password = ft.TextButton('Esqueci minha senha')
    button = ft.Container(
        ft.ElevatedButton('Entrar',
                            width=200,
                            height=50,
                            on_click=is_user),
        alignment=ft.alignment.center, margin=ft.margin.only(top=15))

    made_by_text = ft.Container(
        ft.Text('Made by @kauacavalcante24 (Github)', size=10),
        alignment=ft.alignment.bottom_center,
        expand=True)

    return ft.View(
        route="/",
        controls=[
            alert,
            text,
            user_account_text,
            user_account,
            user_password_text,
            user_password,
            forgot_password,
            button,
            made_by_text
        ]
    )