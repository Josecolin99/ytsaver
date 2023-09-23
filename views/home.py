import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from tools import youtube
from tools.paths import media_root

class HomeView:
    def __init__(self, root):
        self.root = root
        self.root_entry = None
        self.url_entry = None
        self.window()

    def window(self):
        self.setup_windows()
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        self.create_entries(frm)
        self.create_buttons(frm)
        
    def setup_windows(self):
        self.root.title("Yt Playlist Downloader #CodedByColin")
        self.root.iconbitmap(media_root('ico/main.ico'))
        
    def seleccionar_ruta(self):
        ruta_seleccionada = filedialog.askdirectory()  # Abre el diálogo de selección de directorio
        self.root_entry = ruta_seleccionada  # Inserta la ruta seleccionada en el Entry de ruta

    def create_entries(self, frame):
        ttk.Label(frame, text="Root:").grid(column=0, row=0, sticky=tk.W)
        ttk.Button(frame, text="Seleccionar Ruta", command=self.seleccionar_ruta).grid(column=1, row=0)
        
        ttk.Label(frame, text="URL:").grid(column=0, row=1, sticky=tk.W)
        self.url_entry = ttk.Entry(frame, width=100)
        self.url_entry.grid(column=1, row=1)

    def create_buttons(self, frame):
        ttk.Button(frame, text="Enviar", command=self.send_data).grid(columnspan=2, row=2)
        ttk.Button(frame, text="Quit", command=self.root.destroy).grid(columnspan=2, row=3)

    def send_data(self):
        root_value = self.root_entry
        url_value = self.url_entry.get()
        if not root_value:
            messagebox.showwarning("Campos vacíos", "Ingrese una ruta para descargar la playlist.")
            return
        if not url_value:
            messagebox.showwarning("Campos vacíos", "Por favor, ingrese una url.")
            return
        youtube.save_playlist(root_value, url_value)

def main():
    root = tk.Tk()
    app = HomeView(root)
    root.mainloop()

if __name__ == "__main__":
    main()
