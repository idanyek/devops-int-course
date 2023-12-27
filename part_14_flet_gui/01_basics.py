import flet as ft
def main(page: ft.Page):
    def button_click(e: ft.ControlEvent):
        print("Button clicked")
        page.add(ft.Text(value=f"Your Name is {text_field.value}"))
        print(e.control.text)

    # option 1
    t = ft.Text(value="Hi", color="green")
    page.controls.append(t)
    page.update()

    # option 2
    t = ft.Text(value="Hello world", color="red", size=20)
    page.add(t)
    pass

    # option 3 - controls in 1 row
    text_field = ft.TextField(label="enter name", value="my name is ....")
    button = ft.ElevatedButton(text="Click Me!", on_click=button_click)
    row = ft.Row(controls=[
        text_field, button
    ])
    page.add(row)


# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
ft.app(target=main)
