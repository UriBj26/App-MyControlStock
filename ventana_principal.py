import wx
import wx.adv

from views.agregar_producto import mostrar_agregar
from views.ver_stock import mostrar_stock
from views.registrar_venta import mostrar_venta
from views.productos_agotados import mostrar_agotados


class MyStockControl(wx.Frame):

    def __init__(self, inventario):
        super().__init__(
            None,
            title="MY STOCK CONTROL",
            size=(1000, 600)
        )

        self.inv = inventario

        # --- LOGO DE LA APLICACIÓN ---
        try:
            icono = wx.Icon("logo.png", wx.BITMAP_TYPE_PNG)
            self.SetIcon(icono)
        except Exception as e:
            print("No se pudo cargar el logo:", e)

        # --- BARRA DE MENÚ ---
        menubar = wx.MenuBar()
        menu_archivo = wx.Menu()
        item_salir = menu_archivo.Append(wx.ID_EXIT, "Salir", "Salir de la aplicación")
        
        menu_ayuda = wx.Menu()
        item_acerca = menu_ayuda.Append(wx.ID_ABOUT, "Acerca de...", "Información del programa")

        menubar.Append(menu_archivo, "&Archivo")
        menubar.Append(menu_ayuda, "&Ayuda")
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, lambda e: self.Close(), item_salir)
        self.Bind(wx.EVT_MENU, self.mostrar_info, item_acerca)

        # --- INTERFAZ PRINCIPAL ---
        self.panel = wx.Panel(self)

        self.menu_panel = wx.Panel(self.panel, size=(180, -1))
        self.menu_panel.SetBackgroundColour("#F8F9FA")

        # Contenedor dinámico de contenidos
        self.contenido_panel = wx.Panel(self.panel)
        
        # Sizer maestro del contenedor
        self.contenido_sizer = wx.BoxSizer(wx.VERTICAL)
        self.contenido_panel.SetSizer(self.contenido_sizer)

        menu_sizer = wx.BoxSizer(wx.VERTICAL)
        for label in [
            "Agregar Producto",
            "Ver Stock",
            "Registrar Venta",
            "Productos Agotados",
            "Salir"
        ]:
            boton = wx.StaticText(self.menu_panel, label=f"   {label}   ")
            boton.SetCursor(wx.Cursor(wx.CURSOR_HAND))
            boton.Bind(wx.EVT_LEFT_DOWN, self.navegar)
            menu_sizer.Add(boton, 0, wx.ALL, 12)

        self.menu_panel.SetSizer(menu_sizer)

        principal = wx.BoxSizer(wx.HORIZONTAL)
        principal.Add(self.menu_panel, 0, wx.EXPAND)
        principal.Add(self.contenido_panel, 1, wx.EXPAND | wx.ALL, 15)

        self.panel.SetSizer(principal)

        # Cargar vista inicial
        mostrar_agregar(self)

    def mostrar_info(self, event):
        info = wx.adv.AboutDialogInfo()
        info.SetName("MY STOCK CONTROL")
        info.SetVersion("1.0")
        info.SetDescription(
            "Materia: Programación Orientada a Objetos\n"
            "Año: 2026\n\n"
            "Tecnologías usadas:\n"
            "• Python\n"
            "• wxPython\n"
            "• SQLite"
        )
        info.SetDevelopers(["Adrian Etchenique", "Bejarano Uriel"])
        wx.adv.AboutBox(info)

    def limpiar(self):
        """Elimina todos los widgets y resetea por completo el Sizer maestro."""
        self.contenido_panel.DestroyChildren()
        self.contenido_sizer.Clear(True)

    def navegar(self, event):
        opcion = event.GetEventObject().GetLabel().strip()

        if opcion == "Agregar Producto":
            mostrar_agregar(self)
        elif opcion == "Ver Stock":
            mostrar_stock(self)
        elif opcion == "Registrar Venta":
            mostrar_venta(self)
        elif opcion == "Productos Agotados":
            mostrar_agotados(self)
        elif opcion == "Salir":
            self.Close()