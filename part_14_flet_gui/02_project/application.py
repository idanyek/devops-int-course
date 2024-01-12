import flet as ft
import sqlite3
import random


def main(page: ft.Page):
    page.title = "Users CRM"
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 300
    page.window_height = 400
    page.window_resizable = False

    def validate(e):
        if all([user_password_text_field.value, user_login_text_field.value, user_age_text_field.value]):
            registration_button.disabled = False
            page.update()

    def register(e):
        # create a connection to the DB file
        connection_manager = sqlite3.connect("users.db")

        # crate a cursor object
        my_cursor = connection_manager.cursor()

        # create a n new table
        my_cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_name TEXT,
                    user_password TEXT,
                    user_age INTEGER,
                    user_is_admin BOOLEAN 
                )  """)

        my_cursor.execute(f"INSERT INTO users VALUES (NULL,"
                          f"'{user_login_text_field.value}',"
                          f"'{user_password_text_field.value}',"
                          f"'{user_age_text_field.value}',"
                          f"'{user_is_admin.value}')")

        connection_manager.commit()
        connection_manager.close()

        # reset user field
        user_login_text_field.value = ""
        user_password_text_field.value = ""
        user_age_text_field.value = ""
        user_is_admin.value = False
        registration_button.disabled = True
        page.update()

    # UI
    header_text = ft.Text(value="User Registration:")
    user_login_text_field = ft.TextField(label="username", width=200, on_change=validate)
    user_password_text_field = ft.TextField(label="password", width=200, on_change=validate, password=True)
    user_age_text_field = ft.TextField(label="age", width=70, text_align=ft.TextAlign.CENTER,
                                       on_change=validate)
    user_is_admin = ft.Checkbox(label="Admin user?")
    registration_button = ft.ElevatedButton(text="Add User", width=200, disabled=True, on_click=register)

    page.add((
        ft.Row([
            ft.Column([
                header_text,
                user_login_text_field,
                user_password_text_field,
                user_age_text_field,
                user_is_admin,
                registration_button
            ])
        ], alignment=ft.MainAxisAlignment.CENTER)
    ))


ft.app(target=main)
