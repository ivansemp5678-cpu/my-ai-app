import flet as ft
from openai import OpenAI

# Вставь свой ключ DeepSeek!
client = OpenAI(api_key="sk-06ffdcb0995847a58cee075f3ebd9f74", base_url="https://api.deepseek.com")

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.END # Сообщения снизу

    chat = ft.ListView(expand=True, spacing=10, auto_scroll=True)
    inp = ft.TextField(hint_text="Сообщение...", expand=True)

    def send(e):
        if not inp.value: return
        t = inp.value
        chat.controls.append(ft.Text(f"Я: {t}", color="cyan"))
        inp.value = ""
        page.update()

        try:
            res = client.chat.completions.create(
                model="deepseek-chat",
                messages=[{"role": "user", "content": t}]
            )
            ans = res.choices[0].message.content
            chat.controls.append(ft.Text(f"Бот: {ans}"))
        except Exception as x:
            chat.controls.append(ft.Text(f"Error: {x}", color="red"))
        page.update()

    page.add(chat, ft.Row([inp, ft.IconButton(ft.icons.SEND, on_click=send)]))

ft.app(target=main)
