import flet as ft

USER_EMAIL = 'admin'
USER_PASSWORD = 'ADMIN'

def profile_view(page: ft.Page):
 
   header = ft.Column(
        controls=[
            ft.Container(
                height=30,
                content=ft.Stack(
                    controls=[
                        ft.Container(
                            content=ft.Text('Sua conta', size=15, weight=ft.FontWeight.W_100),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            content=ft.Icon(ft.icons.MENU),
                            alignment=ft.alignment.center_left
                        )
                    ]
                ),
            ), ft.Divider(height=1, thickness=1, color=ft.colors.GREY)
        ], spacing=5
    )

   profile_photo = ft.Container(
        ft.Container(
                width=100,
                height=100,
                border_radius=50,
                border=ft.border.all(1, ft.colors.BLACK),
                content=ft.Image(
                    src="/icons/user_icon.png",
                    fit=ft.ImageFit.COVER,
                ),
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
        ), alignment=ft.alignment.center, bgcolor=ft.colors.WHITE, padding=3
    )

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
        route="/profile",
        controls=[
            header,
            profile_photo,
            welcome_text,
            text,
            button,
        ]
    )