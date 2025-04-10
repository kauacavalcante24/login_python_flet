import flet as ft

def main(page: ft.Page):
    page.title = 'Login'
    page.window_width = 400
    page.window_height = 700

    text = ft.Container(ft.Text('Conecte-se à sua conta', size=25), alignment=ft.alignment.center, margin=ft.margin.only(bottom=20))
    user_account_text = ft.Text('Nome de usuário ou email')
    user_account = ft.TextField(label='Ex: minha_conta@email.com', suffix_text=".com")
    user_password_text = ft.Text('Senha')
    user_password = ft.TextField(label='Digite a sua senha', password=True, can_reveal_password=True)
    forgot_password = ft.TextButton('Esqueci minha senha')
    button = ft.Container(
        ft.ElevatedButton('Entrar',
            width=200,
            height=50,
        ), alignment=ft.alignment.center, margin=ft.margin.only(top=15))
    made_by_text = ft.Container(
        ft.Text('Made by @kauacavalcante24 (Github)', size=10,),
        alignment=ft.alignment.bottom_center,
        expand=True)

    page.add(
        text,
        user_account_text,
        user_account,
        user_password_text,
        user_password,
        forgot_password,
        button,
        made_by_text
    )

ft.app(target = main)