# Pokedex Main Page

# Fleet modules
import flet as ft
from flet import border, colors

# Tools modules
from tools import shapes, paths
from tools.screen_adapter import adapt_size as size

import aiohttp
import asyncio


class MiVentana:
    # Config Window
    def __init__(self):
        self.WIDTH = size(1280)
        self.HEIGHT = size(720)
        self.download_path = None
        
    def start_window(self):
        self.app = ft.app(target=self.main)
        
    def virtualize(self, page: ft.Page):
        page.title = "No deberias estar viendo esto"
        page.window_width = self.WIDTH
        page.window_height = self.HEIGHT
        page.window_resizable = False
        page.padding = size(0)
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment= ft.CrossAxisAlignment.CENTER
        
    def main(self, page: ft.Page):
        self.virtualize(page)
        main_container = self.main_container()
        page.add(main_container)
    
    #Content
        
    def main_container(self):
        columns = ft.Column(
            spacing=0, 
            controls=[
                self.upper_container(), 
                self.middle_container(), 
                self.down_container()
                ]
            )
        container = ft.Container(
            columns,
            padding=0,
            width=self.WIDTH,
            height=self.HEIGHT,
            bgcolor='#282828',
        )
        return container
    
    def upper_container(self):
        image = ft.Image(
                src=paths.media_root('yt.png'),
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        return image
    
    def middle_container(self):
        columns = ft.Column(
            spacing=0, 
            controls=[
                ft.TextField()
                ]
            )
        container = ft.Container(
            columns,
            padding=0,
            width=self.WIDTH,
            height=size(150),
            bgcolor='#282828',
        )
        return container
    
    def down_container(self):
        file_picker = ft.FilePicker()

        # Crear un botón
        button = ft.ElevatedButton(
            "Seleccionar Directorio",  # Texto del botón
            on_click=lambda _: file_picker.get_directory_path()  # Acción al hacer clic
        )
        
        # Establecer el manejador de eventos para cuando el FilePicker retorne un resultado
        file_picker.on_result = self.on_file_picker_result
        return ft.Column(controls=[button, file_picker])
    
    def on_file_picker_result(self, event: ft.FilePickerResultEvent):
        # Verifica si el diálogo fue cancelado (en ese caso, event.path será None)
        if event.path is not None:
            self.download_path = event.path
            print(f"Directorio seleccionado: {event.path}")
        else:
            print("Ningún directorio fue seleccionado.")
    
if __name__ == "__main__":
    ventana = MiVentana()
    ventana.start_window()


