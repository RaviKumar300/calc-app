import flet as ft

def main(page: ft.Page):
    # App setup
    page.title = "Minimalist Calc"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    # 1. UI Elements
    txt_number1 = ft.TextField(label="First Number", width=150, keyboard_type=ft.KeyboardType.NUMBER)
    txt_number2 = ft.TextField(label="Second Number", width=150, keyboard_type=ft.KeyboardType.NUMBER)
    result_text = ft.Text(value="Result: ", size=30, weight=ft.FontWeight.BOLD)

    # 2. Logic Function
    def calculate(e):
        try:
            n1 = float(txt_number1.value)
            n2 = float(txt_number2.value)
            
            # CRITICAL FIX: We read 'data' because 'text' property is gone in newer versions
            operator = e.control.data
            
            if operator == "+":
                res = n1 + n2
            else:
                res = n1 - n2
                
            result_text.value = f"Result: {res}"
            result_text.color = ft.Colors.BLACK
        except ValueError:
            result_text.value = "Please enter numbers!"
            result_text.color = ft.Colors.RED
        
        page.update()

    # 3. Add to Page
    # CRITICAL FIX: Used ft.Button with 'content' and 'data' instead of 'text'
    page.add(
        ft.Row([txt_number1, txt_number2], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(
            [
                ft.Button(
                    content=ft.Text("+"), 
                    data="+", 
                    on_click=calculate, 
                    width=70
                ),
                ft.Button(
                    content=ft.Text("-"), 
                    data="-", 
                    on_click=calculate, 
                    width=70
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row([result_text], alignment=ft.MainAxisAlignment.CENTER),
    )

# Use existing app entry point (warnings are fine for now)
ft.app(target=main)
