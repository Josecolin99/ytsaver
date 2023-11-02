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
    def __init__(self):
        self.WIDTH = size(1280)
        self.HEIGHT = size(720)
        
    def start_window(self):
        self.app = ft.app(target=self.main)
        
    def virtualize(self, page: ft.Page):
        page.title = "Hola"
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
        
    def main_container(self):
        columns = ft.Column(spacing=0, controls=[self.upper_container()])
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
                src='C:/secret_files/ytsaver/assets/yt.jpeg',
                width=200,
                height=200,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        return image

if __name__ == "__main__":
    ventana = MiVentana()
    ventana.start_window()


