import flet as ft

def main(page: ft.Page):
    img = ft.Image(src="haroldExhibit.jpg", width=45, height=45, fit=ft.ImageFit.CONTAIN)

    page.title = "NavigationBar Example"
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME_ROUNDED, label="Home"),
            ft.NavigationBarDestination(icon=ft.Image(src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg", width=24, height=24), label="GitHub"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS_ROUNDED, label="Settings"),
        ]
    )
    page.add(
        ft.Row(
            controls=[
                img,
                ft.Text("HAROLD JEY N. MADJOS")
            ],
            alignment=ft.MainAxisAlignment.START
        )
    )

ft.app(target=main)