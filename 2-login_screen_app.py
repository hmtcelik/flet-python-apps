import flet as ft


def main(page: ft.Page):
    page.title = "Giris Ekrani"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 500
    page.window_height = 500

    def validate(e):
        if txt_username.value and txt_passwd.value:
            submit_button.disabled = False
        else:
            submit_button.disabled = True

        page.update()

    def submit(e):
        page.clean()
        page.add(
            ft.Row(
                [
                    ft.Text(f"Hoş Geldiniz: {txt_username.value} !", size=30)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    txt_username = ft.TextField(
        label="Kullanici Adi",
        text_align=ft.TextAlign.LEFT,
        width=200,
        on_change=validate,
    )

    txt_passwd = ft.TextField(
        label="Sifre",
        text_align=ft.TextAlign.LEFT,
        width=200,
        password=True,
        on_change=validate,
    )

    submit_button = ft.ElevatedButton(
        text="Giris Yap",
        width=200,
        height=50,
        disabled=True,
        on_click=submit,
    )

    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        txt_username,
                        txt_passwd,
                        submit_button,
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(main)
