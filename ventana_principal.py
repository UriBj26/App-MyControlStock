import wx

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

        # --- CREACIÓN DE LA BARRA DE MENÚ ---
        menubar = wx.MenuBar()

        # Menú Archivo
        menu_archivo = wx.Menu()
        item_salir = menu_archivo.Append(wx.ID_EXIT, "Salir", "Salir de la aplicación")
        
        # Menú Acerca de
        menu_acerca = wx.Menu()
        item_acerca = menu_acerca.Append(wx.ID_ABOUT, "Acerca de", "Información del programa")

        # Añadir al MenuBar
        menubar.Append(menu_archivo, "&Archivo")
        menubar.Append(menu_acerca, "Acerca de")
        
        self.SetMenuBar(menubar)

        # Vincular eventos del menú
        self.Bind(wx.EVT_MENU, lambda e: self.Close(), item_salir)
        self.Bind(wx.EVT_MENU, self.mostrar_info, item_acerca)
        # --- FIN DE LA BARRA DE MENÚ ---

        self.panel = wx.Panel(self)

        self.menu_panel = wx.Panel(
            self.panel,
            size=(180, -1)
        )

        self.menu_panel.SetBackgroundColour("#F8F9FA")

        self.contenido_panel = wx.Panel(self.panel)

        menu_sizer = wx.BoxSizer(wx.VERTICAL)

        for label in [
            "Agregar Producto",
            "Ver Stock",
            "Registrar Venta",
            "Productos Agotados",
            "Salir"
        ]:

            boton = wx.StaticText(
                self.menu_panel,
                label=f"   {label}   "
            )

            boton.SetCursor(wx.Cursor(wx.CURSOR_HAND))
            boton.Bind(wx.EVT_LEFT_DOWN, self.navegar)

            menu_sizer.Add(
                boton,
                0,
                wx.ALL,
                12
            )

        self.menu_panel.SetSizer(menu_sizer)

        principal = wx.BoxSizer(wx.HORIZONTAL)

        principal.Add(
            self.menu_panel,
            0,
            wx.EXPAND
        )

        principal.Add(
            self.contenido_panel,
            1,
            wx.EXPAND | wx.ALL,
            15
        )

        self.panel.SetSizer(principal)

        mostrar_agregar(self)

    # Nuevo método para mostrar el mensaje de "Acerca de"
    def mostrar_info(self, event):
        wx.MessageBox("Sistema de Gestión de Inventario v1.0\nDesarrollado con Python y wxPython", 
                      "Acerca de", wx.OK | wx.ICON_INFORMATION)

    def limpiar(self):

        self.contenido_panel.DestroyChildren()

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