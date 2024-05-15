import flet as ft

def main(page: ft.Page):
    page.title = "Control de stock"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    producto = ft.TextField(label="Producto")
    precio = ft.TextField(label="Precio")
    lista_productos = []
    
    def agregar(e):
        lista_productos.append((producto.value, precio.value))
        print(lista_productos)
        
    def quitar(e):
        elemento_quitado = lista_productos.pop()
        print(elemento_quitado)
    
    
    page.add(
        ft.Row([producto, precio]),
        ft.Row(
        [ft.IconButton(ft.icons.REMOVE, on_click=quitar),
        ft.IconButton(ft.icons.ADD, on_click=agregar)]
        )
    )
    
ft.app(main)